#sep ifadesi, İngilizcede separator (ayırıcı, ayraç) kelimesinin kısaltmasıdır. Dolayısıyla print() fonksiyonundaki bu sep parametresi,
#  ekrana basılacak öğeler arasına hangi karakterin yerleştirileceğini gösterir. Bu parametrenin öntanımlı değeri bir adet boşluk karakteridir (” “). 
# Yani siz bu özel parametrenin değerini başka bir şeyle değiştirmezseniz, Python bu parametrenin değerini bir adet boşluk karakteri olarak alacak ve 
# ekrana basılacak öğeleri birbirinden birer boşlukla ayıracaktır.
#  Ancak eğer biz istersek bu sep parametresinin değerini değiştirebiliriz. 
# Böylece Python, karakter dizilerini birleştirirken araya boşluk değil, bizim istediğimiz başka bir karakteri yerleştirebilir.

print("http://","www.", "batuhan.", "com")

# Çıktısı http:// www. batuhan. com

print("Batuhan", "Yiğit", sep="-")

# Çıktısı Batuhan-Yiğit

print("Birinci satır", "İkinci Satır", "Üçüncü Satır")

# Çıktısı Birinci satır İkinci Satır Üçüncü Satır

print("Birinci satır", "İkinci Satır", "Üçüncü Satır", sep="\n")

#Çıktısı 
# Birinci satır
# İkinci Satır
# Üçüncü Satır



