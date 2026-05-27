class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def __str__(self):
        return f'kucing: {self.nama} | umur: {self.umur} tahun'

    def __eq__(self, other):
        return self.umur == other.umur

    def __lt__(self, other):
        return self.umur < other.umur

    def __gt__(self, other):
        return self.umur > other.umur


kucing1 = Kucing('Mochi', 2)
kucing2 = Kucing('Tompel', 5)
kucing3 = Kucing('Bule', 2)

print(kucing1)
print(kucing2)
print(kucing3)

print('\n ***pengujian perbandingan***')

print(f'apakah {kucing1.nama} lebih tua dari {kucing2.nama}? : {kucing1 > kucing2}')

print(f'apakah {kucing1.nama} lebih muda dari {kucing2.nama}? : {kucing1 < kucing2}')

print(f'apakah umur {kucing1.nama} sama dengan {kucing3.nama}? : {kucing1 == kucing3}')