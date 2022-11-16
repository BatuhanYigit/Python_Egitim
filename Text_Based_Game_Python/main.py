import oyun
import ayarlar
def secima():
    try:
        ayarlar.slowPrint("Oyuna Devam Etmek İstiyor musun {}  (evet/hayır): ".format(name))
        secim = input()
        if(secim == "evet"):
            ayarlar.slowPrint("Hadi Başlayalım....\n")

            oyun.story()

        elif(secim == "hayır"):
            ayarlar.slowPrint("Bir dahakine görüşmek üzere :(")

        else:
            secim()
            ayarlar.slowPrint("Lütfen evet veya hayır seçeneğini seçiniz....")
    except TypeError:

        secima()



print("""

   _____                         ____            
  / ____|                       / __ \           
 | |  __  __ _ _ __ ___   ___  | |  | |_ __  ___ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | | '_ \/ __|
 | |__| | (_| | | | | | |  __/ | |__| | |_) \__
  \_____|\__,_|_| |_| |_|\___|  \____/| .__/|___/
                                      | |        
                                      |_|        



""")

ayarlar.slowPrint("Hoşgeldiniz........\n")

ayarlar.slowPrint("İsminiz Nedir ? : ")
name = input()

ayarlar.slowPrint("Hoş geldin ".format(name))
secima()




