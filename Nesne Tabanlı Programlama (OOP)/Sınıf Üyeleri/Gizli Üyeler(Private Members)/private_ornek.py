class Calisan():
    __personel = [] #personel olan üyeyi __personel olarak değiştirdik ve gizli üye yaptık
    
    
    """
    Aynı şekilde personel listesini görüntülemek için de doğrudan personel listesine erişmeye çalışmayacağız. Yani şöyle bir şey yazmayacağız:

    Çalışan.personel
    Bunun yerine, bu iş için özel olarak tasarladığımız personeli_görüntüle() fonksiyonunu kullanacağız:

    Çalışan.personeli_görüntüle()
    İşte yukarıdaki kodlarda yer alan personel listesinin usulsüz bir şekilde kullanılmasını önlemek amacıyla bu listeyi bir gizli üye haline getirebilirsiniz:
    """

    def __init__(self,isim):
        self.isim = isim
        self.kabiliyetler = []
        self.__personele_ekle()
    
    @classmethod
    def personel_sayisini_goruntule(cls):
        print(len(cls.__personel))

    def __personele_ekle(self): 
        self.__personel.append(self.isim)
        print("{} adlı kişi personele eklendi".format(self.isim))

    @classmethod
    def personeli_goruntule(cls):
        print("Personel Listesi : ")
        for kisi in cls.__personel:
            print(kisi)
    
    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetler.append(kabiliyet)

    def kabiliyetleri_goruntule(self):
        print("Kabiliyetler : ")
        for kabiliyet in self.kabiliyetler:
            print(kabiliyet)


"""
Çalışan.__personel

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Çalışan' has no attribute '__personel'

"""


"""
Şimdi, bu sınıf içindeki gizli üyeye erişeceğiz.

Dikkatlice bakın:

import sinif
s = sinif.Sınıf()
s._Sınıf__gizli

'gizli'
Ne kadar da tuhaf, değil mi?

İşte Python, siz bir sınıf üyesini __gizli şeklinde tanımladığınızda, bu öğe üzerinde şu işlemleri gerçekleştirir:

Öncelikle değişkenin baş tarafına bir alt çizgi ekler:

_
Daha sonra, bu alt çizginin sağ tarafına bu gizli üyeyi barındıran sınıfın adını iliştirir:

_Sınıf
Son olarak da gizli üyeyi sınıf adının sağ tarafına yapıştırır:

_Sınıf__gizli
Dolayısıyla _Sınıf__gizli kodunu kullanarak, __gizli adlı üyeye sınıf dışından erişebilirsiniz.


"""