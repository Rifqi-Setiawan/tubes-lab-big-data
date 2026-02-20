---
id_materi: LM-006
mata_kuliah: Logika Matematika
topik: Argumen dan Validitas Pembuktian
sub_topik: Modus Tollens lanjutan, Fallacy
tingkat_kesulitan: Menengah
prasyarat: Logika Proposisi Dasar
---

# Argumen dan Validitas Pembuktian (Modus Tollens Lanjutan, Fallacy)

**Ringkasan Materi (TL;DR)**
Sebuah argumen valid jika mustahil premis bernilai benar namun kesimpulannya salah. Modus Tollens lanjutan memungkinkan penarikan kesimpulan dari premis implikasi yang kompleks. *Fallacy* (kesesatan formal) adalah argumen yang polanya menyerupai inferensi valid namun cacat secara logika (contoh: *Affirming the Consequent*, *Denying the Antecedent*).

**Konsep dan Cara Kerja**
- **Modus Tollens Lanjutan**: 
  Jika diberikan $(A \lor B) \rightarrow C$ dan diketahui $\neg C$, maka kesimpulannya adalah $\neg(A \lor B)$, yang setara dengan $\neg A \land \neg B$ (De Morgan).
- **Fallacy (Kesesatan Berpikir)**:
  1. *Affirming the Consequent* (Pembalikan): $p \rightarrow q, q \vdash p$. Membenarkan akibat tidak menjamin sebabnya.
  2. *Denying the Antecedent* (Penolakan): $p \rightarrow q, \neg p \vdash \neg q$. Menolak sebab tidak menjamin akibatnya tidak terjadi (karena bisa ada sebab lain).

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Analisislah argumen berikut: "Jika API error, maka aplikasi crash. Aplikasi crash, berarti API error." Apakah argumen ini valid?
**A1**: Tidak valid. Argumen ini mengandung *fallacy Affirming the Consequent*. Aplikasi crash (akibat) bisa saja disebabkan oleh memori bocor (Out of Memory) atau hal lain, bukan hanya karena API error.

**Q2**: Diberikan premis: (1) $(P \land Q) \rightarrow R$. (2) $\neg R$. Tentukan kesimpulan valid menggunakan Modus Tollens!
**A2**: Dari $X \rightarrow Y$ dan $\neg Y$, kita peroleh $\neg X$. Maka kesimpulannya adalah $\neg (P \land Q)$. Berdasarkan Hukum De Morgan, ekspresi ini setara dengan $\neg P \lor \neg Q$.

---

---
id_materi: LM-007
mata_kuliah: Logika Matematika
topik: Resolusi Logika
sub_topik: Resolusi dalam Proposisi
tingkat_kesulitan: Tinggi
prasyarat: Bentuk Normal Konjungtif (CNF)
---

# Resolusi Logika dalam Proposisi

**Ringkasan Materi (TL;DR)**
Resolusi adalah kaidah inferensi kuat yang menjadi dasar *automated theorem proving* (seperti Prolog). Aturan ini menggabungkan dua klausa yang mengandung literal kontradiktif (positif dan negatif) untuk menghasilkan klausa baru (resolvent). Semua kalimat harus dikonversi ke Conjunctive Normal Form (CNF) terlebih dahulu.

**Konsep / Cara Kerja / Kompleksitas**
Aturan Resolusi Dasar:
$$ \frac{p \lor q \quad, \quad \neg p \lor r}{\therefore q \lor r} $$
Dalam pemrograman cerdas, digunakan teknik **Resolusi Refutasi (Pembuktian dengan Kontradiksi)**:
1. Ubah semua premis ke CNF.
2. Negasikan kesimpulan yang ingin dibuktikan, dan ubah ke CNF.
3. Tambahkan negasi kesimpulan tersebut ke himpunan premis.
4. Lakukan pencoretan (resolusi) antar klausa. 
5. Jika menghasilkan *klausa kosong* (kontradiksi), maka negasi kesimpulan salah, sehingga kesimpulan asli bernilai **valid**.

*Kompleksitas*: Algoritma ini memiliki *worst-class time complexity* eksponensial $O(2^n)$ karena termasuk NP-Complete.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Diberikan dua klausa: $K_1 = A \lor \neg B \lor C$ dan $K_2 = B \lor D$. Susunlah *resolvent* (hasil resolusinya)!
**A1**: Kita memiliki literal kontradiktif yaitu $\neg B$ di $K_1$ dan $B$ di $K_2$. Kita dapat meresolusinya (mencoret keduanya). Hasil *resolvent*-nya adalah penggabungan sisa literal: $A \lor C \lor D$.

