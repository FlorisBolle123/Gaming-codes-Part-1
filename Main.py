#importing modules
import pgzrun
from random import randint
from time import time

#setting screen size
WIDTH=800
HEIGHT=600

#making variables
satellites=[]
lines=[]
next_satellite=0

start_time = 0
total_time = 0
end_time = 0

number_of_satellite=8

#Creating and setting the limit of how many satellites and where they are
def create_satellites():
    global start_time
    for count in range(0,number_of_satellite):
        satellite=Actor("setalite")
        satellite.pos=randint(40,WIDTH-40), randint(40,HEIGHT-40)
        satellites.append(satellite)
    start_time=time()

#Makes everything be drawn on your screen
def draw():
    global total_time
    screen.blit("bg",(0,0))
    number =1
    for satellite in satellites:
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        number=number+1

    if next_satellite < number_of_satellite:
        total_time=time() - start_time
        screen.draw.text(str(round(total_time)),(10,10),fontsize=30)
    else:
        screen.draw.text(str(round(total_time)),(10,10),fontsize=30)
    	
    for i in lines:
        screen.draw.line(i[0],i[1],(255,255,255))

def update():
    pass

#Making the mouse adjustments for the game
def on_mouse_down(pos):
    global next_satellite,lines
    if next_satellite < number_of_satellite:
        if satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((satellites[next_satellite-1].pos, satellites[next_satellite].pos))
            next_satellite = next_satellite+1
        else:
            lines=[]
            next_satellite=0

create_satellites()

pgzrun.go()