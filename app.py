from tkinter import *
import get
from datetime import datetime as dt

def atualizar():
    dolar = get.Dolar()
    euro = get.Euro()
    BTC = get.BTC()

    lbl_dolar.config(text=f"Dolár: R${dolar}", font=("Arial", 8))
    lbl_euro.config(text=f"Euro: R${euro}", font=("Arial", 8))
    lbl_BTC.config(text=f"Bitcoin: {BTC}", font=("Arial", 8))

    agora = dt.now().strftime("%H:%M:%S")
    lbl_hora.config(text=(f"atualizado por ultimo às {agora}"))

dolar = get.Dolar()
euro = get.Euro()
BTC = get.BTC()

janela = Tk()
janela.title("Cotações")
janela.geometry("300x150")

lbl_titulo = Label(janela, text="Cotação em tempo real", font=('Arial', 14))
lbl_titulo.pack(pady=10)

lbl_dolar = Label(janela, text=f"Dolár: R$ {dolar}", font=("Arial", 8))
lbl_dolar.pack()

lbl_euro = Label(janela, text=f"Euro: R$ {euro}", font=("Arial", 8))
lbl_euro.pack()

lbl_BTC = Label(janela, text=f"Bitcoin: R$ {BTC}", font=("Arial", 8))
lbl_BTC.pack()

lbl_hora = Label(janela, text=(""))
lbl_hora.pack()

lbl_atualizar = Button(janela, text="ATUALIZAR", font=("Arial", 10), command=atualizar)
lbl_atualizar.pack()


janela.mainloop()
