# ============================================================
# Parent Class - Hero
# ============================================================
class Hero:
    def __init__(self, nama):
        self.nama = nama

    # Tugas Analisis 6 - Poin 2: method serang() di parent sengaja dihapus
    # untuk mensimulasikan error saat child class tidak mengimplementasikan method sendiri
    # def serang(self):
    #     print("Hero menyerang dengan tangan kosong.")


# ============================================================
# Child Classes - Masing-masing mengimplementasikan method serang() versinya sendiri
# ============================================================
class Mage(Hero):
    # Override: perilaku serang khusus role Mage
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")

class Archer(Hero):
    # Tugas Analisis 6 - Poin 2: nama method diubah menjadi tembak_panah()
    # sehingga Archer tidak memiliki method serang() dan akan memicu AttributeError
    def tembak_panah(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")

class Fighter(Hero):
    # Override: perilaku serang khusus role Fighter
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")

class Healer(Hero):
    # Tugas Analisis 6 - Poin 1: Healer ditambahkan tanpa mengubah blok looping
    # Ini membuktikan skalabilitas Polymorphism; karakter baru cukup didaftarkan ke list
    def serang(self):
        print(f"{self.nama} (Healer) tidak menyerang, tapi menyembuhkan teman!")


# ============================================================
# MAIN PROGRAM - Latihan 6: Polymorphism (Fleksibilitas Interaksi)
# ============================================================
pasukan = [
    Mage("Eudora"),
    Archer("Miya"),   # Objek ini akan memicu AttributeError karena tidak punya method serang()
    Fighter("Zilong"),
    Healer("Estes")
]

print("--- PERANG DIMULAI ---")

for pahlawan in pasukan:
    # Satu perintah serang() berlaku untuk semua tipe hero (Polymorphism),
    # namun program akan crash saat mencapai Archer karena method-nya berbeda nama
    pahlawan.serang()