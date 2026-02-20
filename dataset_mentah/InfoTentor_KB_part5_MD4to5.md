---
id_materi: MD-004
mata_kuliah: "Matematika Diskrit"
topik: "Relasi dan Fungsi"
sub_topik: "Relasi dan Fungsi (Sifat Refleksif/Simetris, Injektif/Surjektif)"
tingkat_kesulitan: "Menengah"
prasyarat: ["Himpunan"]
---

# Relasi dan Fungsi (Sifat Refleksif/Simetris, Injektif/Surjektif)

**Ringkasan Materi (TL;DR)**
Relasi adalah himpunan aturan pemasangan anggota komputasional antar dua set data/domain. Fungsi divalidasi sebagai relasi "Spesial", di mana setiap subjek dari Domain himpunan asal mutlak dituntut mencentang mengeksekusi pemasangan HANYA SATU kali tepat presisi menuju destinasi Kodomain. 

**Konsep Sifat Relasional**
Apabila relasi entitas $R$ diujikan berputar menaungi Himpunan internal $A$:
1. **Refleksif (Reflexive)**: Segenap anggota wajib merujuk dirinya mandiri ($a,a \in R$, untuk semua elemen mutlak $a \in A$).
2. **Simetris (Symmetric)**: Kalau $a$ relasi mengeksekusi $b$, mutlak berlaku rute bolak-balik $b$ mengeksekusi $a$ ($a,b \in R \Rightarrow b,a \in R$).
3. **Transitif (Transitive)**: Hukum jembatan rantai. $(a,b \in R \land b,c \in R) \Rightarrow a,c \in R$.
*(Kumpulan relasi yang merangkul utuh menyabet ketiga pilar sifat di atas dinobatkan mutlak sebagai **Equivalence Relation / Relasi Ekuivalen**).*

**Konsep / Klasifikasi Pemetaan Fungsi**
Fungsi $f: A \rightarrow B$ memiliki batasan fungsional utilitas spesifik:
1. **Injektif (Satu-Satu / One-to-One)**: Target entitas output B tidak ditoleransi mendapati dua atau ganda suplai input A berbeda yang memasukinya. ($f(a) = f(b) \Rightarrow a = b$).
2. **Surjektif (Pada / Onto)**: Seluruh barisan pangkalan Kodomain (B) ludes tak bersisa menerima tembakan panah Input asal Domain A. Set Range Fungsi $f$ komputasional murni memeluk utuh sama kapasitasnya dengan Set entitas Kodomain B.
3. **Bijektif (Korespondensi Satu-Satu)**: Fungsi superior divalidasi merangkul tuntas sifat pilar Injektif dikombinasikan secara simetris bersama Surjektif. Konsekuensinya mutlak melahirkan fungsi sakti **Invers** (Fungsi balikan $f^{-1}$).

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Simak himpunan batas relasi komputator database entitas persahabatan di jejaring sosmed *Facebook*. Jika relasi didefinisikan $S(a,b) =$ "Akun A Berteman mem-follow relasi dengan Akun B". Evaluasi dan bedah sifat-sifat relasional (Refleksif, Simetris, Transitif) murni di tata ruang *Follower Facebook*!
**A1**: 
- **Bukan Refleksif (Irreflexive)**: Individu tidak dibenarkan dirancang meng-klik *Add Friend* berteman kepada profil dirinya sendiri di platform.
- **Simetris Murni**: Kalau "A berteman dengan B", mekanisme arsitektur platform *Facebook* otomatis memaksa tivalidasi dua-arah rimpang silang "B mutlak berteman kembali persis dengan A".
- **Bukan Transitif**: Kalau "Budi berteman dengan Andi" dan "Andi berteman dengan CEO Mark", tidak menggaransi memastikan statusnya "Budi serta-merta berteman dengan CEO Mark". Mereka baru berstatus perlintasan *Mutual Friends*.

**Q2**: Apabila terdapat rancangan program metode *Hashing Encryption Data*, arsitektur utilitas pemetaan *Fungsi Hash ID* ini harus direkayasa berstatus wajib mengakar sifat fungsional Injektif atau Surjektif? Paparkan konsekuensi rasional jika menyalahi!
**A2**: Fungsi *Hash* sangat krusial diwajibkan menjunjung patokan fungsional utilitas sifat fundamental **Injektif (Satu ke Satu)**. Karena memori *Hashing* mengkonversi deretan file mentah (A) yang sangat beragam ukurannya kepada output batas seragam terenkripsi *Hash Signature* (B). Jika ia menyalahi aturan alias terganjal sifat input ganda menabrak ke satu rentetan karakter Hash ID muara yang sama (Tidak Injektif), skenario ini memecah validasi sekuriti program meletupkan tabrakan data ganda yang populer dicap *Hash Collision Bug*.

