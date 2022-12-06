#Örneğin kullanıcıya bir parola belirletirken, belirlenecek parolanın 8 karakterden uzun, 3 karakterden kısa olmamasını sağlayalım:

while True:
    parola = input("Parolanızı Belirleyiniz : ")
    if not parola:
        print("Şifreniz boş olamaz.")
    elif len(parola)>8 or len(parola)<3:
        print("Parola 8 karakterden uzun 3 karakterden kısa olamaz")
    else:
        print("Parolanız oluşturulmuştur..")
        break