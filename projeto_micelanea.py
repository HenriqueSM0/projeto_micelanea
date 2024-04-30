# Ex 2 :

from tkinter import *
import os
from datetime import *
import time
import random

Pasta = os.path.dirname(__file__)

janela = Tk()
janela.title('Utilidades e Micelâneas')

fogueira = PhotoImage(file= Pasta + '\img' + '\\fogueira.gif')
relogio = PhotoImage(file= Pasta + '\img' + '\\relógio.gif')
dado = PhotoImage(file= Pasta +  '\img' + '\\dado.gif')
rel_00_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 00_00.gif')
rel_00_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 00_30.gif')
rel_01_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 1_00.gif')
rel_01_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 1_30.gif')
rel_02_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 2_00.gif')
rel_02_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 2_30.gif')
rel_03_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 3_00.gif')
rel_03_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 3_30.gif')
rel_04_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 4_00.gif')
rel_04_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 4_30.gif')
rel_05_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 5_00.gif')
rel_05_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 5_30.gif')
rel_06_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 6_00.gif')
rel_06_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 6_30.gif')
rel_07_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 7_00.gif')
rel_07_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 7_30.gif')
rel_08_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 8_00.gif')
rel_08_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 8_30.gif')
rel_09_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 9_00.gif')
rel_09_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 9_30.gif')
rel_10_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 10_00.gif')
rel_10_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 10_30.gif')
rel_11_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 11_00.gif')
rel_11_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 11_30.gif')
rel_12_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 12_00.gif')
rel_12_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 12_30.gif')
rel_13_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 13_00.gif')
rel_13_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 13_30.gif')
rel_14_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 14_00.gif')
rel_14_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 14_30.gif')
rel_15_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 15_00.gif')
rel_15_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 15_30.gif')
rel_16_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 16_00.gif')
rel_16_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 16_30.gif')
rel_17_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 17_00.gif')
rel_17_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 17_30.gif')
rel_18_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 18_00.gif')
rel_18_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 18_30.gif')
rel_19_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 19_00.gif')
rel_19_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 19_30.gif')
rel_20_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 20_00.gif')
rel_20_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 20_30.gif')
rel_21_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 21_00.gif')
rel_21_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 21_30.gif')
rel_22_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 22_00.gif')
rel_22_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 22_30.gif')
rel_23_00 = PhotoImage(file= Pasta +  '\img' + '\\relógio 23_00.gif')
rel_23_30 = PhotoImage(file= Pasta +  '\img' + '\\relógio 23_30.gif')

frame_1 = Frame(janela)
frame_T_1 = Frame(janela)
frame_T_2 = Frame(janela)
frame_T_3 = Frame(janela)
frame_T_4 = Frame(janela)
frame_T_5 = Frame(janela)
frame_T_6 = Frame(janela)
frame_T_7 = Frame(janela)
frame_R = Frame(janela)
frame_S = Frame(janela)
frame_S_numeros = Frame(janela)
frame_S_palavras = Frame(janela)

def temperatura_conversao_ir() :
    frame_1.forget()
    frame_T_1.pack()

def temperatura_conversao_voltar() :
    frame_T_1.forget()
    frame_1.pack()

def temperatura_celcius_para_kelvin_ir() :
    frame_T_1.forget() 
    frame_T_2.pack()

def temperatura_celcius_para_kelvin_converter() :

    c = float(entrada_temperatura_celcius_1.get())
    k = c + 273

    if k >= 0 :
        
        saida_temperatura_kelvin_1['text'] = f'{k}K'
        saida_temperatura_kelvin_1['fg'] = 'Black'
    
    else :

        saida_temperatura_kelvin_1['text']= '-----'
        saida_temperatura_kelvin_1['fg']= 'Light Blue'

def temperatura_celcius_para_kelvin_voltar() :

    frame_T_2.forget()
    frame_T_1.pack()

def temperatura_kelvin_para_celcius_ir() :

    frame_T_1.forget()
    frame_T_3.pack()

