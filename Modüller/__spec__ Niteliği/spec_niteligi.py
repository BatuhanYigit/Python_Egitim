
import subprocess

adi = subprocess.__spec__.name
konumu = subprocess.__spec__.origin

print("Adı : ",adi)
print("Konumu : ",konumu)








"""
__spec__ niteliği de bize modüller hakkında çeşitli bilgiler sunan birtakım araçları içinde barındırır. Mesela bir modülün ad ve konum bilgilerine ulaşmak için bu niteliği kullanabiliriz:


"""