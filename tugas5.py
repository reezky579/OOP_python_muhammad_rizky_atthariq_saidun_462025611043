class Kucing:
    def __init__(self, nama, kode_pemilik, berat_badan):
        self.__nama = nama
        self.__kode_pemilik = kode_pemilik
        self.__berat_badan = berat_badan

    def get_nama(self):
        return self.__nama

    def cek_berat(self, kode):
        if kode == self.__kode_pemilik:
            return f'berat {self.__nama}: {self.__berat_badan} kg'
        else:
            return f'kode salah! akses diTOLAK!'

    def kasih_makan(self, kode, jumlah):
        if kode != self.__kode_pemilik:
            return f'kode salah! gagal kasih makan'
        if self.__berat_badan + jumlah > 10:
            return f'{self.__nama} sudah terlalu gemuk, jangan dikasih makan lagi!'
        self.__berat_badan += jumlah
        return f'berhasil kasih makan! berat sekarang: {self.__berat_badan} kg'


kucing1 = Kucing('Mochi', 1010, 3.5)

print('\n nama kucing:', kucing1.get_nama())

print('\n ===pengujian cek berat badan===')

# kode benar
print(kucing1.cek_berat(1010))

# kode salah
print(kucing1.cek_berat(2020))

print('\n ===pengujian kasih makan===')

# kasih makan dengan kode benar
print(kucing1.kasih_makan(1010, 1.5))

# kasih makan dengan kode salah
print(kucing1.kasih_makan(4040, 1))