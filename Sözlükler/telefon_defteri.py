telefon_defteri = {
"batuhan yiğit":"1111111",
"mertcan elik":"2222222",
"alparslan":"33333",
}

kisi = input("İsim Giriniz : ")

if kisi in telefon_defteri:
    cevap = "{} adlı kişinin telefon numarası: {}"
    print(cevap.format(kisi,telefon_defteri[kisi]))

else:
    print("Aradığınız kişiyi bulamadık")