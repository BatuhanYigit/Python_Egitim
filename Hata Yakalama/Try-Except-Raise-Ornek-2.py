tr_karakterler = "şçğüöıİ"

parola = input("Parolanızı Giriniz : ")
for i in parola:
    if i in tr_karakterler:
        raise TypeError("Parolanızda Türkçe Karakter Kullanamazsınız!!!")
    else:
        pass
print("Parola Geçerli...")