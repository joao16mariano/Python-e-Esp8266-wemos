from tkinter import *
from PIL import Image, ImageTk
import serial

global releA
releA = False

global releB
releB = False

global releC
releC = False

global releD
releD = False

global releE
releE = False

global releF
releF = False

def create_porta():
    global portaUSB
    aux = temp.get()
    portaUSB = serial.Serial(aux, 9600)
    

def sen_command(cod):
    aux = str(cod)
    portaUSB.write(aux.encode())
    

def comando(op):
    global releA
    global releB
    global releC
    global releD
    global releE
    global releF
    
    
    if (op == 1 and releA == False):
        print("D4 Ligado")
        sen_command('001')
        icone = ImageTk.PhotoImage(file="verde.png")
        botao1.config(image=icone, highlightthickness = 0, bd=0)
        botao1.image = icone
        releA = True

    elif (op == 1 and releA == True):
        print('D4 Desligado')
        sen_command('003')
        icone = ImageTk.PhotoImage(file="cinza.png")
        botao1.config(image=icone, highlightthickness = 0, bd=0)
        botao1.image = icone
        releA = False
        

        

    elif (op == 2 and releB == False):
        print('D5 Ligado')
        sen_command('005')
        icone = ImageTk.PhotoImage(file="verde.png")
        botao2.config(image=icone, highlightthickness = 0, bd=0)
        botao2.image = icone
        releB = True

    elif (op == 2 and releB == True):
        print('D5 Desligado')
        sen_command('008')
        icone = ImageTk.PhotoImage(file="cinza.png")
        botao2.config(image=icone, highlightthickness = 0, bd=0)
        botao2.image = icone
        releB = False
        

        

    elif (op == 3 and releC == False):
        print('D7 Ligado')
        sen_command('011')
        icone = ImageTk.PhotoImage(file="verde.png")
        botao3.config(image=icone, highlightthickness = 0, bd=0)
        botao3.image = icone
        releC = True

    elif (op == 3 and releC == True):
        print('D7 Desligado')
        sen_command('014')
        icone = ImageTk.PhotoImage(file="cinza.png")
        botao3.config(image=icone, highlightthickness = 0, bd=0)
        botao3.image = icone
        releC = False
        



    elif (op == 4 and releD == False):
        print('D3 Ligado')
        sen_command('017')
        icone = ImageTk.PhotoImage(file="verde.png")
        botao4.config(image=icone, highlightthickness = 0, bd=0)
        botao4.image = icone
        releD = True

    elif (op == 4 and releD == True):
        print('D3 Desligado')
        sen_command('020')
        icone = ImageTk.PhotoImage(file="cinza.png")
        botao4.config(image=icone, highlightthickness = 0, bd=0)
        botao4.image = icone
        releD = False

        


    elif (op == 5 and releE == False):
        print('D2 Ligado')
        sen_command('023')
        icone = ImageTk.PhotoImage(file="verde.png")
        botao5.config(image=icone, highlightthickness = 0, bd=0)
        botao5.image = icone
        releE = True

    elif (op == 5 and releE == True):
        print('D2 Desligado')
        sen_command('026')
        icone = ImageTk.PhotoImage(file="cinza.png")
        botao5.config(image=icone, highlightthickness = 0, bd=0)
        botao5.image = icone
        releE = False
        



    elif (op == 6 and releF == False):
        print('D1 Ligado')
        sen_command('029')
        icone = ImageTk.PhotoImage(file="verde.png")
        botao6.config(image=icone, highlightthickness = 0, bd=0)
        botao6.image = icone
        releF = True

    elif (op == 6 and releF == True):
        print('D1 Desligado')
        sen_command('032')
        icone = ImageTk.PhotoImage(file="cinza.png")
        botao6.config(image=icone, highlightthickness = 0, bd=0)
        botao6.image = icone
        releF = False
        
    

janela = Tk()

janela.title('Automação Residencial')
janela.geometry('410x750')
janela.configure(bg='#1972a1')


text_Port = Label (text='Porta do Arduino:', fg = '#0cff00', bg='#1972a1', ).place(x=50,y=200)
temp = StringVar ()
porta = Entry(janela, bg='#84a8bb', textvariable = temp).place(x=150,y=200)
botao_port  = Button(text='OK', fg = '#0cff00', bg='#1972a1', command = create_porta).place(x=290,y=197)



texto1 = Label(text='D4 - QUARTO', fg = '#fcfafa',bg='#1972a1')
texto1.place(x=40,y=100)
ico1 = ImageTk.PhotoImage(file="cinza.png")
botao1 = Button(text='Ligar Led D4', command = lambda: comando(1))
botao1.config(image=ico1, highlightthickness = 0, bd=0)
botao1.place(x=60,y=120)


texto2 = Label(text='D5 - SALA', fg = '#fcfafa', bg='#1972a1')
texto2.place(x=170,y=100)
ico2 = ImageTk.PhotoImage(file="cinza.png")
botao2 = Button(text='Ligar Led D5', command = lambda: comando(2))
botao2.config(image=ico2, highlightthickness = 0, bd=0)
botao2.place(x=180,y=120)


texto3 = Label(text='D6 - COZINHA', fg = '#fcfafa',bg='#1972a1')
texto3.place(x=280,y=100)
ico3 = ImageTk.PhotoImage(file="cinza.png")
botao3 = Button(text='Ligar Led D6', command = lambda: comando(3))
botao3.config(image=ico3, highlightthickness = 0, bd=0)
botao3.place(x=300,y=120)


texto4 = Label(text='D3 - QUARTO2', fg = '#fcfafa',bg='#1972a1')
texto4.place(x=280,y=21)
ico4 = ImageTk.PhotoImage(file="cinza.png")
botao4 = Button(text='Ligar Led D3', command = lambda: comando(4))
botao4.config(image=ico4, highlightthickness = 0, bd=0)
botao4.place(x=300,y=40)


texto5 = Label(text='D2 - QUARTO3', fg = '#fcfafa',bg='#1972a1')
texto5.place(x=160,y=21)
ico5 = ImageTk.PhotoImage(file="cinza.png")
botao5 = Button(text='Ligar Led D2', command = lambda: comando(5))
botao5.config(image=ico5, highlightthickness = 0, bd=0)
botao5.place(x=180,y=40)


texto6 = Label(text='D1 - QUARTO3', fg = '#fcfafa',bg='#1972a1')
texto6.place(x=40,y=21)
ico6 = ImageTk.PhotoImage(file="cinza.png")
botao6 = Button(text='Ligar Led D1', command = lambda: comando(6))
botao6.config(image=ico5, highlightthickness = 0, bd=0)
botao6.place(x=60,y=40)



janela.mainloop()
