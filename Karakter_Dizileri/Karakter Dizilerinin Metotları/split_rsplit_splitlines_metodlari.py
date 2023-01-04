batuhan = "Batuhan Can Yiğit"

print(batuhan.split())

for i in batuhan.split():
    print(i)

kisaltma = input("Kıslatmasını öğrenmek istediğiniz kurum adını giriniz : ")

for i in kisaltma.split():
    print(i[0], end="")

deneme = "İstanbul, Lüleburgaz, Laleli, Hataylı,"
print(deneme)

for i in deneme:
    print(i)

for i in deneme.split("l"):
    print(i)

split_deneme = "Ankara Büyükşehir Belediyesi"

print(split_deneme.split(" "))

#>> ['Ankara', 'Büyükşehir', 'Belediyesi']

print(split_deneme.split(" ", 1)) #  1 sayısı sayesinde bölme işlemi karakter dizisi üzerine bir kez uygulandı. 

#>> ['Ankara', 'Büyükşehir Belediyesi']