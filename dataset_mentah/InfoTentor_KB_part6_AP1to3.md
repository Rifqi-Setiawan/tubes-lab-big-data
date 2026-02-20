---
id_materi: AP-001
mata_kuliah: "Algoritma dan Pemrograman"
topik: "Struktur Dasar Eksekusi Kode"
sub_topik: "Struktur Percabangan (If, Else-If, Switch)"
tingkat_kesulitan: "Dasar"
prasyarat: ["Logika Proposisional"]
---

# Struktur Percabangan (If, Else-If, Switch)

**Ringkasan Materi (TL;DR)**
Kompilator mengeksekusi skrip komando per baris linear sekuensial merambat ke bawah mendatar terstruktur. *Struktur Percabangan (Conditional Flow)* mendobrak mendikte memecah alur komputator utilasi program murni untuk menyebrangi melempar interupsi pengeksekusian blok utilitas memori spesifik *HANYA JIKA* lolos mematuhi seleksi parameter relasional komparitas tertentu (TRUE). Jika gagal menembus kondisi prasyarat uji, skrip lompat blok tersebut dan menyortir di interupsi kondisional berikutnya.

**Konsep / Struktur Blok Kondisional / Sintaks Abstrak**
1. **If Murni Tunggal**: Eksekusi seruluh utilasi program di badan balok ini murni kalau batas prasyarat terpenuhi (1/True). Kalau gagal, eksekusi dilangkahi di-bypass mutlak.
2. **If - Else Bersyarat Alternatif**: Menyuntikkan jalur percabangan pertolongan (Plan B). Kalau uji validasi argumen blok `If` gugur putus (0/False), arus daya prosesor mutlak dihantamkan membelot dialirkan murni mengeksekusi parameter balok sintaks komando alternatif di gerbong instruksi perbatasan mutlak `Else()`. 
3. **If - Else If Berantai**: Rangkaian memburu kordinasi berlapis berlipat ganda rasion kondisional untuk komparasi bertingkat lebih dari dwi-kondisi.
4. **Switch - Case**: Percabangan struktur asimtot perbatasan optimal ditujukan mengakomodir utilasi relasional nilai mutlak presisi bulat konstan komputator mentah, misal menampung batas Menu Pilihan Navigasi UI parameter konstan (Contoh: Case `1`, Case `'A'`). Diperlukan pemecah saklar rem iterasi baris perintah parameter mutlak **`Break;`** supaya eksekusi utilasi program menahan membendung loncatan komputatornya jatuh kebablasan tergelincir menabrak memecah mengekseskusi limit barisan `Case` dibawahnya *(Mengindari skenario kecelakaan Fall-Through Bug)*.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Simak pseudo program percabangan berjejer berikut: 
```python
x = 10
if (x > 5):
    print("A")
if (x % 2 == 0):
    print("B")
else:
    print("C")
```
Apakah luaran pencetakan terminal pasca utilasi mutakhir skrip diatas? Kenapa tidak memakai sintaks referensi utilitas `Else If`?
**A1**: Program mencetak tervalidasi menjejalkan susunan keluaran mencetak **"A" dan "B" secara berderet**. Karena ke-dua parameter blok utilasi `if()` tersebut merupakan rantai eksekutor independen tak terikat rasional (Saling tak mempedulikan urusan masing masing independesi evaluasinya). Jika komputator menata menulisnya melengkungkan struktur gabungan murni di bawah gerbong rentetan **`Else If (x % 2 == 0)`**, lantas luaran program akan mentok dibendung pencetakan pertama keluarannya di output log **"A"** saja, karena `Else If` ditujukan melangkahi melewari iterasi uji parameter evaluasinya mutlak jika sekat `If` awal yang membawahinya mendahuluinya telah duluan sukses dinilai teruji terpenuhi.

