"""
Burada fonk1 kapsayıcı (enclosing) veya dış fonksiyonumuz, fonk2 ise içerideki (nested) yani iç fonksiyonumuz oluyor. 
İç içe fonksiyonlarımızın ilginç özellikleri olduğunu söyleyebiliriz. 
Ayrıca bu fonksiyonları iyice anlamak, ileride üreteçleri (diğer bir adı ile yürüyücüleri) de daha iyi anlamamızı sağlayacaktır.
"""

def yazici():
    def yaz(mesaj):
        print(mesaj)
    return yaz


"""



"""