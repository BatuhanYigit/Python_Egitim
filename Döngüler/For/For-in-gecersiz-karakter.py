tr_harfler = "şçöğüİı"
parola = input("Parola belirleyiniz : ")
for karakter in parola:
    if(karakter in tr_harfler):
        print("Şifrenizde türkçe karakter bulunmaktadır.")
    else:
        print("Şifreniz belirlendi ....")
        