**Q2**: Apabila anda membandingan skenario batas arsitektur komputasi pencarian presisi batas rentang asimetris "Mencari status grade mahasiswa bila nilainya di antara rentang floating mutlak batas `80.5` sampai presisi `90.0`". Manakah utilitas rimpangan seleksi yang dibenci mutlak tak sanggup dieksekusi kompilator dan diforsir ditolak digunakan: Struktur *Else-If Tree* ataukah metode referensial struktur sintaks *Switch-Case*?
**A2**: Metode penugasan utilitas rasio seleksi **Switch-Case murni ditolak dan dibenci di blokir** kinerjanya. Sifat alamiah komputator memori sirkuit pencarian komparitor arsitektur utilasi bahasa *Switch-Case* ini tak digubah mengenali evaluasi limit relasional rentang (*Range evaluation* `<`, `>`). Algoritmanya tak lain sebatas mencacah membanding presisi angka kongruen yang bertumpu menabrak tipe numerik Konstan Diskrit mentah integer maupun *char* byte persis ($Switch(10)$ kongruan presisi harus murni menabrak pas *Case 10*). Tipe parameter desimal *(Floating point)* dilarang secara presisi sintaks dalam argumen kondisi `Switch()` konstan tersebut. Utilitas uji rentang mutlak domainnya diforsir diproses dikawal hanya via gerbang perbatasan komparasi *If-Else*.

---

---
id_materi: AP-002
mata_kuliah: "Algoritma dan Pemrograman"
topik: "Struktur Dasar Eksekusi Kode"
sub_topik: "Struktur Perulangan (For, While, Do-While)"
tingkat_kesulitan: "Menengah"
prasyarat: ["Struktur Percabangan"]
---

# Struktur Perulangan (For, While, Do-While)

**Ringkasan Materi (TL;DR)**
*Looping* (Perulangan iteratif iterasi) mensimulasikan mekanisme utilasi komputator untuk mengeksekusi melahap membaca serangkaian badan kode secara membabi-buta berulang kali (Loop) mengitari baris blok yang mutlak seragam. Iterasi terus berotasi mutlak sampai ditahan disfungsi ketika terbentur dengan perbatasan uji pilar parameter *Condition Validation* mutlak menghasilkan penilaian False (0) yang membebaskannya meroboh menghentikan perputaran limit kodenya. 

**Konsep Ruang / Format Pemutar Logika Loop**
1. **For Loop (Count-Controlled)**:
Iterasi mutlak dibatasai pilar kuantitas jumlah perulangan komputasi mutlaknya secara rigid telah dikalkulasi purna dari awal titik inisiator eksekusi skrip murni.
Format pilar susunanya: `for (Inisialisasi variabel awalan; Cek relasional Limit stop; Aksi Increment laju pertambahan)`.
Sangat primadona utamanya diforsir membongkar menyeka menyisir deretan baris Index batasan array List sekuensial.
2. **While Loop (Condition-Controlled)**:
Berputar tak terbatas mutlak selama evaluasinya memegang predikat benar `True()`. Pengecekan limit prasyarat dijaga diregulasi dan dites diletakan posisnya di atap pintu masuk (Pre-test) pangkal instruksi paling utama loop. Bila perdana langsung divonis False, blok badan perulangan takkan tereksekusi sedikitpun nol kali mutlak.
3. **Do-While Loop (Exit-Controlled)**:
Varian kebaliakan dari utilitas di rentang skema While. Pengecekan argumen kondisi limit diletakkan ditunda posisisnya menjalar ke tapal batas pinggir terminal pangkal ujung di blok kaki rimpang terbelakang *(Post-test loop)*. Hal perancangan aneh ini mutlak menjanjikan eksekutor blok iteransinya dipastikan menggaransi *minimal satu kali murni* eksekusi gerbong kode mutlak diputar walau ternyata batas kondisi aslinya salah secara mutlak gagal direalisasikan sedari mula awal nilainya.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Simak rutinitas loop perbatasan While di program sintaks abstraksi skrip ini:
```python
penghitung = 5
while (penghitung > 0):
    print("Log Server")
    # lupa menulis increment/decrement update
```
Kelalaian komputasi kecacatan utilitas eksekusi macam apa yang membentur menyandera di program komputator referensi tersebut dan di mana letak solusi mereparasinya?
**A1**: Insiden *Bug* ini dinobatkan membongkar utilasi mesin meledakan perputaran batas iteratif limit mutlak bernasib **Infinite Loop Error (Perulangan Gagal Henti Tak Berhingga)**. Parameter `while` senantiasa ditanam menginstruksi loop mengecek rasio kordinasi (`5 > 0`), nilainya akan langgeng senantiasa abadi mutlak True(1) selamanya karena tiada sebarispun interupsi fungsi pemangkas pengubah kondisi parameter (`penghitung`) di tubun kodenya tersebut nilainya konstan 5. Relung pemecah meretas mengobati penyakit *bug* memori siklus mutlak ini wajib ditambahkan injeksi *Langkah Update Statement Incrementer* variabel misalnya: `penghitung = penghitung - 1` disisipin menyentuh merapat di parameter ujung memori akhir blok putaran eksekusinya.

