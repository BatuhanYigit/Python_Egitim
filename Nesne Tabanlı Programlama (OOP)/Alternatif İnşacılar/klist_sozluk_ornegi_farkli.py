liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
         ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
         ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

def bul(deger,sira):
    return[li for li in liste if deger == li[sira]]

def sorgula(olcut=None, deger=None):

    d = {'isbn' : bul(deger, 0),
         'yazar': bul(deger, 1),
         'eser' : bul(deger, 2),
         'yayinevi': bul(deger, 3),               }


    for oge in d.get(olcut,liste):
        print(*oge,sep=', ')