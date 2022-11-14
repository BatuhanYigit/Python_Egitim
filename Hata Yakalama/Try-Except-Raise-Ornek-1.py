#Bazen, yazdığımız bir programda, kullanıcının yaptığı bir işlem normal şartlar altında hata vermeyecek olsa bile biz ona ‘Python tarzı’ bir hata mesajı göstermek isteyebiliriz. 
# Böyle bir durumda ihtiyacımız olan şey Python’ın bize sunduğu raise adlı deyimdir.
# Bu deyim yardımıyla duruma özgü hata mesajları üretebiliriz. Bir örnek verelim:

bolunen = int(input("Bölünecek Sayıyı Giriniz : "))
if bolunen == 23:
    raise Exception("Bu Programda 23 sayısını görmek istemiyorum !!! :D")
bolen = int(input("Bolen Sayısını Giriniz : "))
print(bolunen/bolen)