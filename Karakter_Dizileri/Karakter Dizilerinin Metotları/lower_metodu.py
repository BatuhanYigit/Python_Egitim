# -*- coding: utf-8 -*-

kisi = input("Aradığınız kişinin ismini giriniz : ")

kisi = kisi.replace("I","ı").replace("İ","i").lower() # türkçe karakterleri düzgün bir şekilde küçültemediği için bu komutu kullandık

if(kisi == "batuhan yiğit"):
    print("email : batuhan.yigit")
    print("telephones : 123123")
    print("address : istanbul")
elif(kisi == "ahmet uçarkuş"):
    print("email : ahmet.ucarkus")
    print("telephones : 4324324324")
    print("address : Ankara")
elif(kisi == "mertcan elik"):
    print("email : mert.elik")
    print("telephones : 45345345435")
    print("address : İzmir")
else:
    print("Böyle bir kişi yok")