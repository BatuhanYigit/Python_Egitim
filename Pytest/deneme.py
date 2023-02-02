def user_login():
    username = input("User :")
    password = input("Pass : ")

    if(username == "user" and password == "pass"):
        print("Hoşgeldiniz!")
        msg = True
        return msg 

    
    else:
        print("Girilemedi")
        msg = False

user_login()
