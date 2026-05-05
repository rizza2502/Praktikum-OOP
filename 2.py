class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    # Method menyerang: Objek ini (self) menyerang objek lain (lawan)
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    # Method diserang: Menerima damage
    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

# --- Inisialisasi Objek (Contoh) ---
hero1 = Hero("Layla", 100, 20)
hero2 = Hero("Zilong", 120, 15)

# --- Output Pertarungan ---
print("\n--- Pertarungan Dimulai ---")

# Layla menyerang Zilong
hero1.serang(hero2) 

print("-" * 25)

# Zilong membalas
hero2.serang(hero1)