def temperatura_kelvin_para_celcius_converter() :

    k = float(entrada_temperatura_kelvin_1.get())
    c = k - 273

    if c >= -273 :

        saida_temperatura_celcius_1['text'] = f'{c}C'
        saida_temperatura_celcius_1['fg'] = 'Black'
    
    else :

        saida_temperatura_celcius_1['text']= '-----'
        saida_temperatura_celcius_1['fg']= 'Light Blue'
    
def temperatura_kelvin_para_celcius_voltar() :

    frame_T_3.forget()
    frame_T_1.pack()

def temperatura_celcius_para_farenheit_ir() :

    frame_T_1.forget()
    frame_T_4.pack()

def temperatura_celcius_para_farenheit_converter() :

    c = float(entrada_temperatura_celcius_2.get())
    f = 1.8 * c + 32

    if f >= -459.4 :
        
        saida_temperatura_farenheit_1['text'] = f'{f}F'
        saida_temperatura_farenheit_1['fg'] = 'Black'
    
    else :

        saida_temperatura_farenheit_1['text']= '-----'
        saida_temperatura_farenheit_1['fg']= 'Light Blue'

def temperatura_celcius_para_farenheit_voltar() :

    frame_T_4.forget()
    frame_T_1.pack()

def temperatura_farenheit_para_celcius_ir() :

    frame_T_1.forget()
    frame_T_5.pack()

def temperatura_farenheit_para_celcius_converter() :

    f = float(entrada_temperatura_farenheit_1.get())
    c= (5/9) * (f - 32)

    if c >= -273 :
        
        saida_temperatura_celcius_2['text'] = f'{c}C'
        saida_temperatura_celcius_2['fg'] = 'Black'
    
    else :

        saida_temperatura_celcius_2['text']= '-----'
        saida_temperatura_celcius_2['fg']= 'Light Blue'

def temperatura_farenheit_para_celcius_voltar() :

    frame_T_5.forget()
    frame_T_1.pack()

def temperatura_farenheit_para_kelvin_ir() :

    frame_T_1.forget()
    frame_T_6.pack()

def temperatura_farenheit_para_kelvin_converter() :

    f = float(entrada_temperatura_farenheit_2.get())
    k = (5/9) * (f - 32) + 273

    if k >= 0 :
        
        saida_temperatura_kelvin_2['text'] = f'{k}K'
        saida_temperatura_kelvin_2['fg'] = 'Black'
    
    else :

        saida_temperatura_kelvin_2['text']= '-----'
        saida_temperatura_kelvin_2['fg']= 'Light Blue'

def temperatura_farenheit_para_kelvin_voltar() :

    frame_T_6.forget()
    frame_T_1.pack()

def temperatura_kelvin_para_farenheit_ir() :

    frame_T_1.forget()
    frame_T_7.pack()

def temperatura_kelvin_para_farenheit_converter() :

    k = float(entrada_temperatura_kelvin_2.get())
    f= (9/5) * (k - 273) + 32

    if f >= -459.4 :
        
        saida_temperatura_farenheit_2['text'] = f'{f}F'
        saida_temperatura_farenheit_2['fg'] = 'Black'
    
    else :

        saida_temperatura_farenheit_2['text']= '-----'
        saida_temperatura_farenheit_2['fg']= 'Light Blue'

def temperatura_kelvin_para_farenheit_voltar() :

    frame_T_7.forget()
    frame_T_1.pack()