**Q2**: Jelaskan mengapa Resolusi Refutasi menggunakan prinsip kontradiksi daripada membuktikan konklusi secara langsung?
**A2**: Mencari *truth assignment* lengkap sering kali lebih memakan resource (harus cek 2^n baris tabel kebenaran). Dengan menambahkan negasi konklusi, kita hanya perlu mencari sepasang klausa yang bertentangan (menghimpun klausa kosong). Jika ditemukan satupun jalur menuju klausa kosong, pembuktian selesai dengan bukti valid.

---

---
id_materi: LM-008
mata_kuliah: Logika Matematika
topik: Logika Predikat
sub_topik: Variabel Bebas dan Terikat
tingkat_kesulitan: Menengah
prasyarat: Kuantifier Universal dan Eksistensial
---

# Logika Predikat: Variabel Bebas dan Terikat

**Ringkasan Materi (TL;DR)**
Dalam Logika Predikat, setiap kuantifier memiliki jangkauan yang disebut *scope*. Variabel dikatakan **Terikat (Bound)** jika berada dalam ruang lingkup sebuah kuantifier. Variabel disebut **Bebas (Free)** jika ia tidak terikat oleh kuantifier manapun. Sebuah kalimat terbuka hanya dapat dinilai kebenarannya jika tidak memiliki variabel bebas.

**Konsep / Cara Kerja**
- Diberikan ekspresi: $\forall x (P(x, y))$
  - $x$ adalah **variabel terikat** karena diikat oleh kuantifier $\forall$.
  - $y$ adalah **variabel bebas** karena tidak ada kuantifier predikat $\forall y$ atau $\exists y$.

**Pseudocode Visualisasi Scope**:
Seperti pembatasan parameter di bahasa pemrograman:
```python
y = 10 # y adalah variabel "Bebas" (Global)

def periksa(x): # x adalah variabel "Terikat" (diikat parameter fungsi)
    return x > y 
```
Jika kita tidak mensubstitusi variabel bebas $y$ dengan konstan, maka ekspresi tidak memiliki nilai kebenaran tetap.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Tentukan variabel bebas dan terikat pada: $\exists x (P(x, y)) \land Q(x)$.
**A1**: 
- $x$ pada $P(x,y)$: Terikat (oleh $\exists x$).
- $y$ pada $P(x,y)$: Bebas (tidak ada kuantifier).
- $x$ pada $Q(x)$: Bebas! Kuantifier $\exists x$ hanya melingkupi $P(x, y)$ di dalam kurungnya.

**Q2**: Mengapa sebuah fungsi preposisi dengan variabel bebas tidak boleh langsung disimpulkan bernilai *True* atau *False*?
**A2**: Karena variabel bebas merepresentasikan argumen yang nilainya belum terdefinisi. Sama seperti fungsi `f(x) = x > 5`. Kita tidak bisa mengatakan *statement* itu benar atau salah sebelum kita memasukkan angka konkrit ke dalam variabel `x`.

---

---
id_materi: LM-009
mata_kuliah: Logika Matematika
topik: Rangkaian Kombinasional
sub_topik: Half Adder & Full Adder
tingkat_kesulitan: Menengah
prasyarat: Gerbang Logika, Aljabar Boolean
---

# Rangkaian Kombinasional (Half Adder & Full Adder)

**Ringkasan Materi (TL;DR)**
Sirkuit penjumlah adalah jantung dari komponen ALU di prosesor. *Half Adder* menjumlahkan 2 bit dasar tanpa carry-in. *Full Adder* bisa memperluas ini dengan kemampuan menjumlahkan 3 bit (termasuk *Carry In* sisa dari penjumlahan register digit sebelumnya). Output keduanya terdiri atas digit bilangan (Sum) dan sisa (Carry Out).

**Konsep / Cara Kerja**
**1. Half Adder**:
Menerima $A$ dan $B$.
$$ Sum = A \oplus B $$
$$ C_{out} = A \cdot B $$

