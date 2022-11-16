import ayarlar
saglik = 100
para = 0
def saglik_kontrol():
    if(saglik == 0):
        print("\nÖldünüz Lütfen Yeniden Başlayınız {}".format(saglik))
    elif(saglik < 50):
        print("\nCanınız Azalıyor...{}".format(saglik))
    else:
        print("\nCan durumunuz : {}".format(saglik))
def para_kontrol():
    print("Banka Durumu {}".format(para))

def story():
    global saglik
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
    ayarlar.slowPrint("""
    *************************************************
                    İkinci Bölüm
    *************************************************
    
    
    \n""")
    ayarlar.slowPrint("\nÖnüne bir yabancı çıktı seninle tanışmak istiyor (tanış \ tanışma) : ")
    story2_tanisma = input()
    if(story2_tanisma == "tanış"):
        print("Yabancı Sana Para Verdi")
        para = para + 100
        para_kontrol()
    elif(story2_tanisma == "tanışma"):
        ayarlar.slowPrint("Yabancı Yüzüne bakmadığın için sinirlendi kafana tahta fırlattı : ")
        saglik = saglik - 10
        saglik_kontrol()
    

            

    
