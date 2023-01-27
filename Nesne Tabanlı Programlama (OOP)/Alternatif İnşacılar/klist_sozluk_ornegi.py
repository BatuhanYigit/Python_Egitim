liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
         ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
         ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

def sorgula(olcut=None, deger=None):

    d = {'isbn' : [li for li in liste if deger == li[0]],
         'yazar': [li for li in liste if deger == li[1]],
         'eser' : [li for li in liste if deger == li[2]],
         'yayinevi': [li for li in liste if deger == li[3]],               }


    for oge in d.get(olcut,liste):
        print(*oge,sep=', ')