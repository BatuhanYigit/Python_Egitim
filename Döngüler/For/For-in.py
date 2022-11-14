#Burada sayılar adlı değişkenin her bir öğesini sayı olarak adlandırdıktan sonra, 
# int() fonksiyonu yardımıyla bu öğeleri tek tek sayıya çevirdik ve her bir öğeyi 2 ile çarptık.

sayilar = "123456789"

for sayi in sayilar:
    print(int(sayi)*2)