**2. Full Adder**:
Menerima $A$, $B$, dan $C_{in}$.
$$ Sum = A \oplus B \oplus C_{in} $$
$$ C_{out} = (A \cdot B) + (C_{in} \cdot (A \oplus B)) $$
$Full Adder$ dapat dibentuk menggunakan 2 buah gerbang Half Adder yang dirangkai bertahap, lalu hasil carry-nya digabungkan menggunakan gerbang OR.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Rancang bagaimana menyusun unit aritmetika 2 bit menggunakan unit Adder!
**A1**: Kita perlu menyusun $A_1A_0 + B_1B_0$. 
Untuk LSB (Bit paling tidak signifikan, $A_0$ dan $B_0$), kita gunakan **Half Adder** (karena tidak ada memori *carry prev*). Hasilnya adalah $S_0$ dan $C_0$.
Untuk $A_1$ dan $B_1$, kita gunakan **Full Adder**, dengan input ke-3 mengambil $C_0$ tadi. Keluaran menjadi $S_1$ dan $C_{final}$. Angka akhirnya adalah $C_{final} S_1 S_0$.

**Q2**: Apa kelemahan utama komputasi metode penyambungan Full Adder lurus berjejer (*Ripple Carry Adder*) jika digunakan di arsitektur CPU 64-bit modern?
**A2**: Peningkatan kelambatan jalur kritis (*propagation delay*). Rangkaian penjumlahan bit ke-63 harus diam pasif menunggu *Carry-out* bergelombang menyelesaikannya dari bit-0 hingga bit-62 ($O(n)$ delay waktu). Jika 1 gerbang = 1 ns, penjumlahan lambat 64 ns.

---

---
id_materi: LM-010
mata_kuliah: Logika Matematika
topik: Penyederhanaan Logika
sub_topik: Peta Karnaugh (K-Map) Dasar
tingkat_kesulitan: Dasar
prasyarat: Sum of Product (SOP)
---

# Penyederhanaan Logika dengan Peta Karnaugh (K-Map) Dasar

**Ringkasan Materi (TL;DR)**
Peta Karnaugh (K-Map) adalah diagram susun visual untuk menyederhanakan rumusan Aljabar Boolean. Tujuannya adalah mengeliminasi variabel redudan agar total gerbang hardware chip efisien. K-Map mengelompokkan area nilai 1 dengan bingkai simetris yang luas potongannya harus berukuran kuadrat perpangkatan angka dasar basis 2 (misal 1, 2, 4, 8 area).

**Konsep / Cara Kerja**
Metode untuk *Sum of Products* (SOP):
1. **Pemetaan Grid**: Buat tabel $2^n$ kotak. Label baris & kolom wajib mengikuti pergerakan **Gray Code** ($00, 01, 11, 10$). Tujuannya memastikan petak vertikal horizontal selang-selingnya selalu persis cuma berselisih 1 bit ubahan saja.
2. **Peletakan 1**: Masukkan biner $1$ di mana output fungsi bernilai *True*.
3. **Pengelompokan (Looping)**: Gambarlah kotak/wilayah keliling persegi/persegi-panjang yang menaungi deretan bilangan $1$ (menggulung pinggiran tabel tidak dilarang). Jumlah kotak dalam grup wajib $1, 2, 4,$ atau $8$.
4. **Penyederhanaan**: Pertahankan variabel yang konstan di *grouping* (1 atau 0 selalu), coret variabel yang berbalik/berubah fluktuasi indeksnya.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Fungsi 3 variabel $F(A,B,C) = \sum m(0, 1, 2, 3)$. Bagaimana rumusan paling sederhananya via K-Map?
**A1**: Minterm-minterm $000, 001, 010, 011$ berada pada 4 blok yang sepenuhnya mendominasi perbatasan baris ketika atribut nilai mutlak $A = 0$ (atau nilai $\overline{A}$). Atribut logikal $B$ dan $C$ semuanya melintasi variasi index polaritas ubah rentang kombinasi $0$ hingga $1$, sehingga dieliminasi secara paripurna. Ekstrak rumusan sederhananya hanya: $F = \overline{A}$.

**Q2**: Mungkinkah dalam Peta Karnaugh mengkurung kumpulan minterm seukuran **3 petak** 1? Apa dampaknya jika dipaksa secara Aljabar?
**A2**: Tidak boleh. Hukum aljabar reduksi Boolean $X \cdot Y + X \cdot \overline{Y} = X(Y+\overline{Y}) = X$ hanya bisa bekerja berpasangan yang mengeleminir selisih 1-bit, yang efek kelipatannya akan menjadi rasio pangkat-2 (kelompok 2, 4, 8). Jika grup 3 petak digabungkan, itu akan melawan kaidah faktorisasi karena akan ada term ekstra yang merusak kompensasi pembatalan suku.
---
