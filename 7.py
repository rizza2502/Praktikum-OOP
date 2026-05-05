from abc import ABC, abstractmethod


# ============================================================
# PILAR 1 - ABSTRACTION: Kerangka Dasar BarangElektronik
# Abstract class ini tidak dapat diinstansiasi secara langsung;
# hanya berfungsi sebagai kontrak bagi semua class turunan
# ============================================================
class BarangElektronik(ABC):
    def __init__(self, nama, stok, harga_dasar):
        self.nama = nama
        # PILAR 2 - ENCAPSULATION: Atribut sensitif dibuat private
        # agar tidak dapat diakses atau dimanipulasi langsung dari luar class
        self.__stok = 0
        self.__harga_dasar = harga_dasar

        # Inisialisasi stok melalui setter agar validasi langsung berjalan sejak awal
        self.set_stok(stok)

    # GETTER: Cara resmi untuk membaca nilai stok dari luar class
    def get_stok(self):
        return self.__stok

    # GETTER: Cara resmi untuk membaca nilai harga dasar dari luar class
    def get_harga_dasar(self):
        return self.__harga_dasar

    # SETTER: Mengubah nilai stok disertai validasi; stok tidak boleh bernilai negatif
    def set_stok(self, jumlah):
        if jumlah >= 0:
            self.__stok = jumlah
            return True
        else:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False

    # Abstract method wajib diimplementasikan oleh setiap class turunan
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# ============================================================
# PILAR 3 - INHERITANCE: Class Laptop mewarisi BarangElektronik
# ============================================================
class Laptop(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, processor):
        super().__init__(nama, stok, harga_dasar)  # Memanggil constructor parent
        self.processor = processor  # Atribut tambahan khusus Laptop
        self.pajak = 0.10           # Tarif pajak Laptop: 10%

    # PILAR 4 - POLYMORPHISM: Override tampilkan_detail() versi Laptop
    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"Harga Dasar: Rp {self.get_harga_dasar():,.0f} | Pajak(10%): Rp {self.get_harga_dasar() * self.pajak:,.0f}")

    # Override hitung_harga_total() dengan perhitungan pajak khusus Laptop
    def hitung_harga_total(self, jumlah):
        harga_plus_pajak = self.get_harga_dasar() * (1 + self.pajak)
        return harga_plus_pajak * jumlah


# ============================================================
# PILAR 3 - INHERITANCE: Class Smartphone mewarisi BarangElektronik
# ============================================================
class Smartphone(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, kamera):
        super().__init__(nama, stok, harga_dasar)  # Memanggil constructor parent
        self.kamera = kamera  # Atribut tambahan khusus Smartphone
        self.pajak = 0.05     # Tarif pajak Smartphone: 5%

    # PILAR 4 - POLYMORPHISM: Override tampilkan_detail() versi Smartphone
    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"Harga Dasar: Rp {self.get_harga_dasar():,.0f} | Pajak(5%): Rp {self.get_harga_dasar() * self.pajak:,.0f}")

    # Override hitung_harga_total() dengan perhitungan pajak khusus Smartphone
    def hitung_harga_total(self, jumlah):
        harga_plus_pajak = self.get_harga_dasar() * (1 + self.pajak)
        return harga_plus_pajak * jumlah


# ============================================================
# FITUR KERANJANG BELANJA - Fungsi di luar class (Polymorphism)
# Menerima list campuran objek Laptop dan Smartphone,
# lalu memproses transaksi dan menghitung total tagihan secara otomatis
# ============================================================
def proses_transaksi(daftar_belanja):
    print("\n--- STRUK TRANSAKSI ---")
    total_tagihan = 0
    for i, item in enumerate(daftar_belanja, 1):
        produk = item['produk']
        qty = item['jumlah']

        # Validasi ketersediaan stok sebelum memproses transaksi
        if produk.get_stok() >= qty:
            subtotal = produk.hitung_harga_total(qty)
            print(f"{i}. ", end="")
            produk.tampilkan_detail()  # Polymorphism: perilaku berbeda sesuai tipe produk
            print(f"Beli: {qty} unit | Subtotal: Rp {subtotal:,.0f}")

            # Mengurangi stok produk sesuai jumlah yang dibeli
            produk.set_stok(produk.get_stok() - qty)
            total_tagihan += subtotal
        else:
            print(f"{i}. Stok {produk.nama} tidak mencukupi!")

    print("-" * 30)
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,.0f}")
    print("-" * 30)


# ============================================================
# MAIN PROGRAM - Tugas Proyek Integrasi: Sistem Inventaris TechMaster
# Alur program mengikuti User Story yang telah ditentukan di modul
# ============================================================

print("--- SETUP DATA ---")

# Langkah 1: Admin membuat data produk
laptop_rog = Laptop("ROG Zephyrus", 10, 20000000, "Ryzen 9")
iphone_13 = Smartphone("iPhone 13", 20, 15000000, "12MP")

print(f"Berhasil menambahkan stok {laptop_rog.nama}: {laptop_rog.get_stok()} unit.")

# Langkah 2: Admin mencoba input stok negatif; program wajib menolak dan memberi peringatan
iphone_13.set_stok(-5)
print(f"Berhasil menambahkan stok {iphone_13.nama}: {iphone_13.get_stok()} unit.")

# Langkah 3 & 4: User melakukan pembelian; program menampilkan struk lengkap beserta pajak
keranjang = [
    {"produk": laptop_rog, "jumlah": 3},
    {"produk": iphone_13, "jumlah": 1}
]

proses_transaksi(keranjang)