

def user_login(username,password):

    if(username == "user" and password == "pass"):
        print("Hoşgeldiniz!")
        msg = True
        return msg 

    
    else:
        print("Girilemedi")
        msg = False

def userinfo():
    username = "user"
    password = "pass"
    return username,password
username,password = userinfo()
user_login(username,password)

def test_user_int():
    username,password = userinfo()
    assert type(username) == type("")
    assert type(password) == type("")

def test_login():
    username,password = userinfo()
    assert user_login(username,password) == True


def test_login_false():
    username,password = user_login()
    assert user_login(username,password) != False
