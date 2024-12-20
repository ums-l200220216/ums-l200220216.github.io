class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.spp_terbayar = False
        self.mata_kuliah = {}

    def bayar_spp(self):
        print(f"{self.nama} sedang membayar SPP...")
        self.spp_terbayar = True
        print("SPP berhasil dibayar!")

    def ambil_mata_kuliah(self, nama_mk):
        if not self.spp_terbayar:
            print("Anda harus membayar SPP terlebih dahulu!")
            return
        if nama_mk in self.mata_kuliah:
            print(f"Mata kuliah {nama_mk} sudah diambil.")
        else:
            self.mata_kuliah[nama_mk] = None
            print(f"Mata kuliah {nama_mk} berhasil diambil.")

    def kerjakan_tugas(self, nama_mk):
        if nama_mk not in self.mata_kuliah:
            print(f"Anda belum mengambil mata kuliah {nama_mk}!")
            return
        print(f"{self.nama} sedang mengerjakan tugas untuk {nama_mk}...")

    def ikut_ujian(self, nama_mk):
        if nama_mk not in self.mata_kuliah:
            print(f"Anda belum mengambil mata kuliah {nama_mk}!")
            return
        print(f"{self.nama} sedang mengikuti ujian untuk {nama_mk}...")
        # Simulasi nilai akhir
        from random import randint
        self.mata_kuliah[nama_mk] = randint(50, 100)
        print(f"Ujian selesai! Nilai untuk {nama_mk} sedang diproses.")

    def cek_nilai(self):
        print("Nilai akhir mata kuliah:")
        for mk, nilai in self.mata_kuliah.items():
            status = "Lulus" if nilai >= 60 else "Tidak Lulus"
            print(f"- {mk}: {nilai} ({status})")

# Simulasi Proses
mahasiswa = Mahasiswa("Athaya Fajar", "L200220216")

mahasiswa.bayar_spp()
mahasiswa.ambil_mata_kuliah("Pemrograman")
mahasiswa.ambil_mata_kuliah("Struktur Data")

mahasiswa.kerjakan_tugas("Pemrograman")
mahasiswa.kerjakan_tugas("Struktur Data")

mahasiswa.ikut_ujian("Pemrograman")
mahasiswa.ikut_ujian("Struktur Data")

mahasiswa.cek_nilai()
