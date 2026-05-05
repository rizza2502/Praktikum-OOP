# ============================================================
# STEP 1: Class Induk (Parent Class) - Hero
# ============================================================
class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


# ============================================================
# STEP 2: Class Anak (Child Class) - Mage
# Mage mewarisi seluruh atribut dan method dari class Hero
# ============================================================
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        # Tugas Analisis 3: baris super() di bawah ini sengaja dinonaktifkan
        # untuk mengamati error yang terjadi saat atribut parent tidak diinisialisasi
        # super().__init__(name, hp, attack_power)
        self.mana = mana  # Atribut tambahan khusus role Mage

    # Override method info() dari parent untuk menampilkan informasi spesifik Mage
    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    # Skill eksklusif Mage yang tidak dimiliki class Hero biasa
    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20                      # Konsumsi mana setelah skill digunakan
            lawan.diserang(self.attack_power * 2)  # Fireball memberikan damage 2x lipat
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")


# ============================================================
# MAIN PROGRAM - Latihan 3: Pewarisan (Inheritance)
# ============================================================
print("\n--- Update Class Hero ---")

# Instansiasi objek Mage (Eudora) dan Hero biasa (Balmond)
eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()                    # Menampilkan info Mage dengan format yang di-override
eudora.serang(balmond)           # Serangan dasar yang diwarisi dari class Hero
print("-" * 30)
eudora.skill_fireball(balmond)   # Skill eksklusif milik class Mage