import time
import random
import sys


class Oyuncu():
    def __init__(self,isim,can=5,enerji=100):
        self.isim = isim
        self.darbe = 0
        self.can = can
        self.enerji = enerji
    
    def mevcut_durum_goruntule(self):
        print('Darbe : ',self.darbe)
        print('Can : ',self.can)
        print('Enerji : ',self.enerji)
    
    def saldir(self, rakip):
        print("Bir saldırı gerçekleştirdiniz")
        print("Saldırı Sürüyor. Bekleyiniz")

        for i in range(10):
            time.sleep(.3)
            print('.',end='',flush=True)

            sonuc = self.saldiri_sonucu_hesapla()

            if sonuc == 0:
                print("\n Sonuç : Kazanan Taraf YOk")

            if sonuc == 1:
                print("\n Sonuç : Rakibinizi darbelediniz")
                self.darbele(rakip)

            if sonuc == 2:
                print("\nSonuç : Rakibinizden darbe aldınız")
                rakip.darbele(self)
    
    def saldiri_sonucu_hesapla(self):
        return random.randint(0,2)

    def kac(self):
        print('Kaçılıyor....')
        for i in range(10):
            time.sleep(.3)
            print('\n', flush=True)

        print('Rakibiniz sizi yakaladı')
    
    def darbele(self,darbelenen):
        darbelenen.darbe += 1
        darbelenen.enerji -= 1
        if (darbelenen.darbe %5)== 0:
            darbelenen.can -= 1
        
        if darbelenen.can < 1:
            darbelenen.enerji = 0
            print("Oyunu {} kazandı!".format(self.isim))
            self.oyundan_cik()

    def oyundan_cik(self):
        print('Çıkılıyor....')
        sys.exit()

##################################

# Oyuncular
siz = Oyuncu('Batuhan')
rakip = Oyuncu('Mehmet')


# Oyun Başlangıcı

while True:
    print('Şuanda Rakibinizle Karşı karşıyasınız.',
           'Yapmak İstediğiniz Hamle: ',
           'Saldır : s',
           'Kaç : k',
           'Çık : q', sep='\n')
    
    hamle = input('\n> ')
    if hamle == 's':
        siz.saldir(rakip)

        print('Rakibinizin Durumu')
        rakip.mevcut_durum_goruntule()

        print('Sizin Durumunuz')
        siz.mevcut_durum_goruntule()

    if hamle == 'k':
        siz.kac()

    if hamle == 'q':
        siz.oyundan_cik()