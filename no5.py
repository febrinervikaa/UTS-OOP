class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print(f"{self.nama} melakukan setor tunai sebesar Rp{jumlah:,.2f}")

    def tarik_tunai(self, jumlah):
        if jumlah > self.saldo:
            print(f"{self.nama} gagal melakukan tarik tunai. Saldo anda tidak mencukupi.")
        else:
            self.saldo -= jumlah
            print(f"{self.nama} melakukan tarik tunai sebesar Rp{jumlah:,.2f}")

class Nasabah(Rekening):
    def tampilkan_data(self):
        print(f"Nama Nasabah: {self.nama}")
        print(f"No. Rekening: {self.no_rekening}")
        print(f"Saldo       : Rp{self.saldo:,.2f}")
        print()

def main():
    nasabah1 = Nasabah("Budi", 5555, 500000)
    nasabah2 = Nasabah("Wati", 6666, 2000000)

    print(" Sebelum Transaksi:")
    nasabah1.tampilkan_data()
    nasabah2.tampilkan_data()

    # Saat Tranksaksi
    nasabah1.setor_tunai(1000000)    
    nasabah2.tarik_tunai(1000000)    

    print("\nSetelah Transaksi:")
    nasabah1.tampilkan_data()
    nasabah2.tampilkan_data()

if __name__ == "__main__":
    main()
