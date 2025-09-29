#importing modules
import pgzrun
from random import randint

#importing constances
TITLE="Flappy Ball"
WIDTH=800
HEIGHT=600

GRAVITY=2000

#Defining a class
class Ball:
    def __init__(self,initial_x,initial_y):
        self.x=initial_x
        self.y=initial_y
        self.vx=200
        self.vy=0
        self.radius=40
       

    def draw(self):
        r=randint(0,255)
        b=randint(0,255)
        g=randint(0,255)
        pos=(self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,(r,g,b))


ball=Ball(50,100)
#drawing ball on screen
def draw():
    screen.clear()
    ball.draw()

#ball Pyschics
def update(dt):
    uy=ball.vy
    ball.vy += GRAVITY *dt
    ball.y += (uy + ball.vy) *0.5*dt

    if ball.y > HEIGHT - ball.radius:
        ball.y=HEIGHT-ball.radius
        ball.vy = -ball.vy*0.9

    ball.x+=ball.vx*dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

#Jump on Space
def on_key_down(key):
    if key == keys.SPACE:
        ball.vy=-500
        
pgzrun.go()