class Sinif():
    sinif_niteligi = "Sınıf Niteliği"

    def ornek_metodu(self):
        print("Ornek Metodu")
    
    @classmethod
    def sinif_metodu(cls):
        print("Sınıf Metodu")
    
    @staticmethod
    def statik_metod():
        print("Statik Metod")


"""
        
        Bu kodların sinif.py adlı bir dosya içinde yer aldığını varsayarsak şöyle bir şeyler yazabiliriz:

import sinif
s = sinif.Sınıf()
dir(s)

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
 '__hash__', '__init__', '__le__', '__lt__', '__module__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
 'statik_metot', 'sınıf_metodu', 'sınıf_niteliği', 'örnek_metodu']
Burada öncelikle kodlarımızı barındıran modülü içe aktardık. Daha sonra, içe aktardığımız modülün içindeki Sınıf() adlı sınıfımızı s örneğine atadık ve ardından dir() komutunu kullanarak, içe aktardığımız bu sınıfın içeriğini sorguladık.

Gördüğünüz gibi, içe aktardığımız sınıfın bütün öğeleri listede var. Yani biz bu sınıf içindeki bütün öğelere normal yollardan erişme imkanına sahibiz:

s.statik_metot()

'statik metot'

s.örnek_metodu()

'örnek metodu'

s.sınıf_metodu()

'sınıf metodu'

s.sınıf_niteliği

'sınıf niteliği'
İşte dir() komutunun çıktısında görünen ve normal yollardan erişebildiğimiz bütün bu öğeler birer aleni üyedir.

Yukarıda da ifade ettiğimiz gibi, program yazarken çoğu zaman yalnızca aleni üyelerle muhatap olacaksınız. Ancak bazı durumlarda, yazdığınız bir sınıftaki bütün sınıf üyelerinin dışarıya açık olmasını istemeyebilirsiniz. Eğer kodlarınızda, sınıfın yalnızca iç işleyişini ilgilendiren, bu yüzden de dışarıdan erişilmesine gerek olmadığını veya erişilirse problem çıkacağını düşündüğünüz birtakım öğeler varsa bunları dışarıya kapatarak bir ‘gizli üye’ haline getirmek isteyebilirsiniz. Peki ama nasıl?
        
        
"""