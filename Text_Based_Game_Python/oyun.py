def story():
    yol = input("Önünde iki yol var sağdan mı gitmek istersin soldan mı ? (sağ/sol) : ")
    if(yol == "sağ"):
        print("Sağdan Gittin ve kafana taş düştü maalesef öldün")
    elif(yol == "sol"):
        print("Soldan gittin")
        sol_dan = input("Karşında kurt var ne yapacaksın ? (Kaç/Dur) : ")
        if(sol_dan == "Kaç"):
            print("Kaçtın!!!")
        elif(sol_dan == "Dur"):
            print("Durdun")

    
