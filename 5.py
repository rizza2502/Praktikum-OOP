from abc import ABC, abstractmethod


# ============================================================
# BAGIAN 1: ABSTRACT CLASS / INTERFACE - GameUnit
# Berfungsi sebagai kontrak (blueprint) yang mewajibkan semua
# class turunan untuk mengimplementasikan method yang terdaftar
# ============================================================
class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass  # Implementasi diserahkan sepenuhnya ke class konkret

    @abstractmethod
    def info(self):
        pass  # Implementasi diserahkan sepenuhnya ke class konkret


# ============================================================
# BAGIAN 2: CLASS KONKRET - Implementasi Wajib dari GameUnit
# ============================================================

class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    # Implementasi wajib method serang() versi Hero
    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    # Implementasi wajib method info() versi Hero
    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    # Implementasi wajib method serang() versi Monster
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    # Implementasi wajib method info() versi Monster
    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# ============================================================
# BAGIAN 3: UJI COBA
# Tugas Analisis 5 - Poin 2: baris berikut akan memicu TypeError
# karena abstract class tidak dapat diinstansiasi secara langsung
# ============================================================

unit = GameUnit()  # ERROR: abstract class tidak bisa dijadikan objek

h = Hero("Alucard")
m = Monster("Serigala")

h.info()
h.serang("Serigala")

print("-" * 20)

m.info()
m.serang("Alucard")