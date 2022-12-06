notunuz = int(input("Notunuzu Giriniz : "))

if(notunuz > 100 or notunuz < 0):
    print("Hatalı Bir Not Girdiniz.")
elif(notunuz >= 90 and notunuz <= 100):
    print("A Aldınız.")
elif(notunuz >= 80 and notunuz <= 89):
    print("B Aldınız.")
elif(notunuz >= 70 and notunuz <= 79):
    print("C Aldınız.")
elif(notunuz >= 60 and notunuz <= 69):
    print("D Aldınız.")
elif(notunuz >= 0 and notunuz <= 59):
    print("F Aldınız.")