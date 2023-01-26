class Calisan():
    personel = []
    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetler = []
        self.personele_ekle()

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele ekledni !'.format(self.isim))

    def personeli_goruntule(self):
        print('Personel Listesi: ')
        for kisi in self.personel:
            print(kisi)

    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetler.append(kabiliyet)
    
    def kabiliyetleri_goruntule(self):
        print('{} Kişinin Kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetler:
            print(kabiliyet)