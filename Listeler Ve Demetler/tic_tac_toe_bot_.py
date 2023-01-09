from time import sleep
import random

tahta = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]




print("\n"*15)

for i in tahta:
    print("\t".expandtabs(30),*i, end="\n"*2)

kazanma_ölçütleri = [[[0, 0], [1, 0], [2, 0]],
                     [[0, 1], [1, 1], [2, 1]],
                     [[0, 2], [1, 2], [2, 2]],
                     [[0, 0], [0, 1], [0, 2]],
                     [[1, 0], [1, 1], [1, 2]],
                     [[2, 0], [2, 1], [2, 2]],
                     [[0, 0], [1, 1], [2, 2]],
                     [[0, 2], [1, 1], [2, 0]]]

x_durumu = []
o_durumu = []

x_random = random.randint(0,3)
y_random = random.randint(0,3)


sira = 1

while True:

    if sira == 1:
        print(sira)
        sira += 1
        isaret = "X".center(3)
        print(sira)
        
        
    elif sira > 1:
        print(sira)
        sira = 0
        isaret = "O".center(3)
        
        
        
        
    

    print()
    print("İşaret : {}\n".format(isaret))
    #sleep(0.3)

    x = input("Yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
    if x == "q":
        break
    y = input("Soldan sağa [1, 2, 3]: ".ljust(30))
    if y == "q":
        break

    x = int(x)-1
    y = int(y)-1

    print("\n"*15)

    if tahta[x][y] == "___":
        tahta[x][y] = isaret
        if isaret == "X".center(3):
            x_durumu += [[x,y]]
        elif isaret == "O".center(3):
            o_durumu += [[x_random,y_random]]
        sira += 1

    else:
        print("\n orası dolu tekrar deneyiniz\n")

    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n"*2)
    
    for i in kazanma_ölçütleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]
        # print("o: ",o)
        # print("x: ",x)


        if len(o) == len(i):
            print("O Kazandı !!!!")
            quit()
        if len(x) == len(i):
            print("X Kazandı !!!!")
            quit()