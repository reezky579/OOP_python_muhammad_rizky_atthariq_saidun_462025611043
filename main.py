class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama  = nama
        self.warna = warna
        self.umur  = umur

kucing1 = Kucing("Mochi", "putih", 2)
kucing2 = Kucing("Tompel", "hitam", 5)

print(kucing1.nama)   # Mochi
print(kucing1.warna)  # putih
print(kucing1.umur)   # 2

print(kucing2.nama)   # Tompel
print(kucing2.warna)  # hitam
print(kucing2.umur)   # 5