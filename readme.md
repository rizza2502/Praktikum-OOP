<div align="center">

<br/>

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        P R A K T I K U M   P E M R O G R A M A N        ║
║           B E R O R I E N T A S I   O B J E K           ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

**Koding dan Kecerdasan Artificial · Fase F · Kelas XI**
*Rekayasa Perangkat Lunak — SMK Telkom Malang*

<br/>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigma-OOP-E63946?style=flat-square)
![Status](https://img.shields.io/badge/Status-Selesai-2DC653?style=flat-square)
![Modul](https://img.shields.io/badge/Modul-MGMP%20RPL-F4A261?style=flat-square)

</div>

---

<br/>

## ✦ Daftar Isi

| No | Bagian | Keterangan |
|----|--------|------------|
| 01 | [Tentang Praktikum](#-tentang-praktikum) | Gambaran umum dan tujuan |
| 02 | [Konsep Utama OOP](#-konsep-utama-oop) | Empat pilar yang dipelajari |
| 03 | [Tugas Analisis 1](#-tugas-analisis-1--class--object) | Class & Object |
| 04 | [Tugas Analisis 2](#-tugas-analisis-2--interaksi-antar-objek) | Interaksi Antar Objek |
| 05 | [Tugas Analisis 3](#-tugas-analisis-3--inheritance) | Inheritance |
| 06 | [Tugas Analisis 4](#-tugas-analisis-4--encapsulation) | Encapsulation |
| 07 | [Tugas Analisis 5](#-tugas-analisis-5--abstraction--interface) | Abstraction & Interface |
| 08 | [Tugas Analisis 6](#-tugas-analisis-6--polymorphism) | Polymorphism |
| 09 | [Proyek: TechMaster](#-proyek-integrasi--techmaster-inventory-system) | Integrasi 4 Pilar OOP |

<br/>

---

<br/>

## ✦ Tentang Praktikum

Praktikum ini berskenario pembangunan **Battle System** sebuah game RPG sebagai media belajar, yang kemudian diakhiri dengan proyek nyata berupa **Sistem Inventaris Toko Elektronik "TechMaster"**. Setiap latihan dirancang untuk mengajarkan satu konsep OOP secara bertahap, mulai dari pembuatan class sederhana hingga penerapan keempat pilarnya secara bersamaan.

Seluruh kode ditulis dalam **Python 3** dan mengikuti praktik penulisan kode yang baik sesuai panduan modul MGMP RPL.

<br/>

---

<br/>

## ✦ Konsep Utama OOP

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   INHERITANCE      →   Mewariskan fitur ke child class  │
│   ENCAPSULATION    →   Melindungi data (private)        │
│   POLYMORPHISM     →   Satu nama method, beda perilaku  │
│   ABSTRACTION      →   Kerangka dasar, detail tersembunyi│
│                                                         │
└─────────────────────────────────────────────────────────┘
```

<br/>

---

<br/>

## 〔01〕Tugas Analisis 1 — Class & Object

> *File: `1.py` · Latihan 1: Membuat Class Hero*

**Pertanyaan**
> Apa yang terjadi jika atribut `hero1.hp` diubah menjadi `500` setelah objek dibuat? Coba lakukan `print(hero1.hp)`.

**Jawaban**

Perubahan berhasil dilakukan dan nilai HP `hero1` menjadi `500`. Hal ini terjadi karena atribut yang didefinisikan secara publik di dalam `__init__` dapat dimodifikasi secara bebas dari luar class tanpa melalui proses validasi apapun. Ini menjadi titik awal mengapa konsep **Encapsulation** penting untuk dipelajari selanjutnya.

```python
hero1 = Hero("Layla", 100, 15)
hero1.hp = 500   # ✅ Berhasil — atribut publik bebas diubah
print(hero1.hp)  # Output: 500
```

**Output Program**

<div align="center">

![Output Latihan 1](dokumentasi/1.png)

*Hasil eksekusi `1.py` — Modifikasi atribut publik dari luar class*

</div>

<br/>

---

<br/>

## 〔02〕Tugas Analisis 2 — Interaksi Antar Objek

> *File: `2.py` · Latihan 2: Interaksi Antar Objek (Method)*

**Pertanyaan**
> Parameter `lawan` pada method `serang()` menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini penting?

**Jawaban**

Dengan menerima **objek utuh**, method `serang()` mendapat akses penuh ke seluruh atribut dan method yang dimiliki objek lawan — termasuk kemampuan untuk memanggil `lawan.diserang()` secara langsung. Jika hanya mengirimkan string nama, interaksi semacam ini tidak mungkin terjadi karena string tidak memiliki method maupun atribut milik class `Hero`.

```
  hero1.serang(hero2)
       │
       └──► memanggil hero2.diserang(self.attack_power)
                  │
                  └──► hero2.hp -= damage  ✅
```

**Output Program**

<div align="center">

![Output Latihan 2](dokumentasi/2.png)

*Hasil eksekusi `2.py` — Dua objek Hero saling berinteraksi*

</div>

<br/>

---

<br/>

## 〔03〕Tugas Analisis 3 — Inheritance

> *File: `3.py` · Latihan 3: Pewarisan (Inheritance)*

**Pertanyaan**
1. Error apa yang muncul saat baris `super().__init__(...)` dihapus?
2. Mengapa error menyebutkan `'Mage' object has no attribute 'name'` padahal argumen `"Eudora"` sudah dikirim?
3. Jelaskan peran `super()` dalam menghubungkan class Anak ke class Induk!

**Jawaban**

**1. Error yang muncul:**
```
AttributeError: 'Mage' object has no attribute 'name'
```

**2. Penyebab:**
Meskipun argumen `"Eudora"` sudah dikirim saat instansiasi, tanpa `super()`, constructor milik class induk (`Hero.__init__`) tidak pernah dieksekusi. Akibatnya, proses binding atribut `self.name`, `self.hp`, dan `self.attack_power` tidak terjadi untuk objek `Mage` tersebut.

**3. Peran `super()`:**
`super()` berfungsi sebagai jembatan yang memanggil constructor class induk dari dalam class anak. Ini memastikan semua atribut dasar yang didefinisikan di `Hero` ikut terinisialisasi ketika sebuah objek `Mage` dibuat, sehingga proses pewarisan berjalan sempurna.

```
Mage("Eudora", 80, 30, 100)
  │
  ├── super().__init__("Eudora", 80, 30)  ← Hero.__init__ dijalankan
  │       └── self.name = "Eudora"  ✅
  │           self.hp   = 80        ✅
  │           self.attack_power = 30 ✅
  │
  └── self.mana = 100  ✅
```

**Output Program**

<div align="center">

![Output Latihan 3](dokumentasi/3.png)

*Hasil eksekusi `3.py` — Eudora (Mage) mewarisi kemampuan Hero dan menggunakan Fireball*

</div>

<br/>

---

<br/>

## 〔04〕Tugas Analisis 4 — Encapsulation

> *File: `4.py` · Latihan 4: Enkapsulasi (Mengamankan Data HP)*

**Pertanyaan**
1. Apakah `hero1._Hero__hp` menampilkan nilai HP atau Error? Mengapa Python masih mengizinkannya?
2. Apa yang terjadi jika logika validasi di Setter dihapus lalu diisi nilai `-100`? Mengapa Setter sangat penting?

**Jawaban**

**1. Percobaan Name Mangling:**

Nilai HP **tetap muncul**. Python tidak benar-benar memblokir atribut private — melainkan hanya menyamarkan namanya melalui mekanisme ***Name Mangling*** (mengubah `__hp` menjadi `_Hero__hp` secara internal). Tujuannya adalah mencegah akses tidak sengaja, bukan pemblokiran total. Oleh karena itu, meski secara teknis masih bisa diakses, praktik ini tetap **dilarang dalam standar penulisan kode yang baik**.

**2. Konsekuensi Tanpa Validasi:**

Tanpa validasi di Setter, nilai `-100` akan tersimpan langsung sebagai HP hero, menghasilkan data yang tidak logis dalam konteks game. Setter adalah lapisan penjaga (*guard layer*) yang memastikan setiap nilai yang masuk memenuhi aturan bisnis yang telah ditetapkan.

```
Dengan Setter (✅ Aman)          Tanpa Setter (❌ Berbahaya)
─────────────────────────        ────────────────────────────
set_hp(-100)                     __hp = -100
  └── if nilai < 0:              hero.hp → -100 (data korup)
        __hp = 0  ← dikunci
hero.hp → 0
```

**Output Program**

<div align="center">

![Output Latihan 4](dokumentasi/4.png)

*Hasil eksekusi `4.py` — Demonstrasi Name Mangling dan validasi Setter*

</div>

<br/>

---

<br/>

## 〔05〕Tugas Analisis 5 — Abstraction & Interface

> *File: `5.py` · Latihan 5: Abstraction & Interface*

**Pertanyaan**
1. Hapus method `serang()` di class `Hero`. Error apa yang muncul? Apa konsekuensinya?
2. Mengapa `GameUnit()` dilarang dibuat menjadi objek? Apa gunanya jika tidak bisa diinstansiasi?

**Jawaban**

**1. Melanggar Kontrak Interface:**

```
TypeError: Can't instantiate abstract class Hero
           with abstract method serang
```

Ketika sebuah class mewarisi Abstract Class dan tidak mengimplementasikan seluruh abstract method yang "dijanjikan", Python akan **menolak class tersebut untuk diinstansiasi** sepenuhnya. Ini adalah mekanisme penegakan kontrak yang kuat — tidak ada celah untuk lupa.

**2. Fungsi Abstract Class:**

`GameUnit` tidak pernah dimaksudkan menjadi objek nyata. Ia adalah **standar desain** — memastikan bahwa siapapun yang membuat class baru (Hero, Monster, atau lainnya) wajib menyediakan method `serang()` dan `info()`. Tanpa ini, konsistensi antara berbagai class dalam sistem tidak dapat dijamin.

```
GameUnit (Abstract — ❌ tidak bisa diinstansiasi)
    │
    ├── Hero    → wajib implement serang() & info()  ✅
    └── Monster → wajib implement serang() & info()  ✅
```

**Output Program**

<div align="center">

![Output Latihan 5](dokumentasi/5.png)

*Hasil eksekusi `5.py` — Demonstrasi abstract class dan penegakan kontrak method*

</div>

<br/>

---

<br/>

## 〔06〕Tugas Analisis 6 — Polymorphism

> *File: `6.py` · Latihan 6: Polymorphism (Fleksibilitas Interaksi)*

**Pertanyaan**
1. Tambahkan class `Healer`. Apakah loop tetap berjalan tanpa modifikasi? Apa keuntungan Polymorphism untuk pengembangan jangka panjang?
2. Apa yang terjadi jika method `serang()` di `Archer` diubah namanya menjadi `tembak_panah()`?

**Jawaban**

**1. Uji Skalabilitas:**

Program tetap **berjalan sempurna** tanpa mengubah satu baris pun pada blok looping. Cukup buat class `Healer`, implementasikan method `serang()`, lalu masukkan ke dalam list `pasukan`. Inilah inti dari Polymorphism: ***Open for Extension, Closed for Modification*** — sistem terbuka untuk ditambah fitur baru tanpa merusak kode yang sudah ada.

**2. Konsistensi Penamaan:**

Program langsung **crash** dengan `AttributeError` saat iterasi mencapai objek `Archer`. Loop memanggil `.serang()` pada setiap objek tanpa peduli tipenya. Jika salah satu class menggunakan nama yang berbeda, kontrak Polymorphism dilanggar dan sistem tidak bisa beroperasi secara seragam.

```python
# ✅ Polimorfisme bekerja dengan sempurna
for pahlawan in pasukan:
    pahlawan.serang()
    # → Mage    : "Eudora menembakkan Bola Api!"
    # → Fighter : "Zilong memukul dengan pedang!"
    # → Healer  : "Estes menyembuhkan teman!"
    # → Archer  : AttributeError ❌ (nama method berbeda)
```

**Output Program**

<div align="center">

![Output Latihan 6](dokumentasi/6.png)

*Hasil eksekusi `6.py` — Satu perintah loop, respons berbeda di tiap objek*

</div>

<br/>

---

<br/>

## ✦ Proyek Integrasi — TechMaster Inventory System

> *File: `7.py` · Tugas Proyek: Sistem Manajemen Inventaris*

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║            T E C H M A S T E R   S T O R E             ║
║         Sistem Manajemen Inventaris Elektronik          ║
╚══════════════════════════════════════════════════════════╝
```

</div>

### Arsitektur Sistem

```
BarangElektronik  (Abstract Class)
├── Abstraction   → Tidak bisa diinstansiasi langsung
├── Encapsulation → __stok & __harga_dasar bersifat private
├── tampilkan_detail()    [abstract]
└── hitung_harga_total()  [abstract]
         │
         ├── Laptop (Child Class)
         │     ├── Inheritance  → Mewarisi semua dari BarangElektronik
         │     ├── Polymorphism → Pajak 10%, format detail unik
         │     └── Atribut tambahan: processor
         │
         └── Smartphone (Child Class)
               ├── Inheritance  → Mewarisi semua dari BarangElektronik
               ├── Polymorphism → Pajak 5%, format detail unik
               └── Atribut tambahan: kamera
```

### Implementasi 4 Pilar OOP

| Pilar | Implementasi dalam Proyek |
|-------|--------------------------|
| **Abstraction** | `BarangElektronik` sebagai abstract class — tidak dapat diinstansiasi, hanya bisa diwariskan |
| **Encapsulation** | `__stok` dan `__harga_dasar` bersifat private; diakses hanya via getter/setter dengan validasi |
| **Inheritance** | `Laptop` dan `Smartphone` mewarisi seluruh struktur dasar dari `BarangElektronik` |
| **Polymorphism** | Method `hitung_harga_total()` menghasilkan nilai berbeda (pajak 10% vs 5%) meski dipanggil identik |

### Alur Program (User Story)

```
1. Admin membuat data produk
        ↓
2. Admin mencoba input stok negatif → ❌ Ditolak Setter
        ↓
3. User memasukkan produk ke keranjang belanja
        ↓
4. proses_transaksi() menghitung subtotal + pajak per produk
        ↓
5. Struk total tagihan ditampilkan
```

### Contoh Output

```
--- SETUP DATA ---
Berhasil menambahkan stok ROG Zephyrus: 10 unit.
Gagal update stok iPhone 13! Stok tidak boleh negatif (-5).
Berhasil menambahkan stok iPhone 13: 20 unit.

--- STRUK TRANSAKSI ---
1. [LAPTOP] ROG Zephyrus | Proc: Ryzen 9
   Harga Dasar: Rp 20.000.000 | Pajak(10%): Rp 2.000.000
   Beli: 3 unit | Subtotal: Rp 66.000.000

2. [SMARTPHONE] iPhone 13 | Cam: 12MP
   Harga Dasar: Rp 15.000.000 | Pajak(5%): Rp 750.000
   Beli: 1 unit | Subtotal: Rp 15.750.000
------------------------------
TOTAL TAGIHAN: Rp 81.750.000
------------------------------
```

**Output Program**

<div align="center">

![Output Proyek TechMaster](dokumentasi/7.png)

*Hasil eksekusi `7.py` — Sistem inventaris TechMaster berjalan sesuai skenario*

</div>

<br/>

---

<br/>

<div align="center">

```
╔════════════════════════════════════════╗
║   Rangkuman Istilah OOP               ║
╠════════════════════════════════════════╣
║  Class         →  Cetakan / Blueprint  ║
║  Object        →  Hasil cetakan        ║
║  Inheritance   →  Mewarisi fitur       ║
║  Encapsulation →  Melindungi data      ║
║  Polymorphism  →  Satu nama, beda aksi ║
║  Abstraction   →  Kerangka tersembunyi ║
║  Interface     →  Kontrak standarisasi ║
╚════════════════════════════════════════╝
```

<br/>

*Dibuat dengan sepenuh hati · SMK Telkom Malang · 2026*
*MGMP RPL — Rekayasa Perangkat Lunak*

</div>