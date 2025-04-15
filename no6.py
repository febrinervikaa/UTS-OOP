class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

    def setor_tunai(self, jumlah):
        self.saldo += jumlah
        print(f"Setor Rp{jumlah} telah berhasil dilakukan. Saldo: Rp{self.saldo}")

    def tarik_tunai(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi.")
        else:
            self.saldo -= jumlah
            print(f"Tarik Rp{jumlah} telah berhasil dilakukan. Saldo: Rp{self.saldo}")

    def transfer(self, penerima, jumlah):
        if jumlah > self.saldo:
            print("Saldo Anda tidak mencukupi untuk transfer.")
        else:
            self.saldo -= jumlah
            penerima.saldo += jumlah
            print(f"Transfer Rp{jumlah} dari {self.no_rekening} ke {penerima.no_rekening} telah berhasil dilakukan.")

class Nasabah(Rekening):
   def tampilkan_data(self):
        print(f"Nama Nasabah: {self.nama}")
        print(f"No. Rekening: {self.no_rekening}")
        print(f"Saldo: Rp{self.saldo:,.2f}")
        print()

def main():
    nasabah1 = Nasabah("Budi", 5555, 500000)
    nasabah2 = Nasabah("Wati", 6666, 2000000)

    print("Sebelum Transaksi:")
    nasabah1.tampilkan_data()
    nasabah2.tampilkan_data()

    nasabah1.setor_tunai(1000000)
    nasabah2.tarik_tunai(1000000)
    nasabah1.transfer(nasabah2, 500000)

    print("\nSetelah Transaksi:")
    nasabah1.tampilkan_data()
    nasabah2.tampilkan_data()

if __name__ == "__main__":
    main()