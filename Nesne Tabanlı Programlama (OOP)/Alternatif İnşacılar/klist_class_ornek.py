class Sorgu():
    def __init__(self):
        self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                      ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                      ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]
    
    def bul(self, deger, sira):
        return [li for li in self.liste if deger == li[sira]]
    
    def sorgula(self, olcut = None, deger = None):
        d = {'isbn'     : self.bul(deger, 0),
             'yazar'    : self.bul(deger, 1),
             'eser'     : self.bul(deger, 2),
             'yayınevi' : self.bul(deger, 3)}

        for oge in d.get(olcut, self.liste):
                print(*oge, sep=', ')