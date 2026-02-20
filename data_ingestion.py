import os
import re
import yaml
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

def load_and_parse_markdown(dataset_dir):
    """
    Membaca semua file .md di direktori dan mengekstrak materi beserta metadatanya.
    Memisahkan materi berdasarkan blok YAML Frontmatter.
    """
    documents = []
    
    # Regex untuk menangkap YAML frontmatter dan konten markdown
    # Group 1: YAML metadata
    # Group 2: Markdown content
    # Menggunakan lookahead (?=...) untuk memastikan kita berhenti sebelum frontmatter berikutnya atau End-Of-File
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
                # Konversi array (seperti 'prasyarat') menjadi tipe string (dipisah koma)
                for key, value in metadata.items():
                    if isinstance(value, list):
                        metadata[key] = ", ".join(value)

                # Simpan metadata & teks mentah ke list
                documents.append({
                    "metadata": metadata,
                    "content": markdown_content
                })
            except yaml.YAMLError as e:
                print(f"Error parsing YAML di file {filename}: {e}")

    return documents

def main():
    dataset_dir = "./dataset_mentah"
    persist_dir = "./chroma_db_infotentor"

    print("=== Memulai Pipeline Data Ingestion RAG InfoTentor ===")
    
    # 1. Ekstraksi File & Parse Frontmatter
    print("\n1. Mengekstrak file markdown...")
    raw_docs = load_and_parse_markdown(dataset_dir)
    print(f"Berhasil mengekstrak {len(raw_docs)} materi dari {dataset_dir}.")

    if not raw_docs:
        print("Tidak ada materi untuk diproses. Pipeline dihentikan.")
        return

    # 2. Chunking menggunakan MarkdownHeaderTextSplitter
    print("\n2. Memulai proses pemotongan teks (Chunking)...")
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

    chunked_documents = []
    for doc in raw_docs:
        # MarkdownHeaderTextSplitter otomatis menyimpan header ke dalam blok `metadata` hasil chunk
        splits = markdown_splitter.split_text(doc["content"])
        
        for split in splits:
            # Menggabungkan metadata YAML asli kita + metadata hirarki Heading yang didapat dari splitter
            combined_metadata = {**doc["metadata"], **split.metadata}
            
            # Buat instance Document standar Langchain yang siap dicerna Vector DB
            chunked_doc = Document(page_content=split.page_content, metadata=combined_metadata)
            chunked_documents.append(chunked_doc)
            
    print(f"Berhasil men-chunk teks menjadi {len(chunked_documents)} bagian (chunks).")

    # 3. Embedding & Vector DB Storage (ChromaDB)
    print("\n3. Loading model embedding dan indexing ke Vector DB (ChromaDB)...")
    
    # Anda juga dapat mengganti ini dengan "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" 
    # apabila dirasa butuh performa pencarian konteks bahasa Indonesia yang sedikit lebih akurat nantinya.
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    
    # Simpan document (sekaligus melakukan embedding) ke disk lokal
    vectorstore = Chroma.from_documents(
        documents=chunked_documents,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    
    print(f"\n✅ Pipeline Selesai! Knowledge Base InfoTentor telah tersimpan dalam vector DB di: {persist_dir}")

if __name__ == "__main__":
    main()
