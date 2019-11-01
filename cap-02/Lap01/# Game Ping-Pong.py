# Game Ping-Pong

from tkinter import *
import random
import time

#Recebendo valor do usurio

level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))

#Variavel

length = 500/level

root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

root.update()

#Variáveis

count = 0
lost = False

#Classe

class Bola:
    def __init__(self, canvas, Barra, color):

        #Variaveis

        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        #Lista

        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        #Variavel
        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    #Funçao
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        #Condicional

        if pos[1] <= 0:

            #Variavel
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)

        #Condicional

        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1

                #Chamando a Funçao

                score()

        #Condicional

        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            
            #Chamando a Funçao

            game_over()

            #Variaveis

            global lost
            lost = True

#Classe

class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    #Funçao

    def draw(self):

        #Chamando o metodo Self

        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        #Condicional

        if self.pos[0] <= 0:

            #Variavel

            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)

    #Funçao

    def move_left(self, event):
    
        #Condicional

        if self.pos[0] >= 0:

            #Variavel

            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3


def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

    time.sleep(1)
    Barra.draw()
    Bola.draw()

#Funções

def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

def game_over():
    canvas.itemconfig(game, text="Game over!")

Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")


score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))


canvas.bind_all("<Button-1>", start_game)

# Executando o programa

root.mainloop()