from abc import ABC, abstractmethod

class MetodePembayaran(ABC):
    def __init__(self, nama):
        self.nama = nama
    
    @abstractmethod
    def bayar(self, jumlah):
        pass
    
    @abstractmethod
    def refund(self, jumlah):
        pass

class ShopeePay(MetodePembayaran):
    def bayar(self, jumlah):
        print(f"Pembayaran sebesar Rp{jumlah} menggunakan ShopeePay berhasil.")
    
    def refund(self, jumlah):
        print(f"Refund sebesar Rp{jumlah} ke ShopeePay berhasil.")

class OVO(MetodePembayaran):
    def bayar(self, jumlah):
        print(f"Pembayaran sebesar Rp{jumlah} menggunakan OVO berhasil.")
    
    def refund(self, jumlah):
        print(f"Refund sebesar Rp{jumlah} ke OVO berhasil.")

class GoPay(MetodePembayaran):
    def bayar(self, jumlah):
        print(f"Pembayaran sebesar Rp{jumlah} menggunakan GoPay berhasil.")
    
    def refund(self, jumlah):
        print(f"Refund sebesar Rp{jumlah} ke GoPay berhasil.")

class KartuKredit(MetodePembayaran):
    def bayar(self, jumlah):
        print(f"Pembayaran sebesar Rp{jumlah} menggunakan Kartu Kredit berhasil.")
    
    def refund(self, jumlah):
        print(f"Refund sebesar Rp{jumlah} ke Kartu Kredit berhasil.")

shopeepay = ShopeePay("ShopeePay")
ovo = OVO("OVO")
gopay = GoPay("GoPay")
kartukredit = KartuKredit("Kartu Kredit")

metode_list = [shopeepay, ovo, gopay, kartukredit]

for metode in metode_list:
    metode.bayar(100000)
    metode.refund(50000)
    print("-")