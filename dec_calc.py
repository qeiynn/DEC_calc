import tkinter as tk
import requests
from sys import exit
from time import perf_counter,ctime

gui = tk.Tk()
gui.title('DEC calculator')
gui.geometry('557x380+700+150')
gui.configure(bg='black')
gui.resizable(False, False)
gui.grid_rowconfigure(0, minsize=20)
gui.grid_rowconfigure(1, minsize=50)
gui.grid_rowconfigure(2, minsize=50)
gui.grid_rowconfigure(3, minsize=50)
gui.grid_rowconfigure(4, minsize=50)
gui.grid_rowconfigure(5, minsize=50)
gui.grid_rowconfigure(6, minsize=50)
gui.grid_rowconfigure(7, minsize=20)

gui.grid_columnconfigure(0, minsize=20)
gui.grid_columnconfigure(1, minsize=50)
gui.grid_columnconfigure(2, minsize=100)
gui.grid_columnconfigure(3, minsize=20)
gui.grid_columnconfigure(4, minsize=20)
gui.grid_columnconfigure(5, minsize=25)
gui.grid_columnconfigure(6, minsize=20)
gui.grid_columnconfigure(7, minsize=25)

v0 = tk.StringVar

dec_price="starting!"
sps_price="starting!"

def fdec(owned, days):
    total = owned
    for _ in range(days):
        total += total * 0.0075
    return (round(total,1))

def refresh():
    global krystalla
    krystalla = int(e2.get())
    global meres
    meres = int(e3.get())
    lbl_result.config(text = str(fdec(krystalla, meres))+" DEC")

def Price():
    a=requests.get("https://api.coingecko.com/api/v3/simple/price?ids=dark-energy-crystals%2Csplinterlands&vs_currencies=usd%2Cusd").json()
    DEC_Price.configure(text=str(a['dark-energy-crystals']['usd'])+" $")
    SPS_Price.configure(text=str(a['splinterlands']['usd'])+" $")
    gui.after(15000,Price)
    print("refreshed at {}  ".format(str(ctime())))

DEC=tk.Label(gui,text="DEC", fg='light blue', bg='black', font='helvetica 12 bold')
SPS=tk.Label(gui,text="SPS", fg='light blue', bg='black', font='helvetica 12 bold')
DEC_Price=tk.Label(gui,text=dec_price,  fg='white', bg='black', font='helvetica 12')
SPS_Price=tk.Label(gui,text=sps_price, fg='white', bg='black', font='helvetica 12')

DEC.grid(row=6,column=5)
DEC_Price.grid(row=6,column=6)
SPS.grid(row=7,column=5)
SPS_Price.grid(row=7,column=6)

Price()

lbl_main = tk.Label(gui, text="                   DEC calculator", fg='light blue', bg='black', font='helvetica 18 bold')
lbl_main.grid(column=0, row=0, columnspan=4, sticky="N")

lbl2 = tk.Label(gui, text="DEC owned      :", fg='light blue', bg='black', font='helvetica 16')
lbl2.grid(column=0, row=2, columnspan=2, sticky="W")
e2 = tk.Entry(gui, bd=2, width=10)
e2.insert(0, "10000")
e2.grid(column=2, row=2, sticky="W")

lbl3 = tk.Label(gui, text="Days to calc     :", fg='light blue', bg='black', font='helvetica 16')
lbl3.grid(column=0, row=3, columnspan=2, sticky="W")
e3 = tk.Entry(gui, bd=2, width=10)
e3.insert(0, "1")
e3.grid(column=2, row=3, sticky="W")

button_calc = tk.Button(gui, text = "calculate", font='helvetica 12', command = refresh)
button_calc.grid(column=3, row=3, columnspan=3, sticky="S")

lbl_result = tk.Label(gui, text = " ", fg='white', bg='black', font='helvetica 18 bold')
lbl_result.grid(column=1, row=4, columnspan=2, sticky="SE")


gui.mainloop()
