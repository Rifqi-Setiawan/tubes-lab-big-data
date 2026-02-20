---
id_materi: MD-006
mata_kuliah: Matematika Diskrit
topik: Prinsip Berhitung
sub_topik: Pigeonhole Principle (Prinsip Sarang Merpati)
tingkat_kesulitan: Menengah
prasyarat: Dasar Himpunan dan Fungsi
---

# Pigeonhole Principle (Prinsip Sarang Merpati)

**Ringkasan Materi (TL;DR)**
*Pigeonhole Principle* (Prinsip Sarang Merpati) menyatakan bahwa jika $n$ proyektil (merpati) dimasukkan ke dalam $m$ kotak (sarang) dan $n > m$, maka pasti setidaknya satu sarang memuat minimal dua merpati. Prinsip sederhana ini sering digunakan di Ilmu Komputer untuk membuktikan kemustahilan (*lossless compression*) atau mendesain penyelesaian tabrakan hash (*hash collisions*).

**Konsep / Cara Kerja / Kompleksitas**
Misalkan fungsi $f: A \rightarrow B$. Jika $|A| > |B|$, maka fungsi $f$ tidak mungkin bersifat injektif (satu-satu). 
Versi yang diperumum (Generalized): Jika $n$ objek ditempatkan ke dalam $m$ kotak, maka setidaknya satu kotak memuat $\lceil n/m \rceil$ objek.

**Contoh di Informatika:**
1. **Hash Table**: Bila terdapat $n$ buah input data yang dimasukkan ke fungsi *Hash* dan dipetakan ke *array* ukuran $m$, jika $n > m$, pasti terjadi *Collision* (tabrakan nilai *hash*). 
2. **Kriptografi**: Membuktikan ada dua pesan asli yang menghasilkan *ciphertext/hash* yang sama jika panjang *hash* lebih kecil dari panjang pesan.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Di laci gelap terdapat 10 pasang kaos kaki hitam dan 10 pasang kaos kaki putih yang terurai acak. Berapa minimal kaos kaki yang harus diambil agar dijamin mendapat sekurang-kurangnya sebuah pasang warna seragam?
**A1**: Jawaban yang benar adalah **3 buah**. 
*Pembahasan*: Sarang ($m$) = 2 (Hitam, Putih). Merpati ($n$) = jumlah pengambilan. 
Skenario ekstrem (2 pengambilan pertama): satu Hitam, satu Putih. Pengambilan ketiga pasti akan jatuh di Hitam atau Putih, menggenapkan salah satu pasangan (karena $3 > 2$).

**Q2**: Sebuah angkatan mahasiswa Informatika berjumlah 370 orang. Buktikan ada minimal 2 mahasiswa yang tanggal dan bulan lahirnya sama persis!
**A2**: 
*Pembahasan*: Merpati ($n$) = 370 mahasiswa. Sarang ($m$) = total hari setahun (maksimal 366 hari saat kabisat). Penuhi nilai *Generalized*: $\lceil n/m \rceil = \lceil 370 / 366 \rceil = \lceil 1.01 \rceil = 2$.
Artinya, minimal dijamin akan ada hari ulang tahun yang sama jatuh untuk sekurang-kurangnya 2 orang mahasiswa secara valid.

---

---
id_materi: MD-007
mata_kuliah: Matematika Diskrit
topik: Teori Graf
sub_topik: Graf Planar dan Pewarnaan Graf (Graph Coloring)
tingkat_kesulitan: Tinggi
prasyarat: Graf Dasar (Vertex & Edges)
---

# Graf Planar dan Pewarnaan Graf (Graph Coloring)

**Ringkasan Materi (TL;DR)**
Graf *Planar* bisa digambar lurus di dimensi ganda bidang tanpa ada titik memotong bersilangan (*edge crossings*). Di sistem komputasi (kompiler, PCB circuit, network node), penataan titik (*Vertex Coloring*) mewajibkan pewarnaan simpul supaya tidak ada dua simpul bertetangga yang bertepatan senada dengan presisi jumlah *Chromatic Number* mininal ($\chi$). 

