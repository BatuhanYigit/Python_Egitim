class Calisan():
    personel = []
    def __init__(self, isim):
        self.isim = isim
        self.kabiliyetler = []
        self.personele_ekle()
    @classmethod
    def personel_sayisini_goruntule(cls):
        print(len(cls.personel))

    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi !'.format(self.isim))
    @classmethod
    def personeli_goruntule(cls):
        print('Personel Listesi: ')
        for kisi in cls.personel:
            print(kisi)

    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetler.append(kabiliyet)
    
    def kabiliyetleri_goruntule(self):
        print('{} Kişinin Kabiliyetleri:'.format(self.isim))
        for kabiliyet in self.kabiliyetler:
            print(kabiliyet)