---

---
id_materi: MD-005
mata_kuliah: "Matematika Diskrit"
topik: "Kombinatorial"
sub_topik: "Kombinatorial Dasar: Permutasi dan Kombinasi"
tingkat_kesulitan: "Menengah"
prasyarat: ["Faktorial Dasar"]
---

# Kombinatorial Dasar: Permutasi dan Kombinasi

**Ringkasan Materi (TL;DR)**
Kombinatorial menyediakan pilar perhitungan diskret perihal mencacah menghitung jumlah skenario permutasi komputasi yang mungkin terjadi di dalam menyusun rentetan koleksi obyek rasion. **Permutasi** mengeksploitasi kepatuhan tata letak formasi *Posisi Urutan* (Order Matters), sedangan **Kombinasi** digunakan menghimpun seleksi acak tanpa mempedulikan hierarki posisi indeks urutan *Unordered* (Order Doesn't Matter).

**Konsep / Cara Kerja / Formulasi Aksiomatis**
Utilitas fungsi berbasis arimetika limit n (kandidat semesta populasi) dan parameter mutlak r (jumlah entri slot obyek ditarik/dipilih). Digodok memakai komponen arsitektur Faktorial ($n! = n \times (n-1) \times \dots 1$).

1. **Permutasi ($P$ / $^n P_r$)**: 
Memilih dan mendudukkan komputasi posisi yang peka terhadap tatanan index struktur (Contoh: PIN Password $123$ berbeda kordinat relasional dengan Password $321$).
$$ P(n, r) = \frac{n!}{(n - r)!} $$
2. **Kombinasi ($C$ / $^n C_r$ / $\binom{n}{r}$)**:
Membentuk formasi panitia ganda batas acak dari populasinya tanpa jabatan sekat hierarki orientasi rasion (Contoh: Menarik bola {Merah, Biru} dinilai kongruen eksak sama setara mutlak diidentikan wujud komputator murninya bersama {Biru, Merah}).
$$ C(n, r) = \frac{n!}{r! \cdot (n - r)!} $$
Kombinasi acapkali dimanifestasikan algoritma koefisien *The Binomial Theorem* (Piramida segitiga Pascal).

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Dari ranah sekumpulan limit basis data berisi $10$ nama Pelamar pendaftar posisi *Staff Data Engineer*. Departemen HRD akan menyaring dan menghire 3 individu unggul menempati posisi setara rata menduduki stasiun kursi *Analis Rekrutmen Junior* seragam tanpa pembedaan grade kepangkatan. Formulasi apakah yang paling presisi di aplikasikan memecah perhitunganya?
**A1**: Dihitung mematuhi pakem utilitas **Kombinasi ($C$)**. Karena penempatan pos kursinya seragam rata tak membeda memposisikan gelar posisi jabatan (Status terambil "Andi, Budi, Susi" divalidasi presis rasion identik murni ekuivalens sejajar utilitas himpunan kordinasinya dengan "Susi, Andi, Budi").
Formula: $C(10, 3) = \frac{10!}{3! \times 7!} = \frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1} = \mathbf{120}$ kemungkinan format pembentukan tim seleksi.

**Q2**: Jika instruksional pergerakan utilasi fungsi Enkripsi *Brute Force* dipaksa diperintahkan membongkar kata Sandi gembok komputasional batas rentangan limit kombinasi $4$ digit nomer biner kordinat posisi *Password* unik yang ditarik dari perbendaharaan himpunan semesta angka dari parameter batasan himpunan susunan $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$ di mana karakter yang diinputnya mustahil boleh di iterasi berulang beruntun, berapakah mutlak hitungan siklus batas iteratif beban limit asimtot CPU yang ditanggung skenario mentok terjauh *Worst-case* algoritma brute force ini?
**A2**: Sandi *Password PIN* sensitip mematok ketegasan perihal **urutan/Order murni**. Susunan angka sandi [1 2 3 4] dievaluasi tidak kompatibel identik silang komparasinya menumbuk pasword [4 3 2 1]. Skenario algoritma menggunakan komputator referensi resolusi murni **Permutasi ($P$)**.
Ada populasi angka mentah $n = 10$ digit. Diposiasikan masuk rimpang mutlak $r = 4$ slot *Password*.
$P(10, 4) = \frac{10!}{(10-4)!} = \frac{10!}{6!} = \mathbf{10 \times 9 \times 8 \times 7 = 5.040}$ batas percobaan komputasi sandi murni iteratif mentah. 

---
