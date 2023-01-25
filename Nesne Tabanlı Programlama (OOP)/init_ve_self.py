# class Calisan():
#     def __init__(self):
#         self.kabiliyetleri = []
#         print(self.kabiliyetleri)


# ahmet = Calisan()

# print(ahmet.kabiliyetleri)

class Calisan():
    kabiliyetleri = ["Sınıf Niteliği"]

    def __init__(self):
        self.kabiliyetleri = ["Örnek Niteliği"]


#örnek niteliğine erişmek için
#örnek adını kullanıyoruz

ahmet = Calisan()

print(ahmet.kabiliyetleri)


#sınıf niteliğine erişmek için
#sınıf adını kullanıyoruz

print(Calisan.kabiliyetleri)