**Q2**: Apabila anda mendeklarasi arsitektur perancangan menu panel navigasi grafis awal UI (Tampilan Menu Awal Interaktif "Tekan 1 untuk Main, 0 untuk Exit"), rutinitas batas sirkulasi memori iteratif mesin `Loop` format apakah yang mutlak lebih diprioritaskan diforsir kompilator untuk digunakan, bila di batasan rasionya disyaratkan parameter "Program wajib serentak berjalan menampilkan pilihan menu secara instan sebelum melakukan interupsi membaca evaluasi menunggu *input* pilihan batas syarat di terminal memori dari sang User"?
**A2**: Batasan struktur relasional iterasi pelonjakan yang diprioritaskan dicanangkan adalah memori mutlak pemutar perbatasan murni struktur rasional **Do-While Loop**. Esensinya murni terlahir karena perlakuan rutinitas skenario menyoal program mencetak layar murni dijamin bergaransi memutar tereksekutor merapat tayang menampilan Menu Grafis minimal eksak sekadar $1$-kali perputaran langkah utuh *(di blok Do)*, tak mengindahkan batas memori apa kondisi status batas awalan inputannya, baru selebih rentang putaranya dievaluasi bergelantung merujuk memprioritaskan mengecek meraba kondisional batas validasinya bergantung pada apa yang pengguna utarakan *(di gerbang mutlak penjaga gawang evalusi `While(input != 0)` di pilar blok belakangan posisinya)*.

---

---
id_materi: AP-003
mata_kuliah: "Algoritma dan Pemrograman"
topik: "Struktur Data Elementer"
sub_topik: "Struktur Data Dasar: Array 1 Dimensi dan 2 Dimensi"
tingkat_kesulitan: "Dasar"
prasyarat: ["Tipe Data dan Variabel Dasar"]
---

# Struktur Data Dasar: Array 1 Dimensi dan 2 Dimensi

**Ringkasan Materi (TL;DR)**
Variabel biasa murni membatasi rentangan daya tampung menjaring menjebol satu butir entitas sel presisi nilai datum. Apabila parameter data yang masuk membengkak rentangannya membuntut murni bernada selaras tipe datanya sejenis seragam (Contoh: deret Nilai Matematika untuk 100 Siswa serentak), utilitas pendigitasian memecah kordinasi mutlak didelegasi menggunakan penampang tatanan *Array/Larik*. Array melipatgandakan perangkaian perbatasan blok-blok porsi sel RAM berdekatan di memori secara kontigu terjejer presisi membentuk satu blok raksasa bervariabel tunggal.

