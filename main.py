import pgzrun
from random import randint
from time import time

WIDTH=800
HEIGHT=600

cheeses=[]

start_time=0
total_time=0
end_time=0

number_of_cheese=10

def create_cheese():
    global start_time
    for count in range(0,number_of_cheese):
        cheese=Actor("cheese")
        cheese.pos=randint(40,WIDTH-40), randint(40,HEIGHT-40)
        cheeses.append(cheese)
    start_time=time()

def on_mouse_down(pos):
    #global mouse
    for i in cheeses:
        #if cheeses[i].collidepoint(pos):
            #mouse=Actor("rat_mouse")


def draw():
    global total_time
    screen.blit("bg",(0,0))
    number=1
    for cheese in cheeses:
        screen.draw.text(str(number),(cheese.pos[0],cheese.pos[1]+20))
        cheese.draw()
        number=number+1

    
    

create_cheese()
pgzrun.go()