def relogio_ir() :

    frame_1.forget()
    frame_R.pack()

    def relogio() :
        tempo_agora = time.strftime('%H:%M:%S')
        display_relogio ['text'] = tempo_agora
        h = datetime.now().hour
        m = datetime.now().minute
        if (h==0) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_00_00
        if (h==0) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_00_30
        if (h==1) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_01_00
        if (h==1) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_01_30
        if (h==2) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_02_00
        if (h==2) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_02_30
        if (h==3) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_03_00
        if (h==3) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_03_30
        if (h==4) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_04_00
        if (h==4) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_04_30
        if (h==5) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_05_00
        if (h==5) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_05_30
        if (h==6) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_06_00
        if (h==6) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_06_30
        if (h==7) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_07_00
        if (h==7) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_07_30
        if (h==8) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_08_00
        if (h==8) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_08_30
        if (h==9) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_09_00
        if (h==9) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_09_30
        if (h==10) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_10_00
        if (h==10) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_10_30
        if (h==11) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_11_00
        if (h==11) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_11_30
        if (h==12) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_12_00
        if (h==12) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_12_30
        if (h==13) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_13_00
        if (h==13) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_13_30
        if (h==14) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_14_00
        if (h==14) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_14_30
        if (h==15) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_15_00
        if (h==15) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_15_30   
        if (h==16) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_16_00
        if (h==16) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_16_30
        if (h==17) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_17_00
        if (h==17) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_17_30
        if (h==18) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_18_00
        if (h==18) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_18_30 
        if (h==19) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_19_00
        if (h==19) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_19_30
        if (h==20) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_20_00
        if (h==20) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_20_30
        if (h==21) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_21_00
        if (h==21) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_21_30
        if (h==22) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_22_00
        if (h==22) and (m in range(30, 60)) : 
            imagem_relogio ['image'] = rel_22_30 
        if (h==23) and (m in range(0, 30)) :
            imagem_relogio ['image'] = rel_23_00
        if (h==23) and (m in range(30, 60)) :
            imagem_relogio ['image'] = rel_23_30
        frame_R.after(1000, relogio)
    relogio()

def relogio_voltar() :

    frame_R.forget()
    frame_1.pack()

def sorteio_ir() :

    frame_1.forget()
    frame_S.pack()

def sorteio_de_numeros_ir() :

    frame_S.forget()
    frame_S_numeros.pack()

def sorteio_de_numeros_resultados() :

    numero_menor = int(entrada_numero_minimo.get())
    numero_maior = int(entrada_numero_maximo.get())
    saida_resultado_sorteio_numeros ['text'] = f'{random.randint(numero_menor, numero_maior)}'

def sorteio_de_numeros_voltar() :

    frame_S_numeros.forget()
    frame_S.pack()

def sorteio_de_palavras_ir() :

    frame_S.forget()
    frame_S_palavras.pack()

def sorteio_de_palavras_resultados() :

    palavras = entrada_palavras.get()
    lista_palavras = palavras.split(', ')
    random.shuffle(lista_palavras)
    saida_resultado_sorteio_palavras ['text'] = lista_palavras[0]
    numero_de_palavras ['text'] = str(len(lista_palavras)) + ' palavras'

def sorteio_de_palavras_voltar() :

    frame_S_palavras.forget()
    frame_S.pack()

# Tela de Início :
        
botao_ir_para_conversao_temp = Button(frame_1, image= fogueira, command = temperatura_conversao_ir)
botao_ir_para_conversao_temp.grid(column = 0, row = 0)

texto_conversao_de_temp = Label(frame_1, text = 'Conversor de temperatura')
texto_conversao_de_temp.grid(column = 0, row = 1)

botao_ir_para_relogio = Button(frame_1, image= relogio, command = relogio_ir)
botao_ir_para_relogio.grid(column = 1, row = 0)

texto_relogio = Label(frame_1, text = 'Relógio com imagem')
texto_relogio.grid(column = 1, row = 1)

botao_ir_para_sorteio = Button(frame_1, image= dado, command = sorteio_ir)
botao_ir_para_sorteio.grid(column = 2, row = 0)

texto_sorteador = Label(frame_1, text = 'Sorteador')
texto_sorteador.grid(column = 2, row = 1)

# Tela de seleção de conversões :

botao_ir_conv_celcius_para_kelvin = Button(frame_T_1, text = 'Celcius para Kelvin', command = temperatura_celcius_para_kelvin_ir)
botao_ir_conv_celcius_para_kelvin.grid(column= 0, row = 0)

