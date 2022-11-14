#try:
#    ...bir takım işler...
#except birHata:
 #   ...hata alınınca yapılacak işlemler...
#finally:
#    ...hata olsa da olmasa da yapılması gerekenler...

#finally.. bloğunun en önemli özelliği, programın çalışması sırasında herhangi bir hata gerçekleşse de gerçekleşmese de işletilecek olmasıdır.
#  Eğer yazdığınız programda mutlaka ama mutlaka işletilmesi gereken bir kısım varsa, o kısmı finally... bloğu içine yazabilirsiniz.

#Genel olarak Python’da dosyalarla çalışabilmek için öncelikle bilgisayarda bulunan bir dosyayı okuma veya yazma kipinde açarız.
#  Dosyayı açtıktan sonra bu dosyayla ihtiyacımız olan birtakım işlemler gerçekleştiririz.
#  Dosyayla işimiz bittikten sonra ise dosyamızı mutlaka kapatmamız gerekir. 
# Ancak eğer dosya üzerinde işlem yapılırken bir hata ile karşılaşılırsa dosyamızı kapatma işlemini gerçekleştirdiğimiz bölüme hiç ulaşılamayabilir.
#  İşte finally... bloğu böyle bir durumda işimize yarayacaktır:

try:
    dosya = open("dosyaadi.txt", "r")
except IOError:
    print("Bir Hata oluştu")
finally:
    dosya.close()