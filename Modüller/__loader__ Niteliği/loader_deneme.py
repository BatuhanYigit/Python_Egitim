import webbrowser

yukleyici = webbrowser.__loader__
kaynak = yukleyici.get_data(webbrowser.__file__ )
print(kaynak)


"""
Burada, daha önce öğrendiğimiz __file__ niteliğini kullandığımıza dikkat edin. __loader__ niteliğinin get_data() adlı metodu, parametre olarak, sorgulayacağımız modülün dizin adresini ister. Bir modülün dizin adresini __file__ niteliği yardımıyla elde edebileceğimizi biliyoruz. Dolayısıyla da get_data() metoduna parametre olarak webbrowser.__file__ kodunu veriyoruz. Elde ettiğimiz şey ise, sorguladığımız modülün kaynak kodlarını içeren bir bayt (bytes) veri tipi oluyor.


"""


"""

_loader__, günlük olarak kullanacağımız bir araç değil. Eğer yazdığınız kodlarda bu niteliğin sunduğu olanaklara ihtiyaç duyarsanız, doğrudan bu nitelik yerine pkgutil adlı bir modülü kullanabilirsiniz.

"""