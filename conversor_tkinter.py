from tkinter import *

def calcular():
    global resultado
    km = float(entrada_km.get())
    resultado['text'] = ('{:.2f}'.format(km/1.852))

window = Tk()
window.title('Conversor km -> nm')
window.geometry('480x100')

valor_km = Label(window, text='Insira o valor em km:')
valor_km.grid(column=0, row=0, padx=10, pady=10)

label_resultado = Label(window, text='Valor em milhas náuticas:')
label_resultado.grid(column=0, row=1, padx=10, pady=10)

entrada_km = Entry()
entrada_km.grid(column=1, row=0, padx=10, pady=10)

botao = Button(text='Calcular', command=calcular)
botao.grid(column=2, row=0, padx=10, pady=10)

resultado = Label(window, text='', font='arial', fg='red')
resultado.grid(column=1, row=1, padx=10, pady=10)

window.mainloop()