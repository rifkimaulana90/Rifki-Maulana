
# ==========================================
# SISTEM NILAI MAHASISWA
# Project Object-Oriented Programming
# ==========================================

# CLASS 1: Mahasiswa
class Mahasiswa:
    jumlah_mahasiswa = 0

    # Constructor
    def __init__(self, nama, nim, tugas, uts, uas):
        self.nama = nama
        self.nim = nim

        # Encapsulation dan setter
        self.nilai = (tugas, uts, uas)

        Mahasiswa.jumlah_mahasiswa += 1

    # Property
    @property
    def nilai(self):
        return self.__nilai

    # Setter
    @nilai.setter
    def nilai(self, data):
        tugas, uts, uas = data

        if all(0 <= n <= 100 for n in data):
            self.__nilai = (tugas, uts, uas)
        else:
            raise ValueError("Nilai harus antara 0-100!")

    # Instance method
    def hitung_nilai_akhir(self):
        tugas, uts, uas = self.__nilai

        return (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

    # Static method
    @staticmethod
    def tentukan_grade(nilai):
        if nilai >= 85:
            return "A"
        elif nilai >= 75:
            return "B"
        elif nilai >= 65:
            return "C"
        elif nilai >= 50:
            return "D"
        else:
            return "E"

    # Instance method
    def status_kelulusan(self):
        if self.hitung_nilai_akhir() >= 65:
            return "LULUS"
        return "TIDAK LULUS"

    # Class method
    @classmethod
    def total_mahasiswa(cls):
        return cls.jumlah_mahasiswa

    # Method menampilkan data
    def tampilkan_data(self):
        tugas, uts, uas = self.nilai
        akhir = self.hitung_nilai_akhir()

        print("-" * 40)
        print(f"Nama        : {self.nama}")
        print(f"NIM         : {self.nim}")
        print(f"Nilai Tugas : {tugas}")
        print(f"Nilai UTS   : {uts}")
        print(f"Nilai UAS   : {uas}")
        print(f"Nilai Akhir : {akhir:.2f}")
        print(f"Grade       : {self.tentukan_grade(akhir)}")
        print(f"Status      : {self.status_kelulusan()}")


# CLASS 2: SistemNilai
class SistemNilai:

    # Constructor
    def __init__(self):
        self.daftar_mahasiswa = []

    # Method mencari mahasiswa
    def cari_mahasiswa(self, nim):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None

    # Method menambahkan mahasiswa
    def tambah_mahasiswa(self):
        print("\n=== TAMBAH MAHASISWA ===")

        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM : ")

        if self.cari_mahasiswa(nim):
            print("NIM sudah terdaftar!")
            return

        try:
            tugas = float(input("Nilai Tugas  : "))
            uts = float(input("Nilai UTS    : "))
            uas = float(input("Nilai UAS    : "))

            # Membuat object dari class Mahasiswa
            mahasiswa = Mahasiswa(nama, nim, tugas, uts, uas)

            self.daftar_mahasiswa.append(mahasiswa)

            print("\nData berhasil ditambahkan!")

        except ValueError:
            print("Masukkan nilai berupa angka 0-100!")

    # Method menampilkan seluruh mahasiswa
    def tampilkan_semua(self):
        print("\n=== DAFTAR NILAI MAHASISWA ===")

        if not self.daftar_mahasiswa:
            print("Belum ada data mahasiswa.")
            return

        for mahasiswa in self.daftar_mahasiswa:
            mahasiswa.tampilkan_data()

        print("-" * 40)
        print(f"Total mahasiswa: {Mahasiswa.total_mahasiswa()}")

    # Method mengubah nilai
    def ubah_nilai(self):
        print("\n=== UBAH NILAI MAHASISWA ===")

        nim = input("Masukkan NIM: ")
        mahasiswa = self.cari_mahasiswa(nim)

        if mahasiswa is None:
            print("Mahasiswa tidak ditemukan!")
            return

        try:
            tugas = float(input("Nilai Tugas baru: "))
            uts = float(input("Nilai UTS baru  : "))
            uas = float(input("Nilai UAS baru  : "))

            # Menggunakan property setter
            mahasiswa.nilai = (tugas, uts, uas)

            print("Nilai berhasil diperbarui!")

        except ValueError:
            print("Masukkan nilai berupa angka 0-100!")

    # Method menghapus mahasiswa
    def hapus_mahasiswa(self):
        print("\n=== HAPUS MAHASISWA ===")

        nim = input("Masukkan NIM: ")
        mahasiswa = self.cari_mahasiswa(nim)

        if mahasiswa is not None:
            self.daftar_mahasiswa.remove(mahasiswa)
            Mahasiswa.jumlah_mahasiswa -= 1

            print("Data berhasil dihapus!")
        else:
            print("Mahasiswa tidak ditemukan!")

    # Method menu utama
    def jalankan(self):
        while True:
            print("\n" + "=" * 40)
            print("       SISTEM NILAI MAHASISWA")
            print("=" * 40)
            print("1. Tambah Mahasiswa")
            print("2. Tampilkan Data Mahasiswa")
            print("3. Ubah Nilai Mahasiswa")
            print("4. Hapus Mahasiswa")
            print("5. Jumlah Mahasiswa")
            print("0. Keluar")
            print("=" * 40)

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.tambah_mahasiswa()

            elif pilihan == "2":
                self.tampilkan_semua()

            elif pilihan == "3":
                self.ubah_nilai()

            elif pilihan == "4":
                self.hapus_mahasiswa()

            elif pilihan == "5":
                print(f"Total mahasiswa: {Mahasiswa.total_mahasiswa()}")

            elif pilihan == "0":
                print("Terima kasih telah menggunakan program!")
                break

            else:
                print("Pilihan tidak valid!")


# Membuat object dari class SistemNilai
if __name__ == "__main__":
    sistem = SistemNilai()
    sistem.jalankan()