**Konsep / Sifat Graf Planar**
- **Teorema Euler**: Apabila $G$ adalah graf planar terhubung direpresentasikan $V$ (titik/vertex), $E$ (sisi/edge), dan membagi area potong dimensi tertutup $F$ (*faces*), berlaku:
$$ V - E + F = 2 $$
- **Kuratowski's Theorem**: Sebuah graf dinilai terkurung di sistem non-planar jika dan hanya jika memuat graf isomorfis dengan partisi utilitas $K_5$ atau $K_{3,3}$.
- Algoritma Dasar perwarnaan umum adalah *Greedy Coloring*, yang di dunia aslinya bersifat NP-Hard untuk mencari optimal $\chi$ (waktu eksponensial).

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Enam buah kelas akan melaksanakan ujian komprehensif. (A&B), (C&D), (A&D), (B&E), (E&F) masing² memiliki mahasiswa irisan sehingga tidak boleh ujian bersama waktu/jam. Tentukan total memori batas jadwal ujian ($\chi$) yang termurah presisi!
**A1**: *Pembahasan*: 
Gambarkan graf kelas. Titik = Kelas (A,B,C,D,E,F). Ada 5 irisan Edge: (A-B), (C-D), (A-D), (B-E), (E-F). 
Titik A warna 1. Titik B, D tetangga, beri warna 2. Titik C, E tetangga B/D beri warna 1. Titik F bisa warna 2. 
Semua terhindar bentrok, hanya memakasi eksak 2 warna ($\chi = 2$). Jadwal termurah hanya perlu 2 slot jam terpisah.

**Q2**: Jika sebuah rangkaian *Printed Circuit Board* (PCB) jaringan Planar mendeskripsikan sirkuit topologi terhubung memuat 11 sambungan Edge dan menyekat luas area 5 teritori Face, Berapa presisi banyak Vertices ($V$/Komponen IC) nya?
**A2**: Karena jaringan dikunci sirkuit Euler: $V - E + F = 2$.
Diketahui batas $E=11$ dan limit area teritorial $F=5$.
$V - 11 + 5 = 2 \implies V - 6 = 2 \implies V = 8$. Dipastikan PCB tersebut memiliki keping titik berjumlah 8 sumbu.

---

---
id_materi: MD-008
mata_kuliah: Matematika Diskrit
topik: Teori Graf Pohon (Tree)
sub_topik: Minimum Spanning Tree (Algoritma Kruskal & Prim)
tingkat_kesulitan: Tinggi
prasyarat: Pohon (Tree) & Graf Berbobot
---

# Minimum Spanning Tree (Algoritma Kruskal & Prim)

**Ringkasan Materi (TL;DR)**
Dalam bentangan graf utilitas *Weighted* (bobot nominal nilai kabel/jarak), *Minimum Spanning Tree (MST)* mendeskripsikan sub-pohon rute asimtot termurah yang mutlak merangkul selasar titik tanpa siklus melingkar putus buntu sama sekali (*Cycle-free*). Kruskal (Sortir E) dan Prim (Sortir V) menyelesaikan optimisasi greedy pembatas komputasi MST ini secara presisi presisi komputator sekuennya $O(E \log V)$.

**Konsep / Cara Kerja**
- **Algoritme Kruskal (*Edge-centric*)**: 
1. Ekstrak keluar sisi/edge array dan sortir urut naik. $\mathcal{O}(E \log E)$
2. Iterasi per edge, jika menggabungkan sisi iterasi array tersebut tidak meretas melanggar deteksi rute melingkar *(Cycle / teratasi pakai Disjoint Set Union)*, satukan pada Pohon. Berhenti di V-1 tepian.
- **Algoritme Prim (*Vertex-centric*)**:
1. Pilih simpul stasiun acak (Vertex array).
2. Dari area batas yang sudah dicaplok MST, terabas lari ke tetangga terdekat pinggiran pinggir sekat Vertex yang belum terkoneksi via muatan *Priority Queue* (Min-Heap).
3. Merapat merangkul rute *bobot lokal terkecil* sekuensial tuntas terpanen seluruh V. $\mathcal{O}(E \log V)$.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Karena parameter kompleksibilitas *Best-Case* Prim terbukti optimal membelah di $O(|E| + |V| \log |V|)$ jikalau menumpang tataan parameter memori *Fibonacci Heap*, di graf penampang kepadatan tarian macam apakah Prim mutlak unjuk gigi mengkudeta Kruskal?
**A1**: **Dense Graph** (Graf bersikuat tumpukan serempak/padat persimpangan rute $E \approx V^2$). Jika Kruskal dideretkan mutlak mensortir rel $E$, ia bakal kelimpungan menduduki $\mathcal{O}(V^2 \log V)$. Sementara utilitas pergeseran *Vertex* di min-heap miliknya Prim tidak menanggung memori masif penyortasian raksasa di ruang memori komputator komparasi awal.

