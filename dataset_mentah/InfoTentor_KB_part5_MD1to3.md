---
id_materi: MD-001
mata_kuliah: "Matematika Diskrit"
topik: "Himpunan"
sub_topik: "Teori Himpunan dan Operasi Dasar (Union, Intersection, dll)"
tingkat_kesulitan: "Dasar"
prasyarat: []
---

# Teori Himpunan dan Operasi Dasar

**Ringkasan Materi (TL;DR)**
Teori Himpunan mengkaji konsep komputasional kumpulan tak beraturan (*unordered collection*) dari sebuah referensi subjek unik objek batas tervalidasi atau elemen. Konsep gabungan operasinya menjadi pondasi fundamental algoritma *relational databases*, filter data set komputator mutlak, maupun operasi limit array modern. 

**Konsep / Cara Kerja / Operasi Logika Basis Himpunan**
- Objek elementer ditandai kurung kurawal $\{a, b, c\}$. Semua elemen himpunan bersifat unik, tak mengenal entitas data terdata ganda ($A = \{1,2,2\}$ dikunci resolusi kompilator kembali menjadi array murni $\{1,2\}$).
Empat relasi basis himpunan komputator mutlak:
1. **Union / Gabungan ($A \cup B$)**: Mencapik merangkul mutlak semesta elemen kedua himpunan disatukan sejajar. Elemen irisan kembar direduksi murni satu representator tunggal presisi.
2. **Intersection / Irisan ($A \cap B$)**: Menyaring murni meraba elemen memori presisi entitas perpotongan mutual yang eksak dianut dipunyai berbarengan serempak oleh $A$ mapun $B$.
3. **Difference / Selisih ($A - B$)**: Mengisolasi elemen khusus mutlak kepemilikan dominan di parameter $A$ saja, dikikis dieliminasi mutlak jika ada elemennya terkandung hadir menduplikasi bernaung di array batasan $B$.
4. **Complement / Komplemen ($A^c$ atau $A'$ atau $\bar{A}$)**: Menyisir membasuh seluruh populasi mutlak blok himpunan parameter batas luasan cakrawala Semesta Asimtot (Universe $U$) dengan syarat elemen terpilih BUKAN eksistensi anggota parameter limit $A$.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Simulasikan komputasional *Database Querying* Array batas entitas limit ini: Himpunan limit mahasiswa matkul Algo (A) = \{Tono, Budi, Rudi\} dan Himpunan matkul Struktur Data (B) = \{Budi, Sita\}. Uraikan hasil operasi murni *Symmetric Difference / Beda Setangkup* ($A \oplus B$)!
**A1**: Relasi presisi logis *Beda Setangkup* memuat elemen parameter murni dari himpunan A berpadu mutlak dengan B, namum melarang mensensor mengeliminir elemen mutualis batas irisan komputasi di antara persimpangan keduanya kordinasinya (Eksklusif logis OR). 
Persilangan batas irisan ($A \cap B$) = \{Budi\}.
Penggabungan kordinasi relasi totalnya Union = \{Tono, Budi, Rudi, Sita\}.
Diselisihkan dengan mutualisme irisannya, maka output Beda setangkup presisi akhirnya dicetak menampillkan array final: **\{Tono, Rudi, Sita\}**.

**Q2**: Apabila anda membandingkan manipulasi limit pergerakan perpotongan rimpang struktur himpunan $A - (B \cup C)$, buktikan ekuivalensinya murni memeluk hukum kesertaraan arsitektur komputator distribusi batas presisi dari relasi $A \cap B^c \cap C^c$ !
**A2**: Secara rasio konvolusi, notasi resolusif selisih himpunan komputasional merujuk batasan presisi translasi hukum asimetris substitusi mutlak irisan berpadu negasi komplemen: $X - Y \equiv X \cap Y^c$. 
Mengaplikasika relasi rujukan ini ke batas soal:
$A - (B \cup C)$ ditransmisikan menyebrang transisi utilasi wujud relasi murni ekuivalens: $A \cap (B \cup C)^c$. 
Kemudian mendudukkan rujukan pelebur pilar batas De Morgan's Law komplemen pada Himpunan pergerakan kurungnya menghasilkan presisi relung: $A \cap (B^c \cap C^c)$. Ekstensinya murni seratus persen sama dan koheren mutlak!

---

---
id_materi: MD-002
mata_kuliah: "Matematika Diskrit"
topik: "Teori Graf"
sub_topik: "Teori Graf: Representasi (Matrix/List) dan Terminologi"
tingkat_kesulitan: "Dasar"
prasyarat: ["Himpunan", "Matriks Dasar"]
---

# Teori Graf: Representasi dan Terminologi

**Ringkasan Materi (TL;DR)**
Graf adalah instrumen model abstraksi rasional matematika penampung tata letak *Vertices* ($V$ / Titik simpul node memori) dan *Edges* ($E$ / Garis batas penyambungan). Sangat diandalkan mengawaki sistem arsitkektur penelusur peta murni rute jaringan network topologi, rantai peta silsilah, maupun sistem *Maps* penunjuk rute GPS komplit. Representasinya dikompres direkam ke dalam bentuk array statis Adjacency Matrix atau bentuk fleksibel Adjacency List. 

**Konsep / Cara Kerja / Formulasi Aksiomatis**
Terminologi Primer Graf:
1. **Degree (Derajat Simpul)**: Limit frekuensi jumlah sirkuit jembatan *Edge* yang menancap tertuju utuh berkorelasi kepada satu batas titik sentral *Vertex* tertentu. Graf berarah (Directed) mengklasifikasikan rasio menjadi Indegree (menancap masuk) dan Outdegree (merambat tancap keluar).
2. **Path & Cycle**: Lintasan jalan serangkaian persimpangan simpul yang menapaki rute rentangan tanpa perulangan memutar. Jikalau muara lintasan awal melangkah bertemu persis kembali pulang ke asal muara pelopor (*Loop/Sirkuit*), ia dicap dinobatkan mutlak sebagai *Cycle*.

Batas Pemetaan Relasional Matriks dan List komputator:
- **Adjacency Matrix (Matriks Ketetanggaan):** Susunan sel bujur per-index memori Array $2D$ ordo $(V \times V)$. Diisi Biner 1 apabila sel index simpul $i$ dan limit $j$ direngkuh sambungan Edge murni, dan diisi 0 jika lintasan mati putus. Limit waktu pelacak sangat kilat sebatas komparasi sel index ruang asimtot $\mathcal{O}(1)$, namun boros memakan utilasi penyimpanan batas array rasion quadratik memori raksasa di $\mathcal{O}(V^2)$.
- **Adjacency List (Daftar Ketetanggaan):** Menugaskan list himpunan dinamis per simpul mengabsen satu per satu elemen tetangga absolut terhubungnya rutenya. Irit rasio penyimpanan asimtot optimal di rentangan rasion $\mathcal{O}(V+E)$, tapi pelacakan index lambat karena dituntut menyeka memutar deretan relasi linear barisan referensial satu satu.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Misal arsitektur rute penunjuk jalur *Google Maps* ditugaskan merepresentasikan algoritma relasi jutaan lokasi seluruh peta persimpangan persendian jaringan murni sedunia ("Sparse Graph" lebat V titik, minim persimpangan E rutenya pinggiran). Manakah utilasi murni pendelegasian struktur data yang absolut tak disarankan berpatok mutlak digunakan merekap jutaan jaringan GPS komputasional memori ini?
**A1**: Sangat dilarang berspekulasi menggunankan konstruksi blok pemetaan parameter statis mutlak **Adjacency Matrix ($V \times V$)**. Di graf jarang *(Sparse graph)* rute simpul jutaan ($V= 10^7$ node lokasi), array murni statis komputator tersebut akan memaksakan mutlak menuntut alokasi pembongkaran penampung rasio ruang utilitas memory array matriks absolut quadratik $10^{14}$ sel ukuran rimpangnya! Padahal probabilitas mayoritas miliaran selnya ini dipastikan dibiarkan menganggur kopong tak berkoneksi mutlak (Biner 0 batas putus relasi kota berlainan benua). List rujukan Dinamis Adjacency List murni merangkum tervalidasi irit menekan pemborosan *space* mutlak memori secara presisi tak tandingi. 

**Q2**: Apabila sebuah batas parameter Graf tak-berarah *(undirected)* komputasi memiliki kuota rasio populasi batas populasi populasi perihal titik Node merengkuh V=7 dan perolehan Edge jalinan sirkulasinya E=13 batas, Berapakah mutlak parameter ukuran himpunan besaran batas *Sum of All Degrees (Total jumlahan populasi Derajat dari ke-7 simpul komputator simpul murninya)*? 
**A2**: Batas rasional penyelesaian dikunci presisi komputasi formula *Handshaking Lemma (Hukum Jabat Tangan Grafik)*. Teorema lemma logis membuktikan rasio jumlahan mutlak derajad entitas populasi simpul graf batas semesta selalu merujuk presisi ke asimtot lipat dwi ganda ganda nominal jumlah persendian tepi Edge rutenya: $\Sigma deg(v) = 2 \times |E|$. 
Berarti parameter utuh pengandaan jumlah keseluruhan total derajat node-nya dikalkulasi presis murni: $2 \times 13 = \mathbf{26}$ derajat komputasional. Hal ini divalidasi mutlak rasional bernilai logis genap sempurna asimetris.

---

---
id_materi: MD-003
mata_kuliah: "Matematika Diskrit"
topik: "Struktur Pohon"
sub_topik: "Struktur Pohon (Tree) dan Binary Tree Dasar"
tingkat_kesulitan: "Menengah"
prasyarat: ["Teori Graf Dasar"]
---

# Struktur Pohon (Tree) dan Binary Tree Dasar

**Ringkasan Materi (TL;DR)**
Dalam komputasional presisi diskrit, Pohon (Tree) tidak lain berupakan arsitektur penyederhanaan hirarkial dari blok graf terhubung yang dilarang melanggar satu pantangan keramat: ***Sama Sekali Tidak Boleh Ada Siklus Muter (Acyclic)***. Tree utuh diutus diforsir menelusur susunan rasio direktori File disk, pohon tata susunan arsitektur logika relasi Silsilah keluarga *(Genealogy)*, dlsb. *Binary Tree* membatasi pakem simpul bapak maksimal melahirkan 2 turunan simpul anak *(Left Child & Right Child)*.

**Konsep / Cara Kerja / Formulasi Properti Tree**
1. **Akar Inti (Root)**: Pucuk menara sentral tertinggi penyanggah utama sirkulasi anak turunannya batas (Level 0 rentang mutlak rasional atas). 
2. **Daun Pangkal (Leaf/Terminal Node)**: Simpul pemungkas ujung terbawah mati putus tak berdikari melanjutkan generasi cabang asoasi sama sekali (Degree Out-nya nihil murni batas limit 0). 
3. **Internal Node**: Persimpangan Node peralihan komputator di antara Root asal pelopor hingga limit Leaf (memiliki simpul anak memori turunan murni). 

Struktural limit rasion komputasi presisi Tree mematuhi hukum simetrik ekuivalens: Sebuah blok tata Graph yang direpresentasikan diisi padat murni komputasi titik sebanyak $N$ simpul parameter Vertices, bilamana relasi tersebut sah menyandang tahta "Tree/Pohon" ia mutlak cuma menguras memori menanam jumlah sirkulasi Edge batas relasional murni eksak sebatas rasion pengurangan utuh linear $\mathbf{N - 1}$ tepi Edge penghubung.

**Varian Penelusuran Traversing Binary Tree Laju Eksekusi Arah SubTree:**
- **Pre-Order (Prefix)**: Visit simpul ROOT asimtot teratas $\rightarrow$ sapu Left Child $\rightarrow$ susuri Right Child purna pelan.
- **In-Order (Infix)**: Susuri sub rantai Left $\rightarrow$ Visit ROOT inti simpul $\rightarrow$ melangkahi sub rantai Right limit purna. Mampu menderetkan pencetakan urut limit biner pencarian biner sortasi murni rapi presisi *Binery Search Tree ascending*.
- **Post-Order (Postfix)**: Telusuri mutlak seluruh kompartemn anak dari mutlak (Left Child $\rightarrow$ Right Child terlebih dulu) purna lunas, baru dipangkas di eksekusi mengevaluasi bapak ROOT-nya sendiri (Sangat sering diforsir mengeksekusi algoritma "Delete/Free-Memory Child sebelum Bapak" secara teliti *bottom-up garbage memory collection rasional*). 

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Simak struktur memori direktori Folder File Windows, di mana tak murni dijumpai rujukan direktori Root yang memiliki relasional mutlak "shortcut anak didalam memori path cucu referensial bapak path root folder memutar yang menembus atapnya sendiri murni atas". Jelaskan justifikasi argumen sifat mendasar arsitektur Tree komputasi murni yang menolak intervensi rute komputator tersebut?
**A1**: Peta direktori File struktur dirancang mengawaki arsitektur presisi relasional basis data *Acyclic Directed Graph Tree* mutlak. Tree melarang eksistensi skema keberadaan perputaran rute memori lintasan jalan tak berujung batas kembali terjerembab (*Loops/Cycles* melingkar tertutup rimpang murni memutar mendarat di asal tumpuan pelopor perintis awalnya). Andai "shortcut mutlak direktif parameter anak mereferensikan membalik ke parameter Folder root tetuanya" diserlarkan diperkenankan, ikatan graf ini gagal bergelar utuh merasuk menyandar sebagai model fungsional Tree murni lantaran menyalahi properti *Acyclic* limit utuh fundamental bebas sirkit komputasional logis logikannya.

**Q2**: Apabila anda diutus menjaring kompilasi tata rimpangan Pohon Keputusan batas asimetri murni Full Binary Tree (Pohon Biner Penuh di mana setiap Parent mutlak harus memiliki simpanan utuh persis 2 pasang anak ganda relasional mendampingi sejajar tanpa toleransi putus). Bila limitasi daun terminal purna pamungkas (*Leaves*) komputasional di limit parameter tercetak rasional genap berjumlah 15 simpul blok, perhitungkan besaran tuntas nilai mutlak batas presisi Internal Nodes titik percabangan yang memayungi membiakkan barisan mutlak terminal Leaves tersebut utuh!
**A2**: Mengakar mereferensikan derivatif hitungan murni konformasi batas Hukum Proporsi Dasar *Full Binary Tree*, tervalidasi rumus mutlak memandu bahwa segenap simpul Internal percabangan Node blok murninya ($I$) disetarakan persis komputasional melurus relasinya merujuk presesi pengurangan $Leaves$-terminat ($L$) susut dikikis dengan bilangan rasio rujukan satu angka parameter ($L - 1$). Jika asimetri populasi terminal $L = 15$ presisi mutlak tercapai. Internal persilangan rute titik persendiaan rimpang node divalidasi komputasi murni mencakup presisi rentang mutlak batas $I = 15 - 1 = \mathbf{14}$ Simpul persilangan murni Internal bercabang gandan pembagi.

---