botao_ir_conv_kelvin_para_celcius = Button(frame_T_1, text = 'Kelvin para Celcius', command = temperatura_kelvin_para_celcius_ir)
botao_ir_conv_kelvin_para_celcius.grid(column= 2, row = 0)

botao_ir_conv_celcius_para_farenheit = Button(frame_T_1, text = 'Celcius para Farenheit', command = temperatura_celcius_para_farenheit_ir)
botao_ir_conv_celcius_para_farenheit.grid(column= 4, row = 0)

botao_ir_conv_farenheit_para_celcius = Button(frame_T_1, text = 'Farenheit para Celcius', command = temperatura_farenheit_para_celcius_ir)
botao_ir_conv_farenheit_para_celcius.grid(column= 0, row = 2)

botao_ir_conv_farenheit_para_kelvin = Button(frame_T_1, text = 'Farenheit para Kelvin', command = temperatura_farenheit_para_kelvin_ir)
botao_ir_conv_farenheit_para_kelvin.grid(column = 2, row = 2)

botao_ir_conv_kelvin_para_farenheit = Button(frame_T_1, text = 'Kelvin para Farenheit', command = temperatura_kelvin_para_farenheit_ir)
botao_ir_conv_kelvin_para_farenheit.grid(column = 4, row = 2)

botao_voltar_conversao_temp = Button(frame_T_1, text= 'Voltar', command = temperatura_conversao_voltar)
botao_voltar_conversao_temp.grid(column= 2, row = 4)

# Celcius para Kelvin :

entrada_temperatura_celcius_1 = Entry(frame_T_2)
entrada_temperatura_celcius_1.grid(column = 1, row = 2)

texto_temperatura_celcius_1 = Label(frame_T_2, text = 'Temperatura em celcius :  ')
texto_temperatura_celcius_1.grid(column = 0, row = 2)

botao_converter_celcius_para_kelvin = Button(frame_T_2, text = 'Converter', command = temperatura_celcius_para_kelvin_converter)
botao_converter_celcius_para_kelvin.grid(column = 2, row = 6)

texto_temperatura_kelvin_1 = Label(frame_T_2, text = 'Temperatura em kelvin :  ')
texto_temperatura_kelvin_1.grid(column = 0, row = 4)

saida_temperatura_kelvin_1 = Label(frame_T_2, text = '')
saida_temperatura_kelvin_1.grid(column = 1, row = 4)

botao_voltar_conv_celcius_para_kelvin = Button(frame_T_2, text = 'Voltar', command = temperatura_celcius_para_kelvin_voltar)
botao_voltar_conv_celcius_para_kelvin.grid(column = 1, row = 6)

# Kelvin para Celcius :

entrada_temperatura_kelvin_1 = Entry(frame_T_3)
entrada_temperatura_kelvin_1.grid(column = 1, row = 2)

texto_temperatura_kelvin_2 = Label(frame_T_3, text = 'Temperatura em Kelvin :  ')
texto_temperatura_kelvin_2.grid(column = 0, row = 2)

botao_converter_kelvin_para_celcius = Button(frame_T_3, text = 'Converter', command = temperatura_kelvin_para_celcius_converter)
botao_converter_kelvin_para_celcius.grid(column = 2, row = 6)

texto_temperatura_celcius_2 = Label(frame_T_3, text = 'Temperatura em Celcius :  ')
texto_temperatura_celcius_2.grid(column = 0, row = 4)

saida_temperatura_celcius_1 = Label(frame_T_3, text = '')
saida_temperatura_celcius_1.grid(column = 1, row = 4)

botao_voltar_conv_kelvin_para_celcius = Button(frame_T_3, text = 'Voltar', command = temperatura_kelvin_para_celcius_voltar)
botao_voltar_conv_kelvin_para_celcius.grid(column = 1, row = 6)

# Celcius para Farenheit :