**Q2**: Apabila rancangan menara telkom memiliki rute ganda bernominal beban biaya terpotret SAMA (Contoh rute A=B=10), mungkinkah solusi luaran desain lintasan kabel hasil Prim dan Kruskal menghasilkan rute pohon *yang berbeda secara fisik gambarnya*? Apakah itu melanggar ketentuan Algoritma MST?
**A2**: Rute jalurnya bisa saja terpoting **berbeda**, tetapi total jumlah biaya kalkulasi minimal beban *cost limit* MST dipastikan tetap identik **SAMA** seratus persen. Muncul *Multiple Valid Minimum Spanning Trees* di graf yang berbobot tidak unik. Ini sah dan tervalidasi serta tidak merongrong cacat resolusi logik dari parameter MST.

---

---
id_materi: MD-009
mata_kuliah: Matematika Diskrit
topik: Analisis Algoritma
sub_topik: Kompleksitas Algoritma Asimtotik (Big-O, Big-Omega, Big-Theta)
tingkat_kesulitan: Menengah
prasyarat: Fungsi Pertumbuhan Eksponensial Logaritma
---

# Kompleksitas Algoritma Asimtotik (Big-O, Big-Omega, Big-Theta)

**Ringkasan Materi (TL;DR)**
Ketika basis pasokan variabel array parameter algoritma membesarkan volume skala hingga parameter tak terbatas $n \to \infty$, durasi *Running Time* merambat curam dipetakan dalam asimtot. 
$\mathcal{O}$ (*Big-O*): Skenario atap pelindung *Worst-case*.
$\Omega$ (*Big-Omega*): Skenario lantai rute tercepat *Best-case*.
$\Theta$ (*Big-Theta*): Tingkatan cengkraman penguji presisi kongruen perpaduan apit ketat keduanya (Asimtot *Average/Tight bounds*).

**Konsep / Cara Kerja / Pseudocode Kompleksitas**
Sebuah fungsi eksak $T(n) = 3n^2 + n \log n + 10$:
Parameter Big-O hanya menyoroti rasio koefisien pemangkas pembengkakan terekstrem $n^2$ dan memangkas menyingkirkan iringan elemen sisanya sehingga komputasi asimtot atas absolut termutasi = $\mathcal{O}(n^2)$.
- $\mathcal{O}(1)$ (Konstan): Cek nilai pertama.
- $\mathcal{O}(\log n)$ (Logaritmik): Binary Search.
- $\mathcal{O}(n)$ (Linier): Linear Search iterasi `for`.
- $\mathcal{O}(n^2)$ (Kuadratik): Loop bersarang (Bubble Sort).
- $\mathcal{O}(2^n)$ (Eksponensial): Rekursi tanpa memorisasi, Fibonacci klasik.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Simak sekuen iteratif Nested-Looping di kode ini:
```python
i = 1 
while i < n:
    for j in range(n):
        print(i, j)
    i = i * 2
```
Tentukan nilai Asimtotik Big-O tereksekusinya array blok utuhnya secara komputasi analitik!
**A1**: **$\mathcal{O}(n \log n)$**
*Pembahasan*: Batasan deret pengitar *while-loop luar* (berbasis pelompat skala $i=i \times 2$) akan meledak meroket hingga atap $n$ dalam kelipatan langkah kuadrat multiplikasi basis-2 $\implies \log n$ siklus iterasi batas waktu. Batasan deret kompres *for-loop dalam* merambat sekuensial linear linier perbatasan absolut satu-langkah iteratif utuh $\implies n$. Karena dikonfigurasi menumpuk *nested* mutlak di-multipilin kalikan, hasil mutlak limit $= \mathcal{O}(n \log n)$.