**Konsep Anatomi Komputasional Array**
Setiap potongan blok relung kotak porsi ruang penyimpanan berhimpun dari Array dijuluki *Elemen Datanya*. Alamat identifikasi referensi kordinasinya dipandu dicokok memakai penomoran utilasi *Index / Subscript*. Kompilator komputator konstan modern memelopori mendudukkan pendaratan rentangan indeks pelopor awalan element pionir bertepatan sejajar selaras memuati indeks nomor mutlak komputasi Index basis pangkal titik **`0`**. 
1. **Array 1 Dimensi (List/Vektor)**: Susunan tata batas melintang linier deret mutlak membentang lurus linear baris horinzontal. Pengindeksan variabel tatananya sederhana (misal `Nilai[4]` diakses berpelopor dari kordinat letak gerbong ke-5 di dalam balok urutan memorinya).
2. **Array 2 Dimensi (Matrix/Tabel)**: Representasi blok perpaduan penyatuan berlembar-lembar tatanan pilar struktur array linear di tumpuk renteng berbaris menyusun barikade himpunan matriks *Baris dan Kolom*. Pemetaan perbatasan memori direferensi menjalar menembak mutlak lewat dwi-kordinasi ganda bersarang dua tanda parameter index kurung kordinat (`[row][column]`). Misal pemetaan mutlak penampung Array Matrix batas papan catur batasnya diforsir `Papan[8][8]`.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Uraikan kalkulasi mutlak resiko perbatasan utilitas tabrakan mesin *Bug Error Index Out of Bounds Memory Access* di array? Andaikan ada deret blok struktur komputasi limit aray `int daftar_angka[10]`. Bila porsi rutinitas pengembalian instruksionalnya dipaksa merogok menjejalkan meraba utilitas indeks ke rentangan instruksi `daftar_angka[10] = 50`, parameter logis batas mana yang menyalahi membelot utuh digerus utiliti skrip rentang ini?
**A1**: Porsi rentangan deklarasi awalan `[10]` menyematkan batas ukuran kuantitas slot laci muatan komputator RAM-nya dialokasikan digaransi menjatah merenggut utuh menampung presen kapabilitas total limit 10 laci porsi elemen kapasitas Array *integer*. Sistem kompilator referensi batas Array senantiasa me-"reset" nol penanda penomoran registrasinya melangkah presisi iterasi pelopor awalan bernomor start pijakan titik indeks `$0$`. Karena diturunkan serempak pergerakan titik awalnya dari basis mutlak $0$, letak mutlak ujung ekor gerbong akhir laci indeks ke-sepuluh komputator ini otomatis telah dirujuk dilimitasi dan mentok hanya bermuara dikoordinal registrasi indeks penampung parameter batas penutup **`[9]`** terakhirnya asimtotnya. Menjejalkan atau merogoh meraba mutlak pemanggilan rentangan di barisan instruksi nilai pilar sintaksi indeks nomer komputasi mentah ke **`[10]`** bakalan dihempas ditolak kompilator lantaran mesin perbatasan ruang ini menyasar ruang laci ke-11 ilusi mutlak yang sejatinya berada menyebrang meluber melahap lokasi ruang rentan *di luar zonasi limit tapal perbatasan RAM blok elemen legal* alokasi rimpangan Array berbatas `daftar_angka` tersebut berakar teritori memorinya yang utuh dialokasikan.

**Q2**: Apabila instruksi susunan mesin komputator anda diforsir dituntut merekam perbatasan jejak data absensi kehadiran kelas harian presisi setiap siswa asoasi di setiap presi hari tatanan semester penuh (Misal referensi perempatan kordinat "Kehadiran Murid Si Budi di Hari ke 43 termutakhir"), bagaimanakah arsitektur pemetaan kordinasi kerangka deklarasi struktur perbatasan matriks representasional `Array 2 Dimensi` diformalisasikan dikonfigurasi utilitas memorinya? Uraikan skema rasio sumbu tatananya!
**A2**: Skenario utilasi model seperti rentang ini absolut murni membutuhkan pemetaan ruang blok presisi himpunan representasi barikade tabel tatanan memori tabel silang Matrik dua sumbu dimensi struktur Array `Absensi[baris_index][kolom_index]`. Pemetaan kordinatnya diwakilkan presisi utuh dirasionalisasikan mendudukan limit elemen: Parameter kurung utilasi awal **Index Baris limit pertama (`[baris_index]`)** digunakan didaulat merepresentasikan relasinya mutlak menyimpan pengenal referensi unik nomer ID perbatasan indeks Absen untuk referensi rujukan perwujudan satu nama entitas mutlak referensi setiap para "Individu Siswa/Murid". Parameter struktur kurung rentangan lanjutan sirkulasinya yang dibelakang merujuk pilar sumbu yang kedua yaitu **Index Kolom silang kedua (`[kolom_index]`)** digunakannya diforsir mendudukkan batasan presis titik representasinya utuh merekam rentangan laju linear menunjuk melacak rentangan pilar utilitas terekam memanjang barisan tatanan referensi nomer indeks Hari presisi dari urutan hari berjalannya pertemuan tatap muka semester kelas limit pertemuan di kelasnya tersebut referensial logisnya mutakhir direkam memorinya utilitasnya utuh.

---
