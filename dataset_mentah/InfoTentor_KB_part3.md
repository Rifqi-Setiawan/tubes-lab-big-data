---
id_materi: AP-006
mata_kuliah: Algoritma dan Pemrograman
topik: Algoritma Pencarian
sub_topik: Linear Search (Kelebihan & Kekurangan dibanding Binary)
tingkat_kesulitan: Dasar
prasyarat: Struktur Data Array Dasar
---

# Algoritma Pencarian: Linear Search

**Ringkasan Materi (TL;DR)**
*Linear Search* (Pencarian Sekuensial) adalah metode algoritma asimtotik pelacak elemen yang menyusuri dan mencocokkan nilai sasaran target elemen demi elemen dari ujung index $0$ larik (*array*) hingga batas akhirnya $n-1$. Kompleksitas kerjanya maksimal dituntut eksekusi linear $\mathcal{O}(n)$, dan utamanya unggul karena tidak mewajibkan data berserakan yang diterimanya untuk disortir pengurutan terlebih dahulu.

**Konsep / Cara Kerja / Pseudocode Kompleksitas**
Pencarian berjalan di dalam bingkai loop interatif yang membandingkan setiap lokasi `array[i]` dengan `target`. Jika *True*, mesin me-*return* nilai *index*. Jika mentok tidak menemukan kesesuaian satupun di array, kembalikan bendera (misal `-1`).

**Kelebihan (vs. Binary Search)**
1. **Tidak Wajib Terurut (No Sorting Required)**: Binary Search diwajibkan menyortir array (yang biayanya $O(n \log n)$). Linear search mampu mencerna input data serampangan seketika tanpa pra-kondisi.
2. **Cepat di Larik Kecil**: Untuk list yang ukurannya sangat mikro, iterasi *Linear Search* acapkali lebih irit beban kalkulasi logika awal daripada harus menghitung posisi partisi membelah nilai paruh-tengah di set Binary search.

**Kekurangan (vs. Binary Search)**
Pencarian data di *Big Data* ber-array raksasa menyumbang komputasi mengerikan dengan performansi siklus batas terburuk merangkak asimtot waktu $\mathcal{O}(n)$. Ini jauh tertindas dibanting efisiennya lompatan putaran *Binary Search* penembus $\mathcal{O}(\log n)$.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Sebutkan perihal variabel skema keadaan iterasi yang merengkuh kecepatan eksekusi Linear Search pada batas waktu optimal konstan $\Omega(1)$?
**A1**: Skenario kondisi utuhnya didapat hanya tatkala nilai angka parameter buruan tersebut bernasib pas bertengger di titik kamar paling awal *array* bernomer index dasar `$0$`. Program mengutus pengecekan sirkulasi perdananya dan langsung ter-interupsi menang menemukannya, tuntas sekejap tanpa mutlak menjahit komputasi iterasi siklus kedua dan seterusnya.

**Q2**: Jika array berisi 1 juta elemen rekaman transaksi *log server* tak berurut, mengapa kita disarankan pakai Linear Search alih-alih merubahnya menjadi skema Binary Search?
**A2**: Arsip antrean *log server* tabiat aslinya senantiasa dibubuhi bertambah dinamis secara serampangan tak rapi susunannya. Menerapkan *Binary Search* mensyaratkan kewajiban pra-proses penataan urutan data (Sorting) yang sangat boros menghabiskan limit memori $\mathcal{O}(n \log n)$ setiap saat. Sedang Linear Search siap sigap menangani lacakan log instan di jangkauan batas utuh $\mathcal{O}(n)$.

---

---
id_materi: AP-007
mata_kuliah: Algoritma dan Pemrograman
topik: Algoritma Pengurutan
sub_topik: Selection Sort
tingkat_kesulitan: Menengah
prasyarat: Array Dasar dan Loop Bersarang (Nested Loop)
---

# Algoritma Pengurutan: Selection Sort