entrada_temperatura_celcius_2 = Entry(frame_T_4)
entrada_temperatura_celcius_2.grid(column = 1, row = 2)

texto_temperatura_celcius_3 = Label(frame_T_4, text = 'Temperatura em Celcius :  ')
texto_temperatura_celcius_3.grid(column = 0, row = 2)

botao_converter_celcius_para_farenheit = Button(frame_T_4, text = 'Converter', command = temperatura_celcius_para_farenheit_converter)
botao_converter_celcius_para_farenheit.grid(column = 2, row = 6)

texto_temperatura_farenheit_1 = Label(frame_T_4, text = 'Temperatura em Farenheit :  ')
texto_temperatura_farenheit_1.grid(column = 0, row = 4)

saida_temperatura_farenheit_1 = Label(frame_T_4, text = '')
saida_temperatura_farenheit_1.grid(column = 1, row = 4)

botao_voltar_conv_celcius_para_farenheit = Button(frame_T_4, text = 'Voltar', command = temperatura_celcius_para_farenheit_voltar)
botao_voltar_conv_celcius_para_farenheit.grid(column = 1, row = 6)

# Farenheit para Celcius :

entrada_temperatura_farenheit_1 = Entry(frame_T_5)
entrada_temperatura_farenheit_1.grid(column = 1, row = 2)

texto_temperatura_farenheit_2 = Label(frame_T_5, text = 'Temperatura em Farenheit :  ')
texto_temperatura_farenheit_2.grid(column = 0, row = 2)

botao_converter_farenheit_para_celcius = Button(frame_T_5, text = 'Converter', command = temperatura_farenheit_para_celcius_converter)
botao_converter_farenheit_para_celcius.grid(column = 2, row = 6)

texto_temperatura_celcius_4 = Label(frame_T_5, text = 'Temperatura em Celcius :  ')
texto_temperatura_celcius_4.grid(column = 0, row = 4)

saida_temperatura_celcius_2 = Label(frame_T_5, text = '')
saida_temperatura_celcius_2.grid(column = 1, row = 4)

botao_voltar_conv_farenheit_para_celcius = Button(frame_T_5, text = 'Voltar', command = temperatura_farenheit_para_celcius_voltar)
botao_voltar_conv_farenheit_para_celcius.grid(column = 1, row = 6)

# Farenheit para Kelvin :

entrada_temperatura_farenheit_2 = Entry(frame_T_6)
entrada_temperatura_farenheit_2.grid(column = 1, row = 2)

texto_temperatura_farenheit_3 = Label(frame_T_6, text = 'Temperatura em Farenheit :  ')
texto_temperatura_farenheit_3.grid(column = 0, row = 2)

botao_converter_farenheit_para_kelvin = Button(frame_T_6, text = 'Converter', command = temperatura_farenheit_para_kelvin_converter)
botao_converter_farenheit_para_kelvin.grid(column = 2, row = 6)

texto_temperatura_kelvin_3 = Label(frame_T_6, text = 'Temperatura em Kelvin :  ')
texto_temperatura_kelvin_3.grid(column = 0, row = 4)

saida_temperatura_kelvin_2 = Label(frame_T_6, text = '')
saida_temperatura_kelvin_2.grid(column = 1, row = 4)

botao_voltar_conv_farenheit_para_kelvin = Button(frame_T_6, text = 'Voltar', command = temperatura_farenheit_para_kelvin_voltar)
botao_voltar_conv_farenheit_para_kelvin.grid(column = 1, row = 6)

# Kelvin para Farenheit :

entrada_temperatura_kelvin_2 = Entry(frame_T_7)
entrada_temperatura_kelvin_2.grid(column = 1, row = 2)

texto_temperatura_kelvin_4 = Label(frame_T_7, text = 'Temperatura em Kelvin :  ')
texto_temperatura_kelvin_4.grid(column = 0, row = 2)

