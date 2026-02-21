"""
Streamlit Application untuk Tutor AI Algoritma & Pemrograman

Aplikasi web berbasis Streamlit yang menyediakan interface chatbot untuk:
- Menjawab pertanyaan tentang algoritma dan pemrograman
- Mengeksekusi dan memvalidasi kode Python
- Menampilkan topik pembelajaran yang tersedia dari knowledge base
"""

import streamlit as st
import traceback
import sys
import re
from rag_agent import create_rag_agent
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# ============================================================================
# Streamlit Configuration
# ============================================================================
st.set_page_config(
    page_title="Tutor AI Algoritma & Pemrograman",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# Custom CSS Styling untuk UI yang lebih baik
# ============================================================================
st.markdown("""
<style>
    /* Styling untuk chat messages */
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    
    /* Styling untuk code blocks */
    .stMarkdown code {
        background-color: #f0f2f6;
        padding: 0.2rem 0.4rem;
        border-radius: 0.25rem;
        font-size: 0.9em;
        color: #e83e8c;
    }
    
    .stMarkdown pre {
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 1rem;
        border-radius: 0.5rem;
        overflow-x: auto;
        border-left: 4px solid #007bff;
    }
    
    .stMarkdown pre code {
        background-color: transparent;
        color: inherit;
        padding: 0;
    }
    
    /* Styling untuk headings */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #1f77b4;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    
    /* Styling untuk lists */
    .stMarkdown ul, .stMarkdown ol {
        margin-left: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .stMarkdown li {
        margin-bottom: 0.5rem;
        line-height: 1.6;
    }
    
    /* Styling untuk blockquotes */
    .stMarkdown blockquote {
        border-left: 4px solid #007bff;
        padding-left: 1rem;
        margin-left: 0;
        color: #6c757d;
        font-style: italic;
    }
    
    /* Styling untuk tables */
    .stMarkdown table {
        border-collapse: collapse;
        width: 100%;
        margin: 1rem 0;
    }
    
    .stMarkdown th, .stMarkdown td {
        border: 1px solid #dee2e6;
        padding: 0.75rem;
        text-align: left;
    }
    
    .stMarkdown th {
        background-color: #f8f9fa;
        font-weight: bold;
    }
    
    /* Improve text readability */
    .stMarkdown {
        line-height: 1.7;
        color: #333;
    }
    
    /* Remove weird symbols and clean up */
    .clean-response {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    /* ========================================================================
       Sidebar Styling - Topik yang Tersedia
       ======================================================================== */
    
    /* Styling untuk sidebar secara umum */
    [data-testid="stSidebar"] {
        background-color: #0e1117;
    }
    
    /* Styling untuk text di sidebar agar lebih terlihat */
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] div {
        color: #fafafa !important;
    }
    
    /* Styling khusus untuk list topik */
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] p.topic-item {
        color: #e0e0e0 !important;
        font-size: 0.95rem !important;
        line-height: 1.8 !important;
        margin: 0.4rem 0 !important;
        padding: 0.3rem 0 !important;
    }
    
    /* Styling untuk bullet points di sidebar - lebih terang */
    [data-testid="stSidebar"] p.topic-item {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    /* Styling untuk heading di sidebar */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #ffffff !important;
        font-weight: 600;
    }
    
    /* Styling untuk subheading "Topik Pembelajaran:" */
    [data-testid="stSidebar"] .stMarkdown strong {
        color: #4fc3f7 !important;
        font-size: 1rem;
        font-weight: 600;
    }
    
    /* Styling untuk caption */
    [data-testid="stSidebar"] .stCaption {
        color: #b0b0b0 !important;
        font-size: 0.85rem;
    }
    
    /* Styling untuk divider */
    [data-testid="stSidebar"] hr {
        border-color: #3a3a3a;
        margin: 1rem 0;
    }
    
    /* Hover effect untuk topik (jika ingin interaktif di masa depan) */
    [data-testid="stSidebar"] .topic-item {
        transition: color 0.2s ease;
    }
    
    [data-testid="stSidebar"] .topic-item:hover {
        color: #4fc3f7 !important;
    }
    
    /* Styling untuk mata kuliah */
    [data-testid="stSidebar"] .mata-kuliah-item {
        color: #b0d4ff !important;
        font-weight: 500;
    }
    
    /* ========================================================================
       Error Message Styling - Agar lebih terlihat
       ======================================================================== */
    
    /* Styling untuk error messages */
    .stAlert[data-baseweb="alert"] {
        border-left: 4px solid #ff4444;
        background-color: #2d1b1b !important;
        border-radius: 0.5rem;
        padding: 1rem;
    }
    
    /* Styling untuk error text */
    .stAlert[data-baseweb="alert"] .stMarkdown,
    .stAlert[data-baseweb="alert"] p,
    .stAlert[data-baseweb="alert"] div {
        color: #ffcccc !important;
        font-size: 1rem !important;
        line-height: 1.6 !important;
    }
    
    /* Styling untuk error heading */
    .stAlert[data-baseweb="alert"] .stMarkdown strong {
        color: #ff6666 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
    }
    
    /* Styling untuk warning messages */
    .stAlert[data-baseweb="alert"][data-status="warning"] {
        border-left: 4px solid #ffaa00;
        background-color: #2d241b !important;
    }
    
    .stAlert[data-baseweb="alert"][data-status="warning"] .stMarkdown,
    .stAlert[data-baseweb="alert"][data-status="warning"] p,
    .stAlert[data-baseweb="alert"][data-status="warning"] div {
        color: #ffe0b3 !important;
    }
    
    /* Styling untuk info messages */
    .stAlert[data-baseweb="alert"][data-status="info"] {
        border-left: 4px solid #4fc3f7;
        background-color: #1b2d3a !important;
    }
    
    .stAlert[data-baseweb="alert"][data-status="info"] .stMarkdown,
    .stAlert[data-baseweb="alert"][data-status="info"] p,
    .stAlert[data-baseweb="alert"][data-status="info"] div {
        color: #b3e5fc !important;
    }
    
    /* Styling untuk success messages */
    .stAlert[data-baseweb="alert"][data-status="success"] {
        border-left: 4px solid #4caf50;
        background-color: #1b2d1f !important;
    }
    
    .stAlert[data-baseweb="alert"][data-status="success"] .stMarkdown,
    .stAlert[data-baseweb="alert"][data-status="success"] p,
    .stAlert[data-baseweb="alert"][data-status="success"] div {
        color: #c8e6c9 !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# Session State Initialization
# ============================================================================
# Inisialisasi session state untuk menyimpan chat history dan agent state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent_initialized" not in st.session_state:
    st.session_state.agent_initialized = False

if "run_agent" not in st.session_state:
    st.session_state.run_agent = None


# ============================================================================
# Helper Functions untuk Formatting Response
# ============================================================================
def clean_and_format_response(text):
    """
    Membersihkan dan memformat respons AI agar lebih mudah dibaca.
    
    Args:
        text (str, list, or any): Raw response text dari AI (bisa string, list, atau tipe lain)
        
    Returns:
        str: Cleaned and formatted text
    """
    # Handle berbagai tipe input
    if text is None:
        return ""
    
    # Jika input adalah list, gabungkan menjadi string
    if isinstance(text, list):
        # Jika list berisi string, gabungkan dengan newline
        if all(isinstance(item, str) for item in text):
            text = '\n'.join(str(item) for item in text)
        else:
            # Jika list berisi objek lain, convert ke string
            text = '\n'.join(str(item) for item in text)
    
    # Convert ke string jika belum string
    if not isinstance(text, str):
        text = str(text)
    
    if not text:
        return ""
    
    # Hapus karakter kontrol yang tidak perlu
    text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', text)
    
    # Normalize whitespace (multiple spaces menjadi single space)
    text = re.sub(r' +', ' ', text)
    
    # Normalize line breaks (multiple newlines menjadi max 2)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Pastikan code blocks memiliki format yang benar
    # Fix markdown code blocks
    text = re.sub(r'```(\w+)?\n', r'```\1\n', text)
    
    # Fix inline code yang tidak ter-format dengan baik
    text = re.sub(r'`([^`\n]+)`', r'`\1`', text)
    
    # Pastikan heading memiliki spacing yang benar
    text = re.sub(r'\n(#{1,6})\s+', r'\n\n\1 ', text)
    
    # Fix list formatting
    # Perbaiki pattern regex: escape - atau letakkan di akhir character class
    text = re.sub(r'\n([*\-+])\s+', r'\n\n\1 ', text)
    text = re.sub(r'\n(\d+\.)\s+', r'\n\n\1 ', text)
    
    # Remove trailing whitespace
    text = text.strip()
    
    return text


def render_ai_response(response_text):
    """
    Render AI response dengan formatting yang lebih baik.
    
    Args:
        response_text (str, list, or any): Response text dari AI (bisa berbagai tipe)
    """
    if not response_text:
        return
    
    # Convert response ke string jika perlu
    if isinstance(response_text, list):
        # Jika list, gabungkan menjadi string
        if all(isinstance(item, str) for item in response_text):
            response_text = '\n'.join(response_text)
        else:
            response_text = '\n'.join(str(item) for item in response_text)
    elif not isinstance(response_text, str):
        response_text = str(response_text)
    
    # Clean response
    cleaned_response = clean_and_format_response(response_text)
    
    # Split response menjadi sections untuk better rendering
    # Deteksi code blocks dengan pattern yang lebih robust
    code_block_pattern = r'```(\w+)?\s*\n(.*?)```'
    parts = []
    last_end = 0
    
    for match in re.finditer(code_block_pattern, cleaned_response, re.DOTALL):
        # Text sebelum code block
        if match.start() > last_end:
            text_part = cleaned_response[last_end:match.start()].strip()
            if text_part:
                parts.append(('text', text_part))
        
        # Code block
        language = match.group(1) or 'python'
        code = match.group(2).strip()
        if code:  # Hanya tambahkan jika ada kode
            parts.append(('code', code, language))
        last_end = match.end()
    
    # Text setelah code block terakhir
    if last_end < len(cleaned_response):
        text_part = cleaned_response[last_end:].strip()
        if text_part:
            parts.append(('text', text_part))
    
    # Render parts
    if not parts:
        # Jika tidak ada code blocks, render langsung
        st.markdown(cleaned_response)
    else:
        for part in parts:
            if part[0] == 'text':
                # Render text dengan markdown
                st.markdown(part[1])
            elif part[0] == 'code':
                # Render code dengan syntax highlighting
                try:
                    st.code(part[1], language=part[2])
                except:
                    # Fallback jika language tidak didukung
                    st.code(part[1], language='text')


def get_topics_from_db():
    """
    Mengambil daftar topik unik dari ChromaDB untuk ditampilkan di sidebar.
    
    Function ini melakukan:
    1. Mengecek apakah database ada dan berisi data
    2. Mengambil semua dokumen dari ChromaDB
    3. Mengekstrak metadata 'topik' dan 'mata_kuliah' dari dokumen
    4. Mengembalikan list unik dari topik dan mata kuliah
    
    Returns:
        tuple: (topics_list, mata_kuliah_list, error_message)
               - topics_list: List of unique topics
               - mata_kuliah_list: List of unique mata kuliah
               - error_message: Error message jika ada, None jika sukses
    """
    import os
    
    persist_dir = "./chroma_db_infotentor"
    
    # Cek apakah direktori ChromaDB ada
    if not os.path.exists(persist_dir):
        return [], [], f"❌ Database belum dibuat. Direktori `{persist_dir}` tidak ditemukan.\n\n**Solusi:** Jalankan `python data_ingestion.py` terlebih dahulu untuk membuat database."
    
    # Cek apakah direktori kosong
    if os.path.exists(persist_dir) and not os.listdir(persist_dir):
        return [], [], f"⚠️ Database kosong. Direktori `{persist_dir}` ada tapi tidak berisi data.\n\n**Solusi:** Jalankan `python data_ingestion.py` untuk mengisi database."
    
    try:
        embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
        
        vectorstore = Chroma(
            persist_directory=persist_dir,
            embedding_function=embeddings
        )
        
        # Coba ambil semua dokumen menggunakan get() method (lebih efisien)
        try:
            # Method get() untuk mendapatkan semua dokumen tanpa query
            all_data = vectorstore.get()
            if all_data and len(all_data.get("ids", [])) > 0:
                # Konversi ke format Document
                from langchain_core.documents import Document
                all_docs = []
                for i, doc_id in enumerate(all_data["ids"]):
                    content = all_data["documents"][i] if "documents" in all_data else ""
                    metadata = all_data["metadatas"][i] if "metadatas" in all_data else {}
                    all_docs.append(Document(page_content=content, metadata=metadata))
            else:
                # Jika get() tidak mengembalikan data, coba dengan similarity_search
                queries = ["algoritma", "pemrograman", "struktur data", "logika", "matematika"]
                all_docs = []
                seen_ids = set()
                
                for query in queries:
                    # Gunakan similarity_search langsung dari vectorstore
                    docs = vectorstore.similarity_search(query, k=200)
                    for doc in docs:
                        doc_id = hash(doc.page_content[:50])
                        if doc_id not in seen_ids:
                            all_docs.append(doc)
                            seen_ids.add(doc_id)
        except Exception as get_error:
            # Fallback ke similarity_search method
            queries = ["algoritma", "pemrograman", "struktur data", "logika", "matematika"]
            all_docs = []
            seen_ids = set()
            
            for query in queries:
                # Gunakan similarity_search langsung dari vectorstore
                docs = vectorstore.similarity_search(query, k=200)
                for doc in docs:
                    doc_id = hash(doc.page_content[:50])
                    if doc_id not in seen_ids:
                        all_docs.append(doc)
                        seen_ids.add(doc_id)
        
        # Jika tidak ada dokumen sama sekali
        if not all_docs:
            return [], [], f"⚠️ Database ada tapi tidak berisi dokumen.\n\n**Solusi:** Jalankan `python data_ingestion.py` untuk mengisi database dengan data dari `dataset_mentah/`."
        
        # Ekstrak topik unik dari metadata
        topics = set()
        mata_kuliah = set()
        
        for doc in all_docs:
            metadata = doc.metadata
            if "topik" in metadata and metadata["topik"]:
                topics.add(metadata["topik"])
            if "mata_kuliah" in metadata and metadata["mata_kuliah"]:
                mata_kuliah.add(metadata["mata_kuliah"])
        
        # Jika tidak ada topik yang ditemukan (tapi ada dokumen)
        if not topics and not mata_kuliah:
            return [], [], f"ℹ️ Database berisi {len(all_docs)} dokumen, tapi tidak ada metadata 'topik' atau 'mata_kuliah'.\n\n**Kemungkinan:** Metadata belum diisi dengan benar saat ingestion."
        
        return sorted(list(topics)), sorted(list(mata_kuliah)), None
        
    except Exception as e:
        error_msg = f"❌ Error saat membaca database: {type(e).__name__}: {str(e)}\n\n**Detail:** {traceback.format_exc()[:500]}"
        return [], [], error_msg


def initialize_agent():
    """
    Inisialisasi RAG Agent jika belum diinisialisasi.
    
    Function ini:
    1. Membaca API key dari Streamlit secrets
    2. Membuat RAG agent dengan API key tersebut
    3. Menyimpan agent ke session state untuk digunakan di seluruh aplikasi
    
    Raises:
        SystemExit: Jika API key tidak ditemukan atau agent gagal diinisialisasi
    """
    if not st.session_state.agent_initialized:
        try:
            # Ambil API key dari Streamlit secrets
            try:
                api_key = st.secrets["GOOGLE_API_KEY"]
            except (FileNotFoundError, KeyError):
                st.error("⚠️ API Key tidak ditemukan. Pastikan file `.streamlit/secrets.toml` sudah dibuat dengan GOOGLE_API_KEY!")
                st.stop()
            
            # Buat agent dengan session_id berdasarkan Streamlit session
            session_id = st.session_state.get("session_id", "default")
            run_agent, _ = create_rag_agent(api_key, session_id=session_id)
            
            st.session_state.run_agent = run_agent
            st.session_state.agent_initialized = True
            
        except Exception as e:
            error_type = type(e).__name__
            error_msg = str(e)
            tb_str = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
            
            st.error(f"❌ Error saat menginisialisasi agent: {error_type}: {error_msg}")
            
            # Tampilkan traceback lengkap dalam expander
            with st.expander("🔍 Lihat Detail Error (Traceback)", expanded=False):
                st.code(tb_str, language="python")
                st.caption("💡 **Tips:** Error ini juga muncul di terminal/console tempat Anda menjalankan `streamlit run app.py`")
            
            # Print ke console juga
            print("="*50, file=sys.stderr)
            print("ERROR: Inisialisasi Agent Gagal", file=sys.stderr)
            print("="*50, file=sys.stderr)
            traceback.print_exc()
            print("="*50, file=sys.stderr)
            
            st.stop()


# ============================================================================
# Sidebar - Knowledge Base Information
# ============================================================================
with st.sidebar:
    st.header("📚 Informasi Knowledge Base")
    
    # Tombol Bersihkan Riwayat
    if st.button("🗑️ Bersihkan Riwayat Obrolan", use_container_width=True):
        st.session_state.messages = []
        st.session_state.agent_initialized = False
        st.session_state.run_agent = None
        st.rerun()
    
    st.divider()
    
    # Tampilkan Topik dari Database
    st.subheader("📖 Topik yang Tersedia")
    
    with st.spinner("Memuat topik dari database..."):
        topics, mata_kuliah_list, error_msg = get_topics_from_db()
    
    # Tampilkan error jika ada
    if error_msg:
        st.warning(error_msg)
        with st.expander("🔧 Cara Memperbaiki"):
            st.code("""
# Di terminal, jalankan:
python data_ingestion.py

# Pastikan file markdown ada di folder dataset_mentah/
# Setelah selesai, refresh halaman ini.
            """, language="bash")
    
    if topics:
        st.markdown("**Topik Pembelajaran:**")
        # Gunakan markdown dengan styling khusus untuk setiap topik
        topics_html = ""
        for topic in topics[:20]:  # Batasi 20 topik pertama
            topics_html += f'<p class="topic-item" style="color: #e0e0e0; font-size: 0.95rem; line-height: 1.8; margin: 0.4rem 0; padding: 0.3rem 0;">• {topic}</p>'
        st.markdown(topics_html, unsafe_allow_html=True)
        
        if len(topics) > 20:
            st.caption(f"... dan {len(topics) - 20} topik lainnya")
    elif not error_msg:
        # Hanya tampilkan info jika tidak ada error (artinya database ada tapi kosong)
        st.info("Belum ada topik yang tersedia. Pastikan database sudah diinisialisasi dengan `data_ingestion.py`.")
    
    if mata_kuliah_list:
        st.divider()
        st.markdown("**Mata Kuliah:**")
        # Gunakan markdown dengan styling khusus untuk mata kuliah
        mk_html = ""
        for mk in mata_kuliah_list:
            mk_html += f'<p class="mata-kuliah-item" style="color: #b0d4ff; font-size: 0.95rem; line-height: 1.8; margin: 0.4rem 0; padding: 0.3rem 0; font-weight: 500;">📘 {mk}</p>'
        st.markdown(mk_html, unsafe_allow_html=True)
    
    st.divider()
    st.caption("💡 **Tips:** Gunakan chat untuk bertanya tentang materi atau minta bantuan menguji kode Python!")


# ============================================================================
# Main Content - Chat Interface
# ============================================================================
st.title("🤖 Tutor AI Algoritma & Pemrograman")
st.markdown("Selamat datang! Saya adalah asisten AI yang siap membantu Anda belajar algoritma dan pemrograman. "
            "Saya dapat menjawab pertanyaan tentang teori dan membantu menguji kode Python Anda.")

# Inisialisasi agent (hanya sekali saat pertama kali load)
initialize_agent()

# Render chat history (riwayat obrolan sebelumnya)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            # Render AI response dengan formatting yang lebih baik
            render_ai_response(message["content"])
        else:
            # Render user message biasa
            st.markdown(message["content"])

# Input handling: Tangkap input dari user dan proses dengan agent
if prompt := st.chat_input("Tanyakan materi atau minta saya uji kode Python..."):
    # Tambahkan pesan pengguna ke session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Tampilkan pesan pengguna
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Tampilkan respons AI
    with st.chat_message("assistant"):
        with st.spinner("🤔 Sedang memproses..."):
            try:
                # Panggil agent executor
                result = st.session_state.run_agent(prompt)
                
                # Extract response - handle berbagai format
                if isinstance(result, dict):
                    response = result.get("output", result.get("response", str(result)))
                elif isinstance(result, str):
                    response = result
                elif isinstance(result, list):
                    # Jika list, gabungkan menjadi string
                    response = '\n'.join(str(item) for item in result)
                else:
                    response = str(result)
                
                # Pastikan response adalah string
                if not isinstance(response, str):
                    response = str(response)
                
                # Tampilkan respons dengan formatting yang lebih baik
                render_ai_response(response)
                
                # Tambahkan respons ke session state (simpan sebagai string)
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                error_type = type(e).__name__
                error_msg = str(e)
                tb_str = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
                
                # Deteksi jenis error untuk pesan yang lebih informatif
                is_quota_error = "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg or "quota" in error_msg.lower()
                is_model_error = "404" in error_msg or "NOT_FOUND" in error_msg
                
                if is_quota_error:
                    error_display = """❌ **Quota API Habis**
                    
Maaf, quota Google Gemini API Anda telah habis. Ini biasanya terjadi karena:
- Anda telah mencapai batas penggunaan harian/bulanan untuk free tier
- Model yang digunakan tidak memiliki quota tersedia

**Solusi:**
1. ⏰ Tunggu beberapa saat (quota biasanya reset setiap hari)
2. 📊 Periksa quota Anda di: [Google AI Rate Limits](https://ai.dev/rate-limit)
3. 🔄 Coba refresh halaman dan kirim ulang pesan
4. 💳 Pertimbangkan untuk upgrade ke paid plan jika diperlukan

Aplikasi akan otomatis mencoba model lain yang mungkin memiliki quota tersedia."""
                    st.warning(error_display)
                elif is_model_error:
                    error_display = f"❌ **Model Tidak Ditemukan**: Model yang diminta tidak tersedia atau tidak didukung.\n\nDetail: {error_msg}"
                    st.error(error_display)
                else:
                    # Error umum - tampilkan dengan format yang lebih jelas
                    error_display = f"""❌ **Maaf, terjadi kesalahan**

**Jenis Error:** `{error_type}`

**Pesan Error:**
{error_msg}

**Saran:**
- Coba refresh halaman dan kirim ulang pertanyaan
- Pastikan format pertanyaan Anda jelas dan lengkap
- Jika error berlanjut, lihat detail error di bawah ini"""
                    st.error(error_display)
                
                # Tampilkan traceback lengkap dalam expander
                with st.expander("🔍 Lihat Detail Error (Traceback)", expanded=False):
                    st.code(tb_str, language="python")
                    st.caption("💡 **Tips:** Error ini juga muncul di terminal/console tempat Anda menjalankan `streamlit run app.py`")
                
                # Print ke console juga untuk debugging
                print("="*50, file=sys.stderr)
                print(f"ERROR: {error_type}: {error_msg}", file=sys.stderr)
                print("="*50, file=sys.stderr)
                traceback.print_exc()
                print("="*50, file=sys.stderr)
                
                # Simpan error message ke chat history
                st.session_state.messages.append({"role": "assistant", "content": error_display})
