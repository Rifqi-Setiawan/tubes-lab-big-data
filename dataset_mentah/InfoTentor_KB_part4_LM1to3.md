---
id_materi: LM-001
mata_kuliah: "Logika Matematika"
topik: "Logika Proposisional"
sub_topik: "Logika Proposisional dan Tabel Kebenaran"
tingkat_kesulitan: "Dasar"
prasyarat: []
---

# Logika Proposisional dan Tabel Kebenaran

**Ringkasan Materi (TL;DR)**
Logika proposisional adalah fondasi analisis bernalar yang mengevaluasi kalimat deklaratif bernilai mutlak BENAR (True/1) atau SALAH (False/0). Tabel Kebenaran (Truth Table) adalah tabel kombinasi yang menjabarkan skenario absolut dari nilai operasional beberapa proposisi yang digabungkan.

**Konsep / Cara Kerja**
- Variabel dasar dilambangkan dengan huruf kecil ($p, q$).
Operasi Logika Utama:
1. **Negasi ($\neg p$ / NOT)**: Membalikkan nilai. Jika $p=1$ maka $\neg p=0$.
2. **Konjungsi ($p \land q$ / AND)**: Bernilai 1 HANYA JIKA $p=1$ dan $q=1$.
3. **Disjungsi ($p \lor q$ / OR)**: Bernilai 1 JIKA minimal salah satu bernilai 1.
4. **Implikasi ($p \rightarrow q$)**: Kaidah sebab-akibat. Bernilai 0 HANYA JIKA sebabnya benar ($p=1$) tetapi akibatnya salah ($q=0$).
5. **Biimplikasi ($p \leftrightarrow q$)**: Bernilai 1 JIKA nilai $p$ identik dengan $q$.

Kompleksitas Evaluasi:
Tabel kebenaran tumbuh secara **eksponensial basis 2**. Untuk $n$ variabel input, terdapat $2^n$ baris skenario yang harus dievaluasi. Algoritma komputasi pengecekan menyeluruh memiliki time complexity asimtot $\mathcal{O}(2^n)$.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Uraikan kenapa evaluasi pernyataan Implikasi ($p \rightarrow q$) mutlak dinilai BENAR (1) apabila nilai variabel sebab ($p$) sudah bernilai SALAH (0)?
**A1**: Dalam aksioma matematika, ini disebut *Vacuous Truth* (Kebenaran Kosong). Esensi implikasi hanya meminta pertanggungjawaban klaim jika syarat awal terpenuhi ($p=1$). Jika syarat awal tidak direalisasikan (False=0), argumen kondisional ini tidak pernah dilanggar, sehingga secara hierarki dianggap tervalidasi utuh (True=1). Contoh: "Jika 1+1=3, maka saya kaya". Karena sebabnya salah, seluruh pernyataan implikasi dianggap bernilai benar secara hampa.

**Q2**: Apabila anda diamanahkan membuat program brute-force Tabel Kebenaran yang menyatukan 20 variabel proposisi atomik, mengapa program ini diprediksi sangat lelet dan merusak rasio memori komputator?
**A2**: Evaluasi komputasi baris memori didasarkan pada formula eksponensial $2^n$. Jika kita menggunakan 20 variabel ($n=20$), tabel tersebut akan memiliki $2^{20} = 1.048.576$ baris. Kompleksitas asimtotiknya meroket di $\mathcal{O}(2^n)$ (suatu komputabilitas *intractable/NP-Hard* untuk nilai $n$ besar), memakan resouce waktu dan memori secara masif untuk menelusuri satu per satu tabel.

---

---
id_materi: LM-002
mata_kuliah: "Logika Matematika"
topik: "Inferensi Logika"
sub_topik: "Inferensi Logika (Modus Ponens, Tollens, Silogisme)"
tingkat_kesulitan: "Dasar"
prasyarat: ["Logika Proposisional"]
---

# Inferensi Logika: Modus Ponens, Tollens, Silogisme

**Ringkasan Materi (TL;DR)**
Inferensi (Deduksi) adalah struktur penalaran derivatif (penarikan kesimpulan) dari beberapa premis fakta mutlak menjadi sebuah konklusi tervalidasi (tautologi). Tiga fondasi primitif yang menjadi pilar komputasi mesin AI Rule-Based System adalah Modus Ponens (Maju), Modus Tollens (Mundur), dan Silogisme (Transisi Rantai). 

**Konsep / Cara Kerja Inferensi Deduktif**
- **Modus Ponens (Afirmasi Sebab / Forward Chaining)**:
Jika implikasi premis $p \rightarrow q$ divalidasi dan fakta $p$ dipastikan terjadi, maka konklusi $q$ pasti BENAR.
Notasi: $\frac{p \rightarrow q \quad, \quad p}{\therefore q}$

- **Modus Tollens (Penolakan Akibat / Backward Chaining)**:
Berlandas pada aturan ekuivalensi *Kontraposisi*. Jika $p \rightarrow q$ mutlak benar, dan realitasnya output akibat $q$ divalidasi GAGAL ($\neg q$), maka ditelusuri sebab tunggalnya tak dipenuhi alias $\neg p$.
Notasi: $\frac{p \rightarrow q \quad, \quad \neg q}{\therefore \neg p}$

