# -*- coding: utf-8 -*-

kisi = input("Aradığınız kişinin ismini giriniz : ")

kisi = kisi.replace("I","ı").replace("İ","i").lower() # türkçe karakterleri düzgün bir şekilde küçültemediği için bu komutu kullandık

if(kisi == "batuhan yiğit"):
    print("email : batuhan.yigit@tga.gov.tr")
    print("telephones : 05523875997")
    print("address : istanbul")
elif(kisi == "ahmet uçarkuş"):
    print("email : ahmet.ucarkus@tga.gov.tr")
    print("telephones : 05523875997")
    print("address : Ankara")
elif(kisi == "mertcan elik"):
    print("email : mert.elik@tga.gov.tr")
    print("telephones : 05523875997")
    print("address : İzmir")
else:
    print("Böyle bir kişi yok")