import tkinter

pencere = tkinter.Tk()
# pencere.geometry('200X70')

etiket = tkinter.Label(text="Merhaba Dünya")
etiket.pack()

dugme = tkinter.Button(text="Tamam",command=pencere.destroy)
dugme.pack()

pencere.mainloop()