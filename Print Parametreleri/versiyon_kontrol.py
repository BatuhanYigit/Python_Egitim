import sys

#sys.version_info
# ÇIKTISI---
#sys.version_info(major=3, minor=10, micro=5, releaselevel='final', serial=0)

#major, kullanılan Python serisinin ana sürüm numarasını; minor ise alt sürüm numarasını verir.
#  Çıktıda bir de micro adlı bir değer var. Bu da kullanılan Python serisinin en alt sürüm numarasını verir.

#Örnek Kullanımlar 
#sys.version_info.major major versiyonunu iletir
#sys.version_info.minor minor versiyonunu iletir
#sys.version_info.micro micro versiyonunu iletir


#sys.version
#ÇIKTISI ----
#3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]

#Örnek Uygulama
import sys

_2x_metni = """
Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde Python'ın
3.x sürümlerinden biri kurulu olmalı."""

_3x_metni = "Programa hoşgeldiniz."

if sys.version_info.major < 3:
    print(_2x_metni)
else:
    print(_3x_metni)

#Burada kullanılan Python serisinin 3.x’ten düşük olduğu durumları sorguladık.
#  Peki aynı serinin farklı sürümlerini denetlemek istersek ne yapacağız? Mesela Python’ın 3.2 sürümünü sorgulamak istersek nasıl bir kod kullanacağız?
#Bunun için şöyle bir şey yazabiliriz:

#if sys.version_info.major == 3 and sys.version_info.minor == 2:

#Gördüğünüz gibi burada version_info değişkeninin hem major hem de minor parametrelerini kullandık. 
# Ayrıca hem ana sürüm, hem de alt sürüm için belli bir koşul talep ettiğimizden ötürü and adlı Bool işlecinden de yararlandık.
#  Çünkü koşulun gerçekleşmesi, ana sürümün 3 ve alt sürümün 2 olmasına bağlı.

#Yukarıdaki işlem için version değişkenini de kullanabilirdik. Dikkatlice bakın:

#if "3.2" in sys.version:



