while(True):
    kullanıcı_adi   = input("Lütfen Kullanıcı Adınızı Giriniz : ")
    if(len(kullanıcı_adi)>40):
        print("Lütfen 40 Karakterden küçük bir kullanıcı adı giriniz! ")
    elif(len(kullanıcı_adi)<40):
        sifre = input("Lütfen Şifrenizi Giriniz : ")
        if(len(sifre)>10):
            print("Şifreniz 10 karakterden büyük olamaz.")
        elif(len(sifre)<10):
            print("Hoş geldiniz...")
    toplam = len(kullanıcı_adi) + len(sifre)
    mesaj = "Kullanıcı Adı Ve parolanızın toplam {} karakterden oluşuyor"
    print(mesaj.format(toplam))