**Ringkasan Materi (TL;DR)**
*Selection Sort* (Sortasi Pilihan) merupakan pondasi algoritma pengurutan barisan elemen purba dengan menancapkan sekat area larik *terurut* dengan *belum terurut*. Ia bekerja ajek menginspeksi mutlak rimpangan array *belum terurut* untuk mencari element pemegang takhta terkecil, dan kemudian memindah-paksakan posisinya *(Swap)* ke rel tepi paling permulaan di zona terurut agar zonanya meluas 1 kompartemen bilik baris secara progresif. 

**Konsep Ruang / Cara Kerja Fisiologi**
**Pseudocode Kompleksitas (Python):**
```python
def selection_sort(arr):
    n = len(arr)
    for batas_urut in range(n):
        # asumsikan angka parameter index saat ini paling minimum
        index_min = batas_urut
        # inspeksi elemen tersisa sekuens di kanannya
        for j in range(batas_urut + 1, n):
            if arr[j] < arr[index_min]:
                index_min = j
        # lempar rotasikan mutasi nilainya ke awal depan
        arr[batas_urut], arr[index_min] = arr[index_min], arr[batas_urut]
    return arr
```
Asimtot waktu mutlak selalu menyedihkan menyentuh iteratif batas putaran $\mathcal{O}(n^2)$ pada seluruh sisi cuaca rute kondisi (Mesti arraynya sudah terurut, utilitas barisnya tetap mengamati utuh). Namun limit rotasi Swap datanya tangguh konstan sangat pelit irit dibatas ruang perbatasan $\mathcal{O}(n)$.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Diberikan porsi data list array: `[45, 12, 59, 21]`. Uraikan transformasi bentuk susunannya tatkala tuntas melewati putaran langkah (*Iterasi i*) nomer urut Pertama dari blok sistem utilasi *Selection sort*!
**A1**: Paska putaran babak $i=0$ (Pertama). Relung algoritme melacak membasuh rimpang susunan data awal menemui nilai tervalidasi $12$ memegang predikat angka termungil seutuh array. Menukarnya *Swap* banting menggeser $12$ ke singgasana $45$. Formasi blok barisan merubah tampilannya dirampungkan menjadi: `[12, 45, 59, 21]`. 

**Q2**: Hal keistimewaan luar batas asimtotik apa yang dinilai unggul secara presisi pada rancangan utilitas usang *Selection sort* membalap kelas mentereng lainnya yang membuatnya masih terpakai valid pada instrumen penyimpan gawai berbatas ketat (*Contoh: EEPROM/Flash NAND Wear Limit / Memori penulisan ketat*)?
**A2**: Atribut utamanya adalah pelit super ngirit siklus rutinitas silang penukaran fisik *Memori Mutasi Swap penulisan flash block* pergerakannya ke *Storage*. Asimtot beban utilitas swap memori rotasinya dikurung mutlak asimtot atasnya bertengger hanya mentok di rotasional batas linear utilasi asimtot atas linear rentang jumlah $\mathcal{O}(n)$ blok fisik mutlak gubahan silang. Lawannya seperti Algoritma sortasi *Bubble Sort* merajai penyiksaan penabrak usia disk komputasi karena merotasi liar berkalang rimpang *Write* penukaran data sirkuit per memory menyentuh kubik ganda meroket pembengkakan rotasinya di perbatasan mutlak $\mathcal{O}(n^2)$ usia.

---

---
id_materi: AP-008
mata_kuliah: Algoritma dan Pemrograman
topik: Manipulasi String Dasar
sub_topik: Manipulasi String Dasar
tingkat_kesulitan: Dasar
prasyarat: Tipe Data Karakter Murni, Biner Tabel (ASCII)
---

# Manipulasi String Dasar

