import oyun

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

print("Hoşgeldiniz........")

name = input("İsminiz Nedir ? : ")

print("Hoş geldin",name)


secim = input("Oyuna Devam Etmek İstiyor musun {}  (yes/no): ".format(name))

if(secim == "yes"):
    print("Hadi Başlayalım....")

    oyun.veyso()

elif(secim == "no"):
    print("Bir dahakine görüşmek üzere :(")

else:
    print("Lütfen yes veya no seçeneğini seçiniz....")