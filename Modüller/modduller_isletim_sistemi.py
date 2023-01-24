import os

#Posix - Linux/GNU Ve Macos
#NT - Windows

print(os.name)

if os.name != "nt":
    print("Kusura bakmayın bu program windows a özel bir programdır")

else:
    print("Hoş geldiniz")