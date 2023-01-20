harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
sozluk = {}

for i in harfler:
    sozluk[i] = harfler.index(i)

print(sozluk)


for i in range(len(harfler)):
    sozluk[harfler[i]] = i

print(sozluk)

# kısa örnek üreteç
sözlük = {i: harfler.index(i) for i in harfler}

print(sözlük)

# üreteç kullanarak ismin kaç harften oluştuğunu öğrendik
isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]

sozluk_isimler = {i: len(i) for i in isimler}

print(sozluk_isimler)