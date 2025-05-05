import pgzrun
from random import randint

WIDTH=600
HEIGHT=500

score = 0
game_over=False

tom=Actor("tom")
tom.pos=100,100

jerry=Actor("jerry")
jerry.pos=200,200

def draw():
    screen.blit("house",(0,0))
    tom.draw()
    jerry.draw()
    screen.draw.text("Score : "+str(score),color="black",topleft=(10,10))

    if game_over:
        screen.fill("black")
        screen.draw.text("Times up! Your final score: "+str(score),midtop=(WIDTH/2,10),fontsize=40,color="violet")

def place_jerry():
    jerry.x=randint(50,(WIDTH-50))
    jerry.y=randint(50,(HEIGHT-50))

def time_up():
    global game_over
    game_over=True

def update():
    global score

    if keyboard.left:
        tom.x=tom.x-2
    if keyboard.right:
        tom.x=tom.x+2
    if keyboard.up:
        tom.y=tom.y-2
    if keyboard.down:
        tom.y=tom.y+2

    jerry_collected=tom.colliderect(jerry)

    if jerry_collected:
        score=score+10
        place_jerry()

clock.schedule(time_up,60.0)

pgzrun.go()