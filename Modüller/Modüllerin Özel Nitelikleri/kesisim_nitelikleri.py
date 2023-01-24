modüller = ['os', 'sys', 'random']

def kesişim_bul(modüller):
    kümeler = [set(dir(__import__(modül))) for modül in modüller]
    return set.intersection(*kümeler)

print(kesişim_bul(modüller))