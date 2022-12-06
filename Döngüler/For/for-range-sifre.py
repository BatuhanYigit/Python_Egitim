for i in range(3):
    parola = input("Şifrenizi Belirleyiniz : ")
    if not parola:
        print("Parola Boş bırakılamaz.")
    elif len(parola) in range(3, 8):
        print("Yeni Parolanız : ",parola)
        break
    elif i == 2:
        print("Parolanızı 3 kere yanlış girdiniz!!!")
    else:
        print("Parola 3 ile 8 arasında olmalı")