**Ringkasan Materi (TL;DR)**
Dalam tata komputator *hardware*, *String* murni beridentitaskan sebagai baris urutan majemuk (*Array*) tipe data Karakter tunggal *(Characters / chars)* yang berangkulan. Manipulasi utilitas baris ini *(Pemotongan Slice, Concatenation / Perpaduan, Transmutasi Case Lower ke Atas Huruf)* adalah utilitas primitif inti kerangka sistem utilasi data tekstual mesin pemrograman.

**Konsep Inti Pembedahan Karakter**
Secara anatomi memori, susunan rentetan per karakter huruf (*Misal:* `B`, `i`, `g`) diregistrasi rujukan bitnya berlabuh pada tatanan nilai mutlak per-index kode biner *ASCII* (Huruf `A` bernilai representasi nominal 65, huruf mungil `a` mendarat di baris angka pergeseran nomer 97). Penutup terminal akhir *String* berhukum di bahasa rendah lazim ditutup menyematkan balok Karakter Nol `\0` (Null terminator).
1. **Concatenation (Penggabungan)**: Menyatukannya melibatkan peng-kopian isi rimpangan array String B diserap mengokupasi index ruang sisa kekosongan ujung di perbatasan null teminator milik entitas String A. 
2. **Sub-Substringing**: Pemenggalan blok rimpang array dengan menspesifikasikan index batas `start` hingga potongan parameter limit target index presisi `end` ke wujud deklarasi alokasi *variabel ruang String array* mandiri.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Bagaimana konsep mesin memanipulasi algoritme dasar rotasi pergeseran penormalan wujud Huruf per Karakter Kapitaslik "A" supaya menjelma rupa mengecilkan fonetik huruf gubahan *Lower Case* utilasi "a"? 
**A1**: Kompilernya tidaklah meraba bentuk *font shape* rupanya, ia hanya mengevolusi pergeseran relung aritmatika deret array integer. Di konvensi ASCII, rentangan mutlak konstan spasi antar huruf kapital (misalnya `A` bernilai angka register 65) dibanding versi mini `a` (bermutlak register angka 97) berselisih ruang kosong integer seluas presisi selisih angka konstan 32 interval. Komputernya sebatas perlu mengais menjumlahkan entitas nilainya `A + 32` ditambatkan kembali ke memory, seketika program akan disuguhi wujud mencetak simbol *char* bernilai karakter mininya (`a`).

**Q2**: Apabila utilasi ruang Array string tidak dibubuhi tanda pamungkas gerbong penutup pengawal `\0` (Null karakter) di ujung belakangnya, ancaman *bug* rentan seperti apakah yang bakal merangsek ke sistem saat kita melakukan iterasi mencetak Print string-nya di program berdasar bahasa memori rawan C/C++?  
**A2**: Loop proses pencetakan *Print out* tidak mengenali tanda henti limitasi tuntas panjang array kalimat yang di-instruksikannya. Ia akan serampangan liar menerabas memuntahkan memori tatanan bytes milik variabel komputator orang lain dan instrupsi acak yang bukan teritori porsinya dari perbatasan RAM *(Buffer Over-read / Segmentation Fault crash)* sampai ia tak sengaja terjumpa di RAM kode byte rincian "0" secara acak tersendiri di luar memori miliknya. 

---

---
id_materi: AP-009
mata_kuliah: Algoritma dan Pemrograman
topik: Konsep Berpikir
sub_topik: Konsep Dasar Rekursif (Recursion) dan Base Case
tingkat_kesulitan: Menengah
prasyarat: Fungsi (Function Dasar), Konsep Stack Memori
---

# Konsep Dasar Rekursif (Recursion) dan Base Case

**Ringkasan Materi (TL;DR)**
Fungsi Iterarif mengulangi utilasi barisan rutinitas mengkudeta sintaks loop kontrol iteratif dasar (For/While). Sebaliknya, **Rekursif** bermodalkan fungsi yang mengeksekusi iterasi utilasinya *dengan cara merujuk bersahut memanggil memori eksistensi rutinitas utilasi fungsi nama dirinya *(invoke itself)* kembali berkaca dari dalam blok tubuh kodenya*. Diwajibkan hadir batas dasar stop muara iteratif yang menahannya, yaitu baris kondisional **Base Case**. 

