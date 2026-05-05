class Hero:
    # Constructor: Dieksekusi secara otomatis ketika objek Hero baru diinstansiasi
    def __init__(self, name, hp, attack_power):
        self.name = name          # Atribut nama hero
        self.hp = hp              # Atribut health point (nyawa) hero
        self.attack_power = attack_power  # Atribut kekuatan serangan hero

    # Method untuk menampilkan informasi lengkap hero ke konsol
    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")


# ============================================================
# MAIN PROGRAM - Latihan 1: Membuat Class Hero
# ============================================================

# Instansiasi objek Hero (Tugas Analisis 1: modifikasi atribut setelah dibuat)
hero1 = Hero("Layla", 100, 15)
hero1.hp = 500      # Memodifikasi atribut hp secara langsung dari luar class
print(hero1.hp)     # Menampilkan nilai hp setelah dimodifikasi

hero2 = Hero("Zilong", 120, 20)

# Memanggil method info() pada masing-masing objek
hero1.info()
hero2.info()