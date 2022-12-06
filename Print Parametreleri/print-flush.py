#Flush parametresi kullandığımız zaman dosyayı kapatmasak bile anlık olarak verilere dosyaya yazar örnek olarak aşağıda ki kodu inceleyebilirsiniz.

f= open("flush.txt", "w")

print("Merhaba Dünya", file=f, flush=True)