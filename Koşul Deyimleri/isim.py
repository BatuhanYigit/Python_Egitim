giris = input("Adın Nedir ? : ")

if(len(giris) <4):
    print("{} ismin kısaymış".format(giris))
elif(len(giris) < 6):
    print("{} İsmin biraz uzunmuş".format(giris))
else:
    print("{} Adın çok uzunmuş".format(giris))