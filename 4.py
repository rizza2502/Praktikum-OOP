class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        # Enkapsulasi: atribut __hp bersifat private,
        # tidak dapat diakses atau dimodifikasi langsung dari luar class
        self.__hp = hp_awal

    # GETTER: satu-satunya cara resmi untuk membaca nilai HP dari luar class
    def get_hp(self):
        return self.__hp

    # SETTER: satu-satunya cara resmi untuk mengubah nilai HP, dilengkapi validasi
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0           # HP tidak diperbolehkan bernilai negatif
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000.")
            self.__hp = 1000        # Mencegah manipulasi HP melebihi batas wajar
        else:
            self.__hp = nilai_baru  # Nilai valid, langsung diperbarui

    def diserang(self, damage):
        # Menggunakan getter dan setter secara konsisten meskipun berada di dalam class
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# ============================================================
# MAIN PROGRAM - Latihan 4: Enkapsulasi (Mengamankan Data HP)
# ============================================================
hero1 = Hero("Layla", 100)

# Tugas Analisis 4 - Poin 1: Demonstrasi Name Mangling Python
# Python memperbolehkan akses paksa ke atribut private melalui sintaks _NamaClass__atribut,
# namun praktik ini melanggar prinsip enkapsulasi dan tidak dianjurkan
print(f"Mencoba akses paksa: {hero1._Hero__hp}")

# Tugas Analisis 4 - Poin 2: Menguji validasi pada Setter
# Setter mencegah HP bernilai negatif; nilai akan dikunci ke 0
hero1.set_hp(-100)
print(hero1.get_hp())