class Kucing:
    def __init__(self, nama, warna, umur):
        self.nama  = nama
        self.warna = warna
        self.umur  = umur

    def tampilkan_info(self):
        return f"nama: {self.nama} warna: {self.warna} umur: {self.umur}"

    def cek_tua(self):
        if self.umur > 3:
            return f"{self.nama} termasuk kucing TUA"
        else:
            return f"{self.nama} termasuk kucing MUDA"

    @staticmethod
    def konversi_umur_ke_manusia(umur_kucing):
        return umur_kucing * 7


kucing1 = Kucing("Mochi", "putih", 2)
kucing2 = Kucing("Tompel", "hitam", 5)

print(kucing1.tampilkan_info())
print(kucing1.cek_tua())

print(kucing2.tampilkan_info())
print(kucing2.cek_tua())

print("konversi (class):", Kucing.konversi_umur_ke_manusia(2))
print("konversi (object):", kucing1.konversi_umur_ke_manusia(5)) 