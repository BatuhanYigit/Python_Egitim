import ayarlar
saglik = 100

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
                ayarlar.slowPrint("İçeri Girdin Fakat ayağını kırdın {}".format(saglik))
                
                
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
            

    
