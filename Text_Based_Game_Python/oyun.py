import ayarlar
saglik = 100
para = 0
envanter = []
def envanter_kontrol():
    ayarlar.slowPrint("""
    *************************************************
                        Envanter
                        {}
    *************************************************
    
    
    \n""".format(envanter))

def saglik_kontrol():
    if(saglik == 0):
        ayarlar.slowPrint("\nÖldünüz Lütfen Yeniden Başlayınız {}".format(saglik))
    elif(saglik < 50):
        ayarlar.slowPrint("\nCanınız Azalıyor...{}".format(saglik))
    else:
        ayarlar.slowPrint("\nCan durumunuz : {}".format(saglik))
def para_kontrol():
    print("Banka Durumu {}".format(para))

def story():
    global saglik
    global para
    ayarlar.slowPrint("Önünde iki yol var sağdan mı gitmek istersin soldan mı ? (sağ/sol) : ")
    yol = input()
    if(yol == "sağ"):
        ayarlar.slowPrint("Sağdan Gittin ve kafana taş düştü maalesef öldün")
    elif(yol == "sol"):
        ayarlar.slowPrint("Soldan gittin\n")
        ayarlar.slowPrint("Karşında kurt var ne yapacaksın ? (Kaç/Dur) : ")
        sol_dan = input()
        if(sol_dan == "kaç"):
            ayarlar.slowPrint("Kaçtın Ve Bir Aralık Gördün Ne Yapacaksın ? (Gir/Girme) : ")
            story_aralik = input()
            
            if(story_aralik == ("gir")):
                saglik = saglik - 10
                ayarlar.slowPrint("İçeri Girdin Fakat ayağını kırdın")
                saglik_kontrol()
                story2()
                
            elif(story_aralik == ("girme")):
                ayarlar.slowPrint("Yoluna Devam ediyorsun")
                story2()


        elif(sol_dan == "dur"):
            ayarlar.slowPrint("Durdun Ve Maalesef kurt sana saldırdı ve öldün!! ")
def story2():
    global para
    global saglik
    global envanter
    ayarlar.slowPrint("""
    *************************************************
                    İkinci Bölüm
    *************************************************
    
    
    \n""")
    ayarlar.slowPrint("\nÖnüne bir yabancı çıktı seninle tanışmak istiyor (tanış \ tanışma) : ")
    story2_tanisma = input()
    while True:
        if(story2_tanisma == "tanış"):
            print("Yabancı Sana Para Verdi")
            para = para + 100
            para_kontrol()
            ayarlar.slowPrint("\n Bir Çiftlik gördün ve elma aldın. ")
            envanter.append("Elma")
            envanter_kontrol()
            ayarlar.slowPrint("\n Kırık Bir Araba Buldun Tamir Etmek İster Misin ? (Evet/Hayır) : ")
            story2_araba = input()
            if(story2_araba == "evet"):
                ayarlar.slowPrint("Arabayı Tamir Ettin Fakat Kolunu Yaraldın...")
                saglik = saglik - 10
                saglik_kontrol()
                story3()
            elif(story2_araba == "hayır"):
                ayarlar.slowPrint("Yerde sağlık kiti buldun...")
                envanter.append("Sağlık Çantası")
                envanter_kontrol()
                ayarlar.slowPrint("Sağlık Çantasını Kullanmak İstiyor Musun? (Evet/Hayır) : ")
                story2_saglikcantasi = input()
                if(story2_saglikcantasi == "evet"):
                    ayarlar.slowPrint("Sağlık Çantasını Kullandın")
                    envanter.remove("Sağlık Çantası")
                    envanter_kontrol()
                    saglik = saglik + 10
                    saglik_kontrol()
                    story3()
                elif(story2_saglikcantasi == "hayır"):
                    ayarlar.slowPrint("Sağlık Çantasını Kullanmadın")
                    envanter_kontrol()
                    saglik_kontrol()
                    story3()

            
            


        elif(story2_tanisma == "tanışma"):
            ayarlar.slowPrint("Yabancı Yüzüne bakmadığın için sinirlendi kafana tahta fırlattı : ")
            saglik = saglik - 10
            saglik_kontrol()
            story3()

        else:
            ayarlar.slowPrint("Lütfen Evet Veya Hayır Giriniz....")

def story3():
    ayarlar.slowPrint("""\n
    *************************************************
                    Üçüncü Bölüm
    *************************************************
    
    \n""")
    envanter_kontrol()
    para_kontrol()

    ayarlar.slowPrint("Koşarak uzaklaşıyorsun ve ayağın kanamaya başladı")
    

    
    

            

    
