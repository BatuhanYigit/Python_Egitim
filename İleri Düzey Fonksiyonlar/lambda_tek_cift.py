tam_sayi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift = list(filter(lambda x: x%2 == 0, tam_sayi))
tek =  list(filter(lambda x: x%2 != 0, tam_sayi))

print(tam_sayi)
print(cift)
print(tek)
