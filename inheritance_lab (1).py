class KomponenUtama:
    def __init__(self):
        print("Komponen Utama dibuat")

    def info(self):
        print("Ini adalah komponen utama sistem")

class PenggerakRoda(KomponenUtama):
    def __init__(self):
        super().__init__()
        print("Sistem Penggerak Roda dibuat")

    def aksi(self):
        print("Robot bergerak menggunakan roda")

class NavigasiOtonom(KomponenUtama):
    def __init__(self):
        super().__init__()
        print("Sistem Navigasi Otonom dibuat")

    def aksi(self):
        print("Sistem navigasi sedang memetakan jalur otomatis")


class RobotOtonom(PenggerakRoda, NavigasiOtonom):
    def __init__(self):
        super().__init__()
        print("Robot Otonom Terintegrasi dibuat")

    def info_robot(self):
        print("Ini adalah Robot Otonom hasil gabungan sistem roda dan navigasi")

# Instansiasi objek
robot = RobotOtonom()

print("\nMethod Resolution Order (MRO):")
print(RobotOtonom.__mro__)

print("\nMenjalankan method:")
robot.info()
robot.aksi()
robot.info_robot()