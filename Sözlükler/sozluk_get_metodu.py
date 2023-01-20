# Gördüğünüz gibi, burada çok basit bir metot yardımıyla bütün dertlerimizi hallettik. Sözlüklerin get() adlı metodu, 
# parantez içinde iki adet argüman alır. Birinci argüman sorgulamak istediğimiz sözlük öğesidir.
#  İkinci argüman ise bu öğenin sözlükte bulunmadığı durumda kullanıcıya hangi mesajın gösterileceğini belirtir. 
#  Buna göre, yukarıda yaptığımız şey, önce “sorgu” değişkenini sözlükte aramak, 
#  eğer bu öğe sözlükte bulunamıyorsa da kullanıcıya, 
# “Bu kelime veritabanımızda yoktur!” cümlesini göstermekten ibarettir

ing_sozluk = {"dil": "language", "bilgisayar": "computer", "masa": "table"}

sorgu = input("Lütfen Anlamını Öğrenmek istediğiniz kelimeyi giriniz : ")

print(ing_sozluk.get(sorgu, "Bu kelime sözlüğümüzde yoktur.")) # Get metodu ile eğer veri tabanında bu kelime yoksa kullanıcıya bu şekilde uyarı verecektir.