**Struktur Cara Kerja / Pseudocode Komputasinya**
Apabila tak dikomandoi palang *Base case*, ia mendaratkan programnya masuk ke tabrakan perulangan tak perkesudahan pengisian balok limit tumpukan rasion memori *Call Stack Overflow memori tabrakan iterasi putus*.
Format Murni *Recursive function* pemecah bilangan faktorial nilai $(n!)$:
```python
def fungsi_faktorial(n):
    # BASE CASE (Batasan pemberhentian mutlak pantulan)
    if n == 0 or n == 1:
        return 1
        
    # KONDISI REKURSI (Recurrence Relation panggil balik diri mereduksi)
    else:
        return n * fungsi_faktorial(n - 1)
```
- Setiap perombakan panggilan *fungsi_faktorial(n-1)*, parameter $n$ direduksi diperkecil limitnya pelarianya dipersingkat memeras agar segera bertabrakan menggedor dengan batas atap muaranya di palang kondisi *Base case*.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Konsep struktur penyokong memori LIFO ganda apa yang dikudeta arsitektur OS menopang penumpukan antrian nilai eksekusi kembalian fungsi Rekursif, dan limit anomali pembengkakannya berdampak meledakkan sistem *bug* bermuncul error bernama apa?  
**A1**: Pengekangan antrian urutan kembalian eksekusi merengkuh penyokong deret memori data **Call Stack**. Kalau perulangan Rekursif ini gagal beralih tuntas meruntuhkan *Base Case* dan mutlak liar memanggil tiada penghabisan limitasi rentangan tak tervalidasi, memori utilasi *Stack* CPU menjumpai jurang fatal tak lagi sanggup membelah sisa rentangan ruangnya menampung *limit variable*. Merengseknya sistem ini mutakhir diistilah error tabrakan memory murni **Stack Overflow Error / Segmentation Fault**.

**Q2**: Adakah komputasi beban kerisauan asimtot waktu rentan yang dihindari oleh pemrogram profesional jika mengeksekusi iterasi algoritma sekuen purba Rekursi klasik fungsi bilangan utilasi barisan *Deret Fibonacci* tanpa memorisasi rekam tatanannya dipadulah *Dynamic Programming*?
**A2**: Sangat mengkhawatirkan. Tanpa pencatatan balok rekapan nilai *Dynamic programming iteratif memori (Memoization)*, utilasi sekuen panggilan arsitektrul Rekursi pola deret murni Fibonacci mutlak melesat mereplika bercabang anak iterasi fungsi pohon pemanggilan fungsi merusak limit tak tehingga membelah komputasi mutlaknya berganda berlipat ganda biner dengan asimtot pergerakan waktu komputator menyedihkan pada batas **Eksponensial Asimtot $\mathcal{O}(2^n)$**. Utilitas ini mengulang menghitung hitungan bilangan sub-deret fungsi kembar di persilangan sebelumnya secara memboroskan tenaga percuma mutlak jutaan siklus waktu.

---

---
id_materi: AP-010
mata_kuliah: Algoritma dan Pemrograman
topik: Manajemen Variabel Memori
sub_topik: Pengenalan Pointer dan Passing by Reference
tingkat_kesulitan: Tinggi
prasyarat: Penugasan (Assignment) Variabel dan Fungsi
---

# Pengenalan Pointer dan Passing by Reference

**Ringkasan Materi (TL;DR)**
Variabel biasa bertindak mengisolasi menghimpun angka murni muatannya (misal nilai variabel = `10`). **Pointer** adalah instrumen khusus yang menampung *nilai Alamat Memori Fisik murni rujukan lokasi sel heksadesimal RAM* pergerakan rujukan letaknya referensi variabel induknya didalam hardware (misal *value* pointer = `0x7C04A`). Konsep referensi ini menghadirkan fitur **Passing by Reference** di fungsi subrutin parametrik operasional. Di mana fungsi tidak membuang memori membengkak meng-copy data ke RAM anyar baru, melainkan lari langsung berselancar ke mesin asalnya dan menyetel parameter pengubahan utilasi induknya permanen.

