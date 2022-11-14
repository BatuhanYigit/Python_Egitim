#Aksi belirtilmediği sürece kullanıcıya
#aşağıdaki soruyu sormaya devam et!
while True:
    soru = input("Nasılsınız, iyi misiniz?")

    #Eğer kullanıcı 'q' tuşuna basarsa...
    if soru == "q":
        break #döngüyü kır ve programdan çık.


###############################2. örnek##############################
tekrar = 1

while tekrar <= 3:
    print("tekrar: ", tekrar)
    tekrar += 1
    input("Nasılsınız, iyi misiniz?")
    print("bool değeri: ", bool(tekrar <= 3))