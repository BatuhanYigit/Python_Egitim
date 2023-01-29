import tkinter as tk

pencere = tk.Tk()

def cikis():
    etiket["text"] = "Elveda Zalim Hayat"
    dugme["text"] = "Bekleyin..."
    dugme["state"] = "disabled"
    pencere.after(2000,pencere.destroy)

etiket = tk.Label(text="Merhaba DÜnya")
etiket.pack()

dugme = tk.Button(text="ÇIk",command=cikis)
dugme.pack()

pencere.protocol("WM_DELETE_WINDOW",cikis)

pencere.mainloop()