- **Silogisme Hipotetis (Transitivitas Implikasi)**:
Penarikan rantai deduktif berantai.
Notasi: $\frac{p \rightarrow q \quad, \quad q \rightarrow r}{\therefore p \rightarrow r}$

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Simak alarm logika server komputasi ini: "Kalau sistem meraba pelonjakan Trafik Load Balancer, maka Alarm Notifikasi Trigger meradang. Sore ini Alarm MATI dan tak dipanggil sama sekali!". Turunkan simpulan valid dan sebutkan rujukannya!
**A1**: Simpulan argumen validnya: **Sistem saat ini tidak mendapati anomali pelonjakan Trafik**. Penarikan deduktif ini divalidasi via **Modus Tollens**. Fakta menolak output/akibat ("Alarm MATI" / $\neg q$), murni menghempaskan rumusan awal hipotesis antecedent dijamin batal ($\neg p$).

**Q2**: Apabila terdapat logika komputasi menyimpulkan: "Jika variabel array $x$ melebihi limit, lantas loop Error mencetak limit. Nyatanya loop Error mencetak limit. Kesimpulan: Variabel array $x$ pasti melebihi limit". Jelaskan cacat fatal arsitektur validasi statemen deduktif ini!
**A2**: Batasan struktur relasional penarikan simpulan deduktif tersebut murni **Tidak Valid/Invalid**. Hal ini dikategorikan membelot melakukan kesesatan kekeliruan bernalar *(Falasi Logika)* bertitel **Affirming the Consequent (Membenarkan sisi Akibat)**. Keruntuhan ini hadir lantaran akibat Loop Error ($q$ True) belum memvalidasi murni disebabkan eksak karena $X$ lebih limit ($p$ True); error sangat berpeluang diinisiasi kausalitas lain, contohnya RAM penuh *(Out of Memory)*.

---

---
id_materi: LM-003
mata_kuliah: "Logika Matematika"
topik: "Hukum Logika"
sub_topik: "Ekuivalensi Logis dan Hukum Logika (De Morgan, dll)"
tingkat_kesulitan: "Menengah"
prasyarat: ["Logika Proposisional"]
---

# Ekuivalensi Logis dan Hukum Logika

**Ringkasan Materi (TL;DR)**
Dua ekspresi rumusan algoritma divalidasi memeluk status identitas **Ekuivalen secara Logis** ($P \equiv Q$) bila mereka mutlak memproduksi skenario kolom output Tabel Kebenaran yang sejajar presisi kembar pada seluruh baris iterasinya. Hukum Aljabar Logika memperlancar programer menyederhanakan *spaghetti code* ekspresi Boolean menjadi instruksi ramping optimal di kompilator sistem.

**Konsep / Cara Kerja / Formulasi Aksiomatis**
- **Hukum Idempotent**: $p \lor p \equiv p$ , dan $p \land p \equiv p$
- **Hukum Komutatif & Asosiatif**: Pertukaran orientasi parameter $(p \lor q \equiv q \lor p)$
- **Hukum Distributif**: Mirip faktorisasi aljabar matematika dasar. $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$
- **Hukum De Morgan (Trik Reversi Komplemen Inversi):**
Kaidah ini merombak batas negasi yang bersembunyi membayangi sarang kurung:
$$ \neg (p \land q) \equiv \neg p \lor \neg q $$
$$ \neg (p \lor q) \equiv \neg p \land \neg q $$
- **Hukum Resolusi Implikasi Dasar (Hukum Material):**
Batas fundamental mengubah anak panah implikasi diganti ke sirkuit relasi murni dasar OR / NOT.
$$ p \rightarrow q \equiv \neg p \lor q $$

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Optimasi rentetan sintaks program bahasa C: `if (! (koneksi_aktif && latensi_rendah))`. Uraikan konversinya dengan mereferensikan hukum logika aksiomatis De Morgan!
**A1**: Notasi operator negasi (`!`) dan kurung AND (`&&`) membayangi ekspresi $\neg (p \land q)$. Bersandar kaidah presisi utilitas pembelahan batas penyatuan dari *De Morgan Theorem*, ekspresi luluh menyusut meng-invers ke dalam resolusi utilasi mandiri berwujud $\neg p \lor \neg q$. Di sintaks program hal ini meminimalisasinya dicetak menjadi kodifikasi ringan: `if (!koneksi_aktif || !latensi_rendah)`. 

**Q2**: Apabila anda mendapati klausa bersyarat kondisional "Jika server menyentuh index limit, Maka program dihentikan". Representasikan konversinya jikalau utilasi *instruction set* arsitektur logika CPU hanya terbatas mampu mengenali operator AND, OR, dan NOT belaka!
**A2**: Program perangkat kompilasi primitip melampaui batasan operator tanda deduktif Implikasi ($\rightarrow$) lewat resolusi ekuivalensi utilasi fundamental **Hukum Material Implication**. Ekpresi deklaratif $p \rightarrow q$ mutlak dicoret diganti ditranslasikan secara komputator limit ke relasi gerbang padanan boolean $\neg p \lor q$. Kode komputasi ditranslasikan menjadi format sirkuit ekuivalen: *(NOT)* Server menyentuh limit _OR_ Program dihentikan.

---
