# 🤖 Tutor AI Algoritma & Pemrograman

Aplikasi chatbot berbasis RAG (Retrieval-Augmented Generation) yang berfungsi sebagai tutor AI untuk pembelajaran algoritma dan pemrograman. Aplikasi ini menggunakan Google Gemini, LangChain, dan ChromaDB untuk menyediakan jawaban yang akurat berdasarkan knowledge base yang telah di-curate.

## 📋 Daftar Isi

- [Fitur](#-fitur)
- [Arsitektur](#-arsitektur)
- [Teknologi yang Digunakan](#-teknologi-yang-digunakan)
- [Prerequisites](#-prerequisites)
- [Instalasi](#-instalasi)
- [Konfigurasi](#-konfigurasi)
- [Penggunaan](#-penggunaan)
- [Struktur Proyek](#-struktur-proyek)
- [Troubleshooting](#-troubleshooting)
- [Lisensi](#-lisensi)

## ✨ Fitur

- **Penjelasan Materi**: Menjawab pertanyaan teori tentang algoritma dan pemrograman dari knowledge base yang telah di-curate
- **Eksekusi Kode Python**: Mampu menulis, mengeksekusi, dan memvalidasi kode Python secara real-time
- **Riwayat Obrolan**: Mengingat konteks percakapan sebelumnya untuk memberikan jawaban yang lebih relevan
- **Antarmuka Pengguna Interaktif**: Dibangun dengan Streamlit untuk pengalaman pengguna yang intuitif
- **Error Handling yang Robust**: Menangani error dengan baik, termasuk quota API dan masalah koneksi

## 🏗️ Arsitektur

```
┌─────────────────┐
│   Streamlit UI  │
│     (app.py)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   RAG Agent     │
│  (rag_agent.py) │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌─────────┐ ┌──────────────┐
│ChromaDB │ │ Google Gemini│
│Vector DB│ │     API      │
└─────────┘ └──────────────┘
```

### Komponen Utama

1. **Data Ingestion Pipeline** (`data_ingestion.py`)
   - Memproses file markdown dari `dataset_mentah/`
   - Mengekstrak metadata dari YAML frontmatter
   - Melakukan chunking berdasarkan header markdown
   - Membuat embeddings dan menyimpan ke ChromaDB

2. **RAG Agent** (`rag_agent.py`)
   - Memuat vector database (ChromaDB)
   - Menginisialisasi tools: Knowledge Base Retriever dan Python Executor
   - Mengatur LLM (Google Gemini) dengan fallback mechanism
   - Mengelola chat history dan memory

3. **Streamlit UI** (`app.py`)
   - Antarmuka pengguna untuk interaksi dengan chatbot
   - Menampilkan topik yang tersedia dari database
   - Menangani error dan menampilkan pesan yang informatif

## 🛠️ Teknologi yang Digunakan

- **Python 3.8+**
- **Streamlit**: Framework untuk membuat web app
- **LangChain**: Framework untuk membangun aplikasi LLM
- **ChromaDB**: Vector database untuk menyimpan embeddings
- **HuggingFace Embeddings**: Model embedding untuk semantic search
- **Google Gemini API**: LLM untuk generating responses
- **LangGraph**: Untuk agent orchestration

## 📦 Prerequisites

Sebelum memulai, pastikan Anda telah menginstal:

- Python 3.8 atau lebih baru
- pip (Python package manager)
- Git (untuk clone repository)

## 🚀 Instalasi

### 1. Clone Repository

```bash
git clone <URL_REPOSITORI_ANDA>
cd Tubes
```

### 2. Buat dan Aktifkan Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Konfigurasi

### 1. Setup Google Gemini API Key

Aplikasi ini memerlukan Google Gemini API Key. Untuk keamanan, API key disimpan di file `secrets.toml` yang tidak akan di-commit ke Git.

1. Buat direktori `.streamlit` di root proyek jika belum ada:
   ```bash
   mkdir .streamlit
   ```

2. Buat file `secrets.toml` di dalam direktori `.streamlit/`:
   ```toml
   GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
   ```
   Ganti `YOUR_GEMINI_API_KEY` dengan API key Google Gemini Anda yang sebenarnya.

   > **Cara mendapatkan API Key:**
   > 1. Kunjungi [Google AI Studio](https://makersuite.google.com/app/apikey)
   > 2. Buat API key baru
   > 3. Copy dan paste ke file `secrets.toml`

   > **⚠️ PENTING**: File `.streamlit/secrets.toml` sudah ditambahkan ke `.gitignore` untuk mencegahnya ter-commit ke repositori publik.

3. (Opsional) File template `secrets.toml.example` sudah tersedia sebagai referensi.

### 2. Ingest Data ke ChromaDB

Jalankan script `data_ingestion.py` untuk memproses materi markdown dan menyimpannya ke ChromaDB:

```bash
python data_ingestion.py
```

Script ini akan:
- Membaca semua file `.md` dari folder `dataset_mentah/`
- Mengekstrak metadata dari YAML frontmatter
- Melakukan chunking berdasarkan header markdown
- Membuat embeddings menggunakan HuggingFace model
- Menyimpan ke ChromaDB di direktori `chroma_db_infotentor/`

**Output yang diharapkan:**
```
=== Memulai Pipeline Data Ingestion RAG InfoTentor ===

1. Mengekstrak file markdown...
Berhasil mengekstrak X materi dari ./dataset_mentah.

2. Memulai proses pemotongan teks (Chunking)...
Berhasil men-chunk teks menjadi Y bagian (chunks).

3. Loading model embedding dan indexing ke Vector DB (ChromaDB)...
Pipeline Selesai! Knowledge Base InfoTentor telah tersimpan dalam vector DB di: ./chroma_db_infotentor
```

## 🎯 Penggunaan

### Menjalankan Aplikasi

Setelah data di-ingest, jalankan aplikasi Streamlit:

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser default Anda (biasanya di `http://localhost:8501`).

### Menggunakan Chatbot

Di antarmuka chatbot, Anda bisa:

1. **Bertanya tentang Konsep/Teori**
   - Contoh: "Apa itu Binary Search?"
   - Bot akan mencari informasi dari knowledge base dan memberikan penjelasan

2. **Meminta Bantuan dengan Kode Python**
   - Contoh: "Buatkan kode Python untuk mencari angka 5 dari array [1,3,5,7,9] menggunakan Binary Search dan buktikan apakah kodenya berhasil!"
   - Bot akan menulis kode, mengeksekusinya, dan memvalidasi hasilnya

3. **Menggunakan Fitur Sidebar**
   - **Bersihkan Riwayat Obrolan**: Mulai percakapan baru
   - **Topik yang Tersedia**: Lihat daftar topik pembelajaran yang ada di database

## 📁 Struktur Proyek

```
Tubes/
│
├── app.py                      # Streamlit UI application
├── rag_agent.py                # RAG Agent dengan tools dan LLM
├── data_ingestion.py           # Pipeline untuk ingest data ke ChromaDB
├── requirements.txt            # Python dependencies
├── README.md                    # Dokumentasi proyek (file ini)
├── .gitignore                  # File yang diabaikan oleh Git
│
├── .streamlit/
│   ├── secrets.toml            # API keys (JANGAN di-commit!)
│   └── secrets.toml.example    # Template untuk secrets.toml
│
├── dataset_mentah/              # File markdown sumber data
│   ├── InfoTentor_KB_part1.md
│   ├── InfoTentor_KB_part2.md
│   └── ...
│
└── chroma_db_infotentor/       # ChromaDB storage (auto-generated, JANGAN di-commit!)
    └── chroma.sqlite3
```

## 🔧 Troubleshooting

### Error: "API Key tidak ditemukan"

**Solusi:**
- Pastikan file `.streamlit/secrets.toml` sudah dibuat
- Pastikan format file benar: `GOOGLE_API_KEY="your_key_here"`
- Restart aplikasi Streamlit setelah membuat/mengubah `secrets.toml`

### Error: "Database belum dibuat" atau "Belum ada topik yang tersedia"

**Solusi:**
```bash
python data_ingestion.py
```
Pastikan script berjalan tanpa error dan direktori `chroma_db_infotentor/` terbuat.

### Error: "429 RESOURCE_EXHAUSTED" (Quota API Habis)

**Solusi:**
- Aplikasi akan otomatis mencoba model lain yang mungkin memiliki quota tersedia
- Tunggu beberapa saat (quota biasanya reset setiap hari)
- Periksa quota Anda di: [Google AI Rate Limits](https://ai.dev/rate-limit)
- Pertimbangkan untuk upgrade ke paid plan jika diperlukan

### Error: "Model tidak ditemukan" (404 NOT_FOUND)

**Solusi:**
- Aplikasi memiliki fallback mechanism yang akan mencoba model lain secara otomatis
- Pastikan API key valid dan memiliki akses ke Gemini API
- Periksa apakah model yang digunakan tersedia di region Anda

### Error saat menjalankan `data_ingestion.py`

**Kemungkinan penyebab:**
- File markdown tidak ada di folder `dataset_mentah/`
- Format YAML frontmatter tidak valid
- Masalah encoding (pastikan file menggunakan UTF-8)

**Solusi:**
- Pastikan folder `dataset_mentah/` berisi file `.md`
- Periksa format YAML frontmatter di file markdown
- Pastikan file markdown menggunakan encoding UTF-8

## 📝 Catatan Penting

1. **API Key Security**: Jangan pernah commit file `.streamlit/secrets.toml` ke Git. File ini sudah ditambahkan ke `.gitignore`.

2. **Database Size**: Direktori `chroma_db_infotentor/` bisa menjadi cukup besar. Direktori ini juga sudah ditambahkan ke `.gitignore`.

3. **Model Embedding**: Default menggunakan `BAAI/bge-small-en-v1.5`. Untuk performa yang lebih baik dengan bahasa Indonesia, pertimbangkan menggunakan `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.

4. **Quota Management**: Google Gemini API memiliki batas quota untuk free tier. Aplikasi akan otomatis mencoba model lain jika quota habis, tetapi untuk penggunaan intensif, pertimbangkan upgrade ke paid plan.

## 🤝 Kontribusi

Kontribusi sangat diterima! Jika Anda ingin berkontribusi:

1. Fork repository ini
2. Buat branch untuk fitur baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buka Pull Request

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik. Silakan gunakan sesuai kebutuhan Anda.

## 👥 Authors

- [Nama Anda] - *Initial work*

## 🙏 Acknowledgments

- Google Gemini untuk API LLM
- LangChain untuk framework RAG
- ChromaDB untuk vector database
- Streamlit untuk UI framework
- HuggingFace untuk embedding models

---

**Happy Coding! 🚀**
