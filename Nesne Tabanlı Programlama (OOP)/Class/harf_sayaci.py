class HarfSayaci:
    def __init__(self):
        self.sesliharfler = 'aeıioöuü'
        self.sessizharfler = 'bcçdfgğhjklmnprsştvyz'
        self.sayac_sesli = 0
        self.sayac_sessiz = 0


    def kelime_sor(self):
        return input("Bir Kelime Girin")

    def seslidir(self, harf):
        return harf in self.sesliharfler
    
    def sessizdir(self, harf):
        return harf in self.sessizharfler

    def arttır(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac_sesli += 1
            if self.sessizdir(harf):
                self.sayac_sessiz += 1
        return (self.sayac_sessiz, self.sayac_sesli)
    
    def ekrana_bas(self):
        sesli,sessiz = self.arttır()
        mesaj = "{} Kelimesinde {} sesli {} sessiz harf vardır".format(self.kelime,sesli,sessiz)

    def calistir(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()
    
if __name__ == "__main__":
    sayac = HarfSayaci()
    sayac.calistir()