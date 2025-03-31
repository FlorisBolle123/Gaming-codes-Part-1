import pgzrun
from random import randint

WIDTH=300
HEIGHT=300

def draw():

    re=210
    g=50
    b=randint(120,255)

    w=WIDTH
    h=HEIGHT-200

    for i in range(20):
        r=Rect((0,0),(w,h))
        r.center=150,150
        screen.draw.rect(r,(re,g,b))

        re=re-10
        g=g+10

        w=w-10
        h+=10

pgzrun.go()