**Q2**: Apabila utilitas komputator mesin telusur Array "Linear Search" dicatat menggondol nilai minimum dasar kecepatan batas rentang lantai eksekusi di asimtot *Big-Omega* $\Omega(1)$, sebutkan di iklim situasi skenario macam apakah hal itu terwujud?
**A2**: Saat variabel angka sasaran tembak buruan referensi mutlak tepat bertengger mengisi lokator perbatasan nilai komputasi *sel index ter-awal pelopor nol pertama (* `[0]` *)*. Eksekusi program pengecekan akan bergelimpang menghentikan operasi melibas siklus seleher hanya dipaksa bermodal mengeksekusi instruksi perbandingan satu langkah waktu statis semata. 

---

---
id_materi: MD-010
mata_kuliah: Matematika Diskrit
topik: Relasi dan Fungsi
sub_topik: Representasi Relasi dengan Matriks
tingkat_kesulitan: Dasar
prasyarat: Dasar Matriks Logis dan Himpunan Kordinasi
---

# Representasi Relasi dengan Matriks

**Ringkasan Materi (TL;DR)**
Entitas interkonektivitas struktural titik komponen dua relung ruang himpunan (Misal relasi tatanan ruang A dengan ruang destinasi tujuan logis B) paling presisi digodok dalam sistem komputer pemrograman dikonversikan merepresentasikan diri via tata letak jajaran **Matriks Boolean Nol-Satu** bersumbu bujur-lintang Cartesian $M_R = [m_{ij}]$.

**Konsep Ruang Matriks Boolean Transposisi**
Penomoran presisi entitas nilai array diringkas dari letak sumber elemen indeks pergerakannya kompotasi ($i$: baris sumber di himpunan asal referensi, dan $j$: lokator posisi kolom ruang himpunan referensi objek tujun iterasi):
- Jika dipetakan persambungan utilitas referensialnya eksak terkait merapat $(a_i, b_j) \in R$, relasinya diklaim sah dan dinampakkan terekam di sel blok persilangan rasion $(i,j)$ sebagai angka murni Biner "**1**".
- Jika ikatan rasion presisi itu dibatalkan/lepas tidak hadir $(a_i, b_j) \notin R$, diisi biner kordinat hampa "**0**".

**Pengukuran Sifat Pola $(A = B$ Domain persegi $M_{n \times n})$:**
1. **Refleksif**: Presisi seluruh parameter kordinat balok sel persimpangan dari *Garis pemutus rute horizontal/diagonal membelah pusat ($m_{11}, m_{22}, m_{33}$, dll)* mutlak diisi barisan padat Biner 1.
2. **Simetris**: Keseimbangan rasio nilai matrik cermin putar rotasi Transpose bersumbu sama konstan asimtot presisinya identik ($M_R = M_R^T$ dan rasio letak $m_{ij} = m_{ji}$).

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Dari ranah set kordinasi himpunan asal A = {X, Y}. Terpantau dikompres terhubung fungsi pemisalan Relasi $R = \{(X,X), (Y,X)\}$. Buatlah konstruksi visualisasinya di matrik!
**A1**: Relasi asimetri berhimpun di batasan kuadrat matrix ruang $2 \times 2$. Sumbu batas kordinasinya (baris mewakili perolehan X dan Y, pun demikian kolom sumbu tujuanya X dan Y). Nilainya dipasok dari relasi kordinasi referensinya.
Hasil matrix:
$$
\begin{bmatrix}
1 & 0 \\
1 & 0 
\end{bmatrix}
$$

**Q2**: Apabila kalian mendapat lembar print-kertas kode biner referensi Matriks dari suatu susunan data utilasi relasional referensi mesin pencari index, Namun ditemukan keganjilan absolut di sel pembelah diagonal kordinasi utamanya dipatok mutlak merapat disusupi rentetan nol murni panjang 0, nilai properti utuh fundamental utilitias asimetri apa yang seketika disimpulkan batal di perumusan tersebut? 
**A2**: Sistem susunan ikatan dipastikan gagal presisi gugur dari parameter sifat properti **Refleksif**. Karakter parameter dari sifat kordinasi ikatan Refleksif menaruh syarak esensial tak terbantahkan absolut: Semua tatanan himpunan sel *ruang relung diri objek yang melirik objek dirinyanya presisinya (loop ikatan ke diri kembali)* seperti $(a,a), (b,b)$ mesti merantai berisikan angka mutakhir konfirmasi bit presisi 1. Kosongnya deret persilangan sentral membanting putus mutlak kepatuhan absolut persyaratannya batal tak bisa dibela komputasi.
---
