class Sinif():
    __gizli = "Gizli"

#Burada __gizli adlı bir gizli sınıf niteliği tanımladık. Bu değişkenin yalnızca baş tarafında iki adet alt çizgi olduğuna, ancak uç tarafında alt çizgi bulunmadığına dikkat edin. İşte Python’da baş tarafında yukarıdaki gibi iki adet alt çizgi olan, ancak uç tarafında alt çizgi bulunmayan (veya yalnızca tek bir alt çizgi bulunan) bütün öğeler birer gizli üyedir. Dışarıya kapalı olan bu gizli üyelere, normal yöntemleri kullanarak sınıf dışından erişemezsiniz.




    def ornek_metodu(self):
        print(self.__gizli)
        print("Örnek Metodu")

    
    @classmethod
    def sinif_metodu(cls):
        print("Sınıf Metodu")

    @staticmethod
    def statik_metod():
        print("statik metod")


#TEST##################################TEST#######################################

# sinif.Sınıf.__gizli

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: type object 'Sınıf' has no attribute '__gizli'

"""
Bir üyenin gizli olabilmesi için başında en az iki adet, ucunda da en fazla bir adet alt çizgi bulunmalıdır. Yani şunlar birer gizli üyedir:

__gizli = 'gizli'
__gizli_ = 'gizli'
__gizli_üye = 'gizli'
__gizli_üye_ = 'gizli'

"""

"""
Burada önemli bir noktaya dikkatinizi çekmek istiyorum: Gizli üyeler yalnızca sınıf dışına kapalıdır. Bu üyelere sınıf içinden rahatlıkla erişebiliriz. Mesela yukarıdaki örnekte bu durumu görüyorsunuz. __gizli adlı değişkene örnek_metodu() içinden normal bir şekilde erişebiliyoruz:

def örnek_metodu(self):
    print(self.__gizli)
    print('örnek metodu')

"""

"""
import sinif
s = sinif.Sınıf()
s.örnek_metodu()

'gizli'
'örnek metodu'

"""