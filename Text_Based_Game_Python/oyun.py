import ayarlar
can = 100

def story():
    yol = input("Önünde iki yol var sağdan mı gitmek istersin soldan mı ? (sağ/sol) : ")
    if(yol == "sağ"):
        ayarlar.slowPrint("Sağdan Gittin ve kafana taş düştü maalesef öldün")
    elif(yol == "sol"):
        ayarlar.slowPrint("Soldan gittin")
        sol_dan = input("Karşında kurt var ne yapacaksın ? (Kaç/Dur) : ")
        if(sol_dan == "kaç"):
            story_aralik = input("Kaçtın Ve Bir Aralık Gördün Ne Yapacaksın ? (Gir/Girme)")
            if(story_aralik == ("gir")):
                can - 10
                ayarlar.slowPrint("İçeri Girdin Fakat ayağını kırdın {}".format(can))
            elif(story_aralik == ("girme")):
                ayarlar.slowPrint("Yoluna Devam ediyorsun")
                story2()


        elif(sol_dan == "dur"):
            ayarlar.slowPrint("Durdun Ve Maalesef kurt sana saldırdı ve öldün!! ")
def story2():
    ayarlar.slowPrint("""
    *************************************************
                    İkinci Bölüm
    *************************************************
    
    
    """)
            

    
