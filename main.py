# Importações:

from __future__ import with_statement
import sys, os
from enum import Flag
from tkinter import *
from turtle import width

from click import command
from yaml import compose_all

# Cores:

cor1 = '#1d1d1b' # Preto / background for window
cor2 = '#2a2a27' # Cinza / background for frames
cor3 = '#2f2f2c' # Cinza / background for buttons
cor4 = '#ffffff' # branco / foreground caracteres
cor5 = '#2f2b10' # Tom de VVerde / background for height
cor6 = '#00a09f' # Azul / background for bottom
cor7 = '#373734' # Cinza / activebackground
cor8 = '#262624' # Preto

# Definindo a Janela:

janela = Tk()
janela.title('Simulador de Média')
janela.config(bg = cor1)

# Definindo as dimensões da janela:

altura = 650
largura = 700

largura_da_tela = janela.winfo_screenwidth()
altura_da_tela = janela.winfo_screenheight()

posx = largura_da_tela/2 - largura/2
posy = altura_da_tela/2 - altura/2

janela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
janela.resizable(False, False)

# Definindo o ícone da janela:
code_directory = sys.path[0]
janela.iconphoto(True, PhotoImage(file = os.path.join(code_directory, 'icon.png')))

# Criando os Frames:

frame_aviso_de_simulado = Frame(janela, width = 600, height= 50, bg = cor5)
frame_aviso_de_simulado.place(x = 50, y = 100)

frame_av1 = Frame(janela, width = 290, height = 100, bg = cor2)
frame_av1.place(x = 50, y = 180)

frame_av2 = Frame(janela, width = 290, height = 100, bg = cor2)
frame_av2.place(x = 360, y = 180)

frame_av3 = Frame(janela, width = 290, height = 100, bg = cor2)
frame_av3.place(x = 50, y = 300)

frame_av4 = Frame(janela, width = 290, height = 100, bg = cor2)
frame_av4.place(x = 360, y = 300)

frame_calculo = Frame(janela, width= 600, height = 150, bg = cor6)
frame_calculo.place(x = 50, y = 420)

# Criando as Labels:

title = Label(janela, text = 'Simular Média', bg = cor1, fg = cor4, font = 'Modern 16 bold')
title.place(x = 50, y = 30)


aviso = Label(frame_aviso_de_simulado, text = 'Nessa simulção não está sendo considerado o bônus do simulado.', bg = cor5, fg = cor4, font = 'Modern 9')
aviso.place(x = 15, y = 13)


label_av1 = Label(frame_av1, text = 'Avaliação I - Individual', bg = cor2, fg = cor4, font = 'Modern 9')
label_av1.place(x = 5, y = 5)


label_av2 = Label(frame_av2, text = 'Avaliação II - Individual', bg = cor2, fg = cor4, font = 'Modern 9')
label_av2.place(x = 5, y = 5)


label_av3 = Label(frame_av3, text = 'Avaliação Final (Discursiva) - Individual', bg = cor2, fg = cor4, font = 'Modern 9')
label_av3.place(x = 5, y = 5)


label_av4 = Label(frame_av4, text = 'Avaliação Final (Objetiva) - Individual', bg = cor2, fg = cor4, font = 'Modern 9')
label_av4.place(x = 5, y = 5)

label_média_calculada = Label(frame_calculo, text = 'Média Calculada', bg = cor6, fg = cor4, font = 'Modern 9')
label_média_calculada.place(x = 10, y = 10)

label_aviso_calculo = Label(frame_calculo, text = 'Abaixo a média calculada a partir das notas informadas para as avaliações.', bg = cor6, fg = cor4, font = 'Modern 9')
label_aviso_calculo.place(x = 10, y = 35)

label_formula = Label(frame_calculo, text = '( ( - * 1,5 ) + ( - * 1,5 ) + ( - * 4 ) + ( - * 3 ) ) / 10 =', bg = cor6, fg = cor4, font = 'Modern 9')
label_formula.place(x = 10, y = 125)

# Criando as Entries:

av1 = 0
entry_av1 = Entry(frame_av1, justify = CENTER, width = 13, bg = cor2, fg = cor4, highlightbackground = cor2, highlightcolor = cor2, relief = FLAT, font = 'Modern 10')
entry_av1.insert(0, float(av1))
entry_av1.pack()
entry_av1.place(x = 90, y = 57)

av2 = 0
entry_av2 = Entry(frame_av2, justify = CENTER, width = 13, bg = cor2, fg = cor4, highlightbackground = cor2, highlightcolor = cor2, relief = FLAT, font = 'Modern 10')
entry_av2.insert(0, float(av2))
entry_av2.pack()
entry_av2.place(x = 90, y = 57)

av3 = 0
entry_av3 = Entry(frame_av3, justify = CENTER, width = 13, bg = cor2, fg = cor4, highlightbackground = cor2, highlightcolor = cor2, relief = FLAT, font = 'Modern 10')
entry_av3.insert(0, float(av3))
entry_av3.pack()
entry_av3.place(x = 90, y = 57)

av4 = 0
entry_av4 = Entry(frame_av4, justify = CENTER, width = 13, bg = cor2, fg = cor4, highlightbackground = cor2, highlightcolor = cor2, relief = FLAT, font = 'Modern 10')
entry_av4.insert(0, float(av4))
entry_av4.pack()
entry_av4.place(x = 90, y = 57)

# Adicionando funções as Entries:

def calcular():
    av1 = float(entry_av1.get())
    av2 = float(entry_av2.get())
    av3 = float(entry_av3.get())
    av4 = float(entry_av4.get())
    soma = ((av1 * 1.5) + (av2 * 1.5) + (av3 * 4) + (av4 * 3)) / 10
    resultado.set(f'{soma:.2f}')

resultado = StringVar()

resultado_label = Label(frame_calculo, textvariable = resultado, bg = cor6, fg = cor4, font = 'Modern 20 bold')
resultado_label.place(x = 270, y = 65)

# Função para limpar a tela:

def limpar():
    resultado.set('')

# Funções de soma/subtração:

def somar_av1():
    global av1
    av1 = av1 + 1
    if av1 == 11:
        av1 = 10
    entry_av1.delete(0, END)
    entry_av1.insert(0, float(av1))

def subtrair_av1():
    global av1
    av1 = av1 - 1
    if av1 == -1:
        av1 = 0
    entry_av1.delete(0, END)
    entry_av1.insert(0, float(av1))

def somar_av2():
    global av2
    av2 = av2 + 1
    if av2 == 11:
        av2 = 10
    entry_av2.delete(0, END)
    entry_av2.insert(0, float(av2))

def subtrair_av2():
    global av2
    av2 = av2 - 1
    if av2 == -1:
        av2 = 0
    entry_av2.delete(0, END)
    entry_av2.insert(0, float(av2))

def somar_av3():
    global av3
    av3 = av3 + 1
    if av3 == 11:
        av3 = 10
    entry_av3.delete(0, END)
    entry_av3.insert(0, float(av3))

def subtrair_av3():
    global av3
    av3 = av3 - 1
    if av3 == -1:
        av3 = 0
    entry_av3.delete(0, END)
    entry_av3.insert(0, float(av3))

def somar_av4():
    global av4
    av4 = av4 + 1
    if av4 == 11:
        av4 = 10
    entry_av4.delete(0, END)
    entry_av4.insert(0, float(av4))

def subtrair_av4():
    global av4
    av4 = av4 - 1
    if av4 == -1:
        av4 = 0
    entry_av4.delete(0, END)
    entry_av4.insert(0, float(av4))

# Criando os Buttons:

botao_calcular = Button(janela, text = 'Calcular', width = 6, height = 0, bg = cor6, fg = cor4, relief = FLAT,
                        activebackground = cor6, activeforeground = cor4, highlightbackground = cor6, highlightcolor = cor6, 
                        command = calcular)
botao_calcular.place(x = 490, y = 600)

botao_limpar = Button(janela, text = 'Limpar', width = 6, height = 0, bg = cor1, fg = cor4, relief = FLAT,
                      activebackground = cor8, activeforeground = cor4, highlightbackground = cor1, highlightcolor = cor8, 
                      command = limpar)
botao_limpar.place(x = 575, y = 600)

botao_mais_av1 = Button(frame_av1, text = '+', width = 1, height = 0, bg = cor3, fg = cor4, relief = FLAT, 
                        activebackground = cor7, activeforeground = cor4, highlightbackground = cor3, highlightcolor = cor7, 
                        command = somar_av1)
botao_mais_av1.place(x = 200, y = 50)

botao_menos_av1 = Button(frame_av1, text = '-', width = 1, height = 0, bg = cor3, fg = cor4, relief = FLAT, 
                         activebackground = cor7, activeforeground = cor4, highlightbackground = cor3, highlightcolor = cor7, 
                         command = subtrair_av1)
botao_menos_av1.place(x = 52, y = 50)

botao_mais_av2 = Button(frame_av2, text = '+', width = 1, height = 0, bg = cor3, fg = cor4, relief = FLAT, 
                        activebackground = cor7, activeforeground = cor4, highlightbackground = cor3, highlightcolor = cor7, 
                        command = somar_av2)
botao_mais_av2.place(x = 200, y = 50)

botao_menos_av2 = Button(frame_av2, text = '-', width = 1, height = 0, bg = cor3, fg = cor4, relief = FLAT, 
                         activebackground = cor7, activeforeground = cor4, highlightbackground = cor3, highlightcolor = cor7, 
                         command = subtrair_av2)
botao_menos_av2.place(x = 52, y = 50)

botao_mais_av3 = Button(frame_av3, text = '+', width = 1, height = 0, bg = cor3, fg = cor4, relief = FLAT, 
                        activebackground = cor7, activeforeground = cor4, highlightbackground = cor3, highlightcolor = cor7, 
                        command = somar_av3)
botao_mais_av3.place(x = 200, y = 50)

botao_menos_av3 = Button(frame_av3, text = '-', width = 1, height = 0, bg = cor3, fg = cor4, relief = FLAT,
                         activebackground = cor7, activeforeground = cor4, highlightbackground = cor3, highlightcolor = cor7, 
                         command = subtrair_av3)
botao_menos_av3.place(x = 52, y = 50)

botao_mais_av4 = Button(frame_av4, text = '+', width = 1, height = 0, bg = cor3, fg = cor4, relief = FLAT,
                        activebackground = cor7, activeforeground = cor4, highlightbackground = cor3, highlightcolor = cor7, 
                        command = somar_av4)
botao_mais_av4.place(x = 200, y = 50)

botao_menos_av4 = Button(frame_av4, text = '-', width = 1, height = 0, bg = cor3, fg = cor4, relief = FLAT,
                         activebackground = cor7, activeforeground = cor4, highlightbackground = cor3, highlightcolor = cor7, 
                         command = subtrair_av4)
botao_menos_av4.place(x = 52, y = 50)




janela.mainloop()