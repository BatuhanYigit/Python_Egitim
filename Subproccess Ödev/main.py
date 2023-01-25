import subprocess as sb


# islem = input("Dosya uzantısı giriniz : ")

uzanti = input("Uzantıyı Giriniz (png, py) : ")

cmd = sb.Popen(["cd /home/batuhan/Desktop; ls *.{}".format(uzanti)],shell=True,stdout=sb.PIPE,text=True)

print(cmd.stdout.read())


