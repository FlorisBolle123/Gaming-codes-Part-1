import pgzrun
from random import randint

#setting up screen
TITLE="SHREK HIT"
WIDTH=500
HEIGHT=500

#adding shrek and text to display
shrek=Actor('shrek')
bg=Actor('th')

message=" "

#Function draw so shrek and other things can be shown
def draw():
    screen.clear()
    bg.draw()
    shrek.draw()
    screen.draw.text(message, center=(400,10),fontsize=30)

#defining positition for shrek
def place_shrek():
    shrek.x=randint(50,WIDTH-50)
    shrek.y=randint(50,HEIGHT-50)

#making the mouse button interact
def on_mouse_down(pos):
    global message
    if shrek.collidepoint(pos):
        message="You hit me!!"
        place_shrek()
    else:
        message="You missed me!!"

place_shrek()

pgzrun.go()