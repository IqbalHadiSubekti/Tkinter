from tkinter import*

my_app=Tk(className='tabung')

L1 = Label(my_app, text='Program Hitung Bangun Ruang Tabung', font=('Times New Roman', 24))
L1.grid(row=0, column=0, columnspan=3, sticky=W)
L2 = Label(my_app, text='Jari-jari: ')
L2.grid(row=3, column=0, sticky=W)

E2 = Entry(my_app)
E2.grid(row=3, column=1, sticky=W)

L3 = Label(my_app, text='Tinggi: ')
L3.grid(row=4, column=0, sticky=W)
E3 = Entry(my_app)
E3.grid(row=4, column=1, sticky=W)

L4 = Label(my_app, text='Luas= ')
L4.grid(row=6, column=1, sticky=W)
luas = StringVar()

L5 = Label(my_app, textvariable=luas)
L5.grid(row=6, column=2, sticky=W)

def alas():
    phi=3.14
    luas.set(2*phi*int(E2.get())**2)

def selimut():
    phi=3.14
    luas.set(phi*int(E2.get())*int(E3.get()))

def permukaan():
    phi=3.14
    luas.set(2*phi*int(E2.get())*int(E3.get()))

def volume():
    phi=3.14
    luas.set(phi*int(E2.get())**2*int(E3.get()))

B1 = Button(my_app, text='Luas Alas', command=alas)
B1.grid(row=5, column=0, sticky=W)
B2 = Button(my_app, text='Luas Selimut', command=selimut)
B2.grid(row=5, column=1, sticky=W)
B3 = Button(my_app, text='Luas Permukaan', command=permukaan)
B3.grid(row=5, column=2, sticky=W)
B4 = Button(my_app, text='Luas Volume', command=volume)
B4.grid(row=5, column=3, sticky=W)

my_app.mainloop()