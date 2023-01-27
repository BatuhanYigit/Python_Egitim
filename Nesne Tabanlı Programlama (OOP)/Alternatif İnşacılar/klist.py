liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
         ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
         ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

def sorgula(olcut=None, deger=None):
    for li in liste:
        if not olcut and not deger:
            print(*li, sep=', ')
        
        elif olcut == 'isbn':
            if deger == li[0]:
                print(*li, sep=', ')
        
        elif olcut == 'yazar':
            if deger == li[1]:
                print(*li, sep=', ')
            
        elif olcut == 'eser':
            if deger == li[2]:
                print(*li, sep=', ')

        elif olcut == 'yayınevi':
            if deger == li[3]:
                print(*li, sep=', ')