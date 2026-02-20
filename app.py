import streamlit as st
from PIL import Image
import google.generativeai as genai
import io

try:
    GENAI_API_KEY = st.secrets["GOOGLE_API_KEY"]
except FileNotFoundError:
    st.error("API Key tidak ditemukan. Pastikan file .streamlit/secrets.toml sudah dibuat!")
    st.stop()

genai.configure(api_key=GENAI_API_KEY)

def extract_math_from_image(image_input):
    model_vision = genai.GenerativeModel('gemini-flash-latest')
    
    prompt_ocr = """
    Tugasmu adalah melihat gambar ini dan mengekstrak soal matematikanya saja.
    Contoh: Jika di gambar ada tulisan "Ayo hitung 3 + 2", outputmu HANYA "3 + 2".
    Jangan tambahkan kata-kata lain.
    """
    
    with st.spinner('Sedang membaca soal...'):
        response = model_vision.generate_content([prompt_ocr, image_input])
        return response.text.strip()

def generate_dyscalculia_poster(math_problem):
    model_imagen = genai.GenerativeModel('gemini-2.0-flash-exp-image-generation')
    
    prompt_poster = f"""
    Buatlah sebuah gambar infografis poster edukasi yang dirancang khusus untuk anak dengan diskalkulia 
    untuk membantu mereka memahami dan menjawab soal matematika ini: "{math_problem}".

    Panduan Desain (PENTING):
    1.  **Visual Konkret:** JANGAN HANYA GUNAKAN ANGKA. Setiap angka dalam soal HARUS diwakili oleh jumlah objek nyata yang lucu dan berwarna.
        * Contoh: Jika soalnya "3 + 2", gambarkan kelompok berisi 3 apel merah dan kelompok berisi 2 jeruk oranye.
    2.  **Tunjukkan Prosesnya:**
        * Jika Tambah (+): Tunjukkan dua kelompok objek digabungkan menjadi satu kelompok besar.
        * Jika Kurang (-): Tunjukkan kelompok awal, lalu silang (X) objek yang dikurangi, dan tunjukkan sisanya.
        * Jika Kali (x): Tunjukkan dalam bentuk baris dan kolom (grid) objek.
    3.  **Jawaban Akhir Jelas:** Tampilkan hasil akhirnya baik sebagai kumpulan objek maupun angka besar yang mudah dibaca.
    4.  **Gaya Visual:** Gunakan latar belakang bersih (krem/putih gading), warna-warna kontras tinggi, garis tebal, dan tata letak yang tidak berantakan (uncluttered). Gaya ilustrasi buku anak-anak yang ramah.
    """
    
    with st.spinner('Sedang menggambar poster jawaban (ini butuh waktu sedikit lama)...'):
        # Meminta Gemini membuat gambar
        response = model_imagen.generate_content(prompt_poster)
        
        # Mengambil data gambar dari respons
        # Gemini biasanya mengembalikan gambar dalam format raw data di bagian 'parts'
        try:
            img_data = response.parts[0].inline_data.data
            img = Image.open(io.BytesIO(img_data))
            return img
        except Exception as e:
            raise Exception(f"Gagal memproses gambar dari AI. Mungkin model sedang sibuk atau kuota habis. Detail: {e}")


st.set_page_config(page_title="Teman Hitung Visual", page_icon="🎨")

st.title("🎨 Teman Hitung Visual")
st.write("Foto soal matematikamu (Tambah, Kurang, Kali, Bagi). Aku akan sulap menjadi poster bergambar agar mudah dimengerti!")

# Input Kamera
img_file = st.camera_input("Ambil foto soal")

if img_file is not None:
    original_image = Image.open(img_file)
    # st.image(original_image, caption="Foto Soalmu", width=300)
    
    try:
        math_text = extract_math_from_image(original_image)
        
        if not math_text:
            st.warning("Hmm, aku tidak menemukan soal matematika di foto itu. Coba foto lebih jelas ya!")
        else:
            st.info(f"Soal yang terbaca: **{math_text}**")
            
            poster_image = generate_dyscalculia_poster(math_text)
            
            st.success("Poster berhasil dibuat! 🎉")
            st.image(poster_image, caption=f"Visualisasi untuk: {math_text}", use_column_width=True)
            
            st.markdown("---")
            st.caption("Tips: Jika hasilnya aneh, coba ambil foto soal lagi dengan pencahayaan yang lebih baik.")

    except Exception as e:
        st.error("Waduh, ada masalah teknis saat membuat poster.")
        with st.expander("Lihat detail error (untuk developer)"):
            st.write(e)
            st.write("Kemungkinan model image generation sedang sibuk atau mencapai batas kuota.")