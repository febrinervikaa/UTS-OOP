class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

class Nasabah(Rekening):
    def tampilkan_data(self):
        print(f"Nama Nasabah: {self.nama}")
        print(f"No. Rekening: {self.no_rekening}")
        print(f"Saldo: Rp{self.saldo:,.2f}")
        print()

def main():
    nasabah1 = Nasabah("Budi", 5555, 500000)
    nasabah2 = Nasabah("Wati", 6666, 2000000)

    # Menampilkan data nasabah
    nasabah1.tampilkan_data()
    nasabah2.tampilkan_data()
    
if __name__ == "__main__":
    main()
