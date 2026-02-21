"""
Data Ingestion Pipeline untuk RAG (Retrieval-Augmented Generation) System

Script ini memproses file markdown dari dataset_mentah/ dan menyimpannya ke ChromaDB
sebagai vector database untuk digunakan oleh RAG agent.

Pipeline:
1. Ekstraksi: Membaca file markdown dan mengekstrak YAML frontmatter + konten
2. Chunking: Memecah dokumen menjadi chunks berdasarkan header markdown
3. Embedding: Menggunakan HuggingFace embeddings untuk membuat vector representations
4. Storage: Menyimpan ke ChromaDB untuk retrieval yang efisien
"""

import os
import re
import yaml
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document


def load_and_parse_markdown(dataset_dir):
    """
    Membaca semua file markdown di direktori dan mengekstrak materi beserta metadatanya.
    
    File markdown diharapkan memiliki format:
    ---
    topik: "Nama Topik"
    mata_kuliah: "Nama Mata Kuliah"
    ...
    ---
    Konten markdown di sini...
    
    Args:
        dataset_dir (str): Path ke direktori yang berisi file markdown
        
    Returns:
        list: List of dictionaries dengan keys 'metadata' dan 'content'
    """
    documents = []
    
    # Regex pattern untuk menangkap YAML frontmatter dan konten markdown
    # Pattern ini mencari:
    # - Group 1: YAML metadata (antara --- dan ---)
    # - Group 2: Markdown content (setelah --- kedua)
    # Menggunakan lookahead untuk memastikan kita berhenti sebelum frontmatter berikutnya
    pattern = re.compile(
        r'^---\s*\n(.*?)\n---\s*\n(.*?)(?=(?:^---\s*\n[a-z_]+:)|\Z)', 
        re.MULTILINE | re.DOTALL
    )

    if not os.path.exists(dataset_dir):
        print(f"Error: Direktori '{dataset_dir}' tidak ditemukan.")
        return documents

    for filename in os.listdir(dataset_dir):
        if not filename.endswith(".md"):
            continue
            
        filepath = os.path.join(dataset_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Mencari seluruh materi yang ada di dalam satu file markdown
        for match in pattern.finditer(content):
            yaml_content = match.group(1).strip()
            markdown_content = match.group(2).strip()

            # Bersihkan pemisah '---' di bagian ter-akhir konten markdown jika terbawa
            if markdown_content.endswith('---'):
                markdown_content = markdown_content[:-3].strip()

            try:
                # Parse YAML metadata string menjadi Dictionary
                metadata = yaml.safe_load(yaml_content)
                if not isinstance(metadata, dict):
                    continue
                
                # Menambahkan nama referensi file ke dalam metadatanya
                metadata['source'] = filename
                
                # ChromaDB hanya menerima tipe data primitif (int, str, float, bool) di metadata
                # Konversi array/list menjadi string (dipisah koma) untuk kompatibilitas
                for key, value in metadata.items():
                    if isinstance(value, list):
                        metadata[key] = ", ".join(str(v) for v in value)

                # Simpan metadata & teks mentah ke list
                documents.append({
                    "metadata": metadata,
                    "content": markdown_content
                })
            except yaml.YAMLError as e:
                print(f"Error parsing YAML di file {filename}: {e}")

    return documents

def main():
    """
    Main function untuk menjalankan pipeline data ingestion.
    
    Pipeline terdiri dari 3 tahap:
    1. Ekstraksi: Membaca dan parse file markdown dengan YAML frontmatter
    2. Chunking: Memecah dokumen menjadi chunks berdasarkan header markdown
    3. Embedding & Storage: Membuat embeddings dan menyimpan ke ChromaDB
    """
    dataset_dir = "./dataset_mentah"
    persist_dir = "./chroma_db_infotentor"

    print("=== Memulai Pipeline Data Ingestion RAG InfoTentor ===")
    
    # Tahap 1: Ekstraksi File & Parse Frontmatter
    print("\n1. Mengekstrak file markdown...")
    raw_docs = load_and_parse_markdown(dataset_dir)
    print(f"Berhasil mengekstrak {len(raw_docs)} materi dari {dataset_dir}.")

    if not raw_docs:
        print("Tidak ada materi untuk diproses. Pipeline dihentikan.")
        return

    # Tahap 2: Chunking menggunakan MarkdownHeaderTextSplitter
    print("\n2. Memulai proses pemotongan teks (Chunking)...")
    # Split berdasarkan header level 1 (#) dan level 2 (##)
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

    chunked_documents = []
    for doc in raw_docs:
        # MarkdownHeaderTextSplitter otomatis menyimpan header ke dalam metadata chunk
        splits = markdown_splitter.split_text(doc["content"])
        
        for split in splits:
            # Menggabungkan metadata YAML asli + metadata header dari splitter
            combined_metadata = {**doc["metadata"], **split.metadata}
            
            # Buat Document instance standar Langchain untuk Vector DB
            chunked_doc = Document(page_content=split.page_content, metadata=combined_metadata)
            chunked_documents.append(chunked_doc)
            
    print(f"Berhasil men-chunk teks menjadi {len(chunked_documents)} bagian (chunks).")

    # Tahap 3: Embedding & Vector DB Storage (ChromaDB)
    print("\n3. Loading model embedding dan indexing ke Vector DB (ChromaDB)...")
    
    # Model embedding: BAAI/bge-small-en-v1.5 (ringan dan cepat)
    # Alternatif untuk bahasa Indonesia: "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    
    # Simpan documents ke ChromaDB (embedding dilakukan otomatis)
    vectorstore = Chroma.from_documents(
        documents=chunked_documents,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    
    print(f"\nPipeline Selesai! Knowledge Base InfoTentor telah tersimpan dalam vector DB di: {persist_dir}")

if __name__ == "__main__":
    main()