botao_converter_kelvin_para_farenheit = Button(frame_T_7, text = 'Converter', command = temperatura_kelvin_para_farenheit_converter)
botao_converter_kelvin_para_farenheit.grid(column = 2, row = 6)

texto_temperatura_farenheit_4 = Label(frame_T_7, text = 'Temperatura em Farenheit :  ')
texto_temperatura_farenheit_4.grid(column = 0, row = 4)

saida_temperatura_farenheit_2 = Label(frame_T_7, text = '')
saida_temperatura_farenheit_2.grid(column = 1, row = 4)

botao_voltar_conv_kelvin_para_farenheit = Button(frame_T_7, text = 'Voltar', command = temperatura_kelvin_para_farenheit_voltar)
botao_voltar_conv_kelvin_para_farenheit.grid(column = 1, row = 6)

# Relógio com imagem :

display_relogio = Label(frame_R, text = '')
display_relogio.grid(column = 1, row = 5)

imagem_relogio = Label(frame_R, image = '')
imagem_relogio.grid(column = 1, row = 3)

botao_voltar_relogio = Button(frame_R, text = 'Voltar', command= relogio_voltar)
botao_voltar_relogio.grid(column= 1, row= 7)

# Sorteador :

botao_ir_sorteio_numeros = Button(frame_S, text= 'Sortear Números', command= sorteio_de_numeros_ir)
botao_ir_sorteio_numeros.grid(column = 0, row = 2)

entrada_numero_minimo = Entry(frame_S_numeros)
entrada_numero_minimo.grid(column = 1, row = 2)

texto_numero_minimo = Label(frame_S_numeros, text = 'Número Mínimo : ')
texto_numero_minimo.grid(column = 0, row = 2)

entrada_numero_maximo = Entry(frame_S_numeros)
entrada_numero_maximo.grid(column = 1, row = 4)

texto_numero_maximo = Label(frame_S_numeros, text = 'Número Máximo : ')
texto_numero_maximo.grid(column = 0, row = 4)

botao_sortear_sorteio_numeros = Button(frame_S_numeros, text= 'Sortear', command = sorteio_de_numeros_resultados)
botao_sortear_sorteio_numeros.grid(column = 1, row = 6)

saida_resultado_sorteio_numeros = Label(frame_S_numeros, text = '')
saida_resultado_sorteio_numeros.grid(column = 1, row = 8)

botao_voltar_sorteio_numeros = Button(frame_S_numeros, text = 'Voltar', command= sorteio_de_numeros_voltar)
botao_voltar_sorteio_numeros.grid(column= 0, row= 6)

botao_ir_sorteio_palavras = Button(frame_S, text= 'Sortear Palavras', command= sorteio_de_palavras_ir)
botao_ir_sorteio_palavras.grid(column = 2, row = 2)

texto_informacoes_sortear_palavras = Label(frame_S_palavras, text = 'Digite as palavras que serão sorteadas, separando as por espaço e vírgula.')
texto_informacoes_sortear_palavras.grid(column= 0, row= 2)

entrada_palavras = Entry(frame_S_palavras, width= 100)
entrada_palavras.grid(column = 1, row = 4)

texto_palavras = Label(frame_S_palavras, text = 'Palavras que serão sorteadas : ')
texto_palavras.grid(column = 0, row = 4)

botao_sortear_palavras = Button(frame_S_palavras, text= 'Sortear', command= sorteio_de_palavras_resultados)
botao_sortear_palavras.grid(column = 1, row = 6)

saida_resultado_sorteio_palavras = Label(frame_S_palavras, text = '')
saida_resultado_sorteio_palavras.grid(column= 1, row = 8)

numero_de_palavras = Label(frame_S_palavras, text = '')
numero_de_palavras.grid(column = 0, row= 8)

botao_voltar_sorteio_palavras = Button(frame_S_palavras, text = 'Voltar', command= sorteio_de_palavras_voltar)
botao_voltar_sorteio_palavras.grid(column= 0, row= 6)

janela.resizable(False, False)

frame_1.pack()

janela.mainloop()