**Konsep Ruang / Cara Kerja Fisiologi**
- **Pass by Value (Default Pemanggilan)**: Ketika variabel argumen `x` dilontarkan diinput via fungsi komputator. Parameter kompilernya murni sibuk menduplikasi memori RAM *fotocopy/cloning* value `x`. Apabila digubah isinya di relung fungsi tersebut di manipulasi acak-acak, variabel mutlak asli di induknya sama sekali tetap utuh tidak berdampak lecet perubahan apapun murni statis.
- **Pass by Reference (Menggunakan Pointer)**: Mengirim utus menembakkan "Alamat Alokasi Ruang Pointer" `&x` ke subfungsi. Fungsi operasional ini merombaknya lurus menabrak gerbong alamat di ROM asalnya lewat komando dereferencing `*ptr`. Semua varian perubahan dan mutasi pergantian nilainya berlaku paten memutar balik mengkudeta nilai di induk variabel tersebut absolut dimodifikasi utuh tertiban tuntas mutakhir.

**Latihan Soal & Pembahasan (Format Q&A)**

**Q1**: Simak pseudo program bahasa rendah C-like pemanggil manipulasi ini:
```cpp
void tukar_angka(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```
Kenapa mutlak diutilitaskan penorehan simbol bintang pointer `*` (dereference) dan peluncur referensi letak memori utuh parameter *Pass by Reference*, bila tugas fungsinya sekeder merajut pemutar balikan parameter `(swap)` variabel asalnya? 
**A1**: Agar perlakuan modifikasi utiliti *Swap pertukaran rotasional mutasi bilangannya* itu secara paten merembes langsung meruntuhkan memanipulasi ke lokasi sel tatanan kordinasi memori orisinil asli induk variabel di luar relung scope fungsi subrutin *tukar_angka* tersebut murni permanen. Semisal nekat meluncurkannya di perbatasan tatanan regulasi murni utilasi biasa *Pass By Value* memori, mesin compiler sebatas me-*swap* tiruan bayangan fotocopy *dummy variables* yang hancur dipangkas ketika rujukan limit fungsionalnya ditutup kompilator, meninggalkan nilai gubahan angka utuh induk di *main()* stagnan gagal berotasi tak termanipulasi sedikitpun.

**Q2**: Apakah peruntungan keuntungan signifikansi komputasi terbesar memakai jembatan rute *Pointer memori Reference* saat mem-passing argumen variabel Array Data Struktur komputasi raksasa bernilai ribuan entitas data ke serapan parameter sebuah utilitas fungsi?
**A2**: Penghematan dan proteksi rasio ruang efisiensi siklus Asimtotik Memori Limitasi *(Space Complexity)* luar bias irit dan waktu komputasional murni tercepat performa utilitas. Tanpa asis pointer referensi pemanggilan, CPU diwajibkan menyalin mengekstrak menduplikasikan utuh beribu gerbong struktur raksasa ke ruang variabel parameter memory blok iteratif baru di tatanan blok *Call Stack variable*, yang fatal memakan ribuan milisekon $\mathcal{O}(n)$ duplikasi limit serta meludeskan kepingan limit ketersediaan sisa *Memori*. Dengan mendelegasikan lintasan rel Pointer, fungsi cuma menyedot suplai mentransfer nilai konstan ringan tatanan "1 nilai tunggal hexadesimal titik gerbong rute alamat memory *head* awalan array referensinya" ke sub fungsinya dalam perbatasan sekon presisi $\mathcal{O}(1)$ utilitas waktu dan memori statis ringan terangkul seketika mantap utuh.
---
