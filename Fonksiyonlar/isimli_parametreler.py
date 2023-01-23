def kayit_olustur(**bilgiler):
    print("-"*30)

    for anahtar,deger in bilgiler.items():
        print("{:10}: {}".format(anahtar,deger))

    print("-"*30)

kayit_olustur(ad = "Batuhan", soyad = "Yiğit", sehir = "İstanbul", tel="055555555")
