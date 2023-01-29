class Sinif():
    sinif_niteligi = "Sınıf Niteliği"

    def __init__(self):
        self.ornek_niteligi = "örnek niteliği"
    
    def ornek_metodu(self):
        print("Örnek Metodu")

    @classmethod
    def sinif_metodu(cls):
        print("Sınıf Metodu")
    

    @staticmethod
    def statik_metod():
        print('Statik Metod')


"""
snf = sınıf.Sınıf()
dir(snf)

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
 '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
 'statik_metot', 'sınıf_metodu', 'sınıf_niteliği',
 'örnek_metodu', 'örnek_niteliği']


"""