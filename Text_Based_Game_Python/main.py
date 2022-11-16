import oyun
import ayarlar
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

ayarlar.slowPrint("Hoşgeldiniz........")

name = input("İsminiz Nedir ? : ")

print("Hoş geldin",name)




def secima():
    secim = input("Oyuna Devam Etmek İstiyor musun {}  (evet/hayır): ".format(name))
    if(secim == "evet"):
        print("Hadi Başlayalım....")

        oyun.story()

    elif(secim == "hayır"):
        print("Bir dahakine görüşmek üzere :(")

    else:
        secim()
        print("Lütfen evet veya hayır seçeneğini seçiniz....")



