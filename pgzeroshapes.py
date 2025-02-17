import pgzrun

WIDTH=300
HEIGHT=300

def draw():

    width=WIDTH
    height=HEIGHT-200

    for i in range(20):
        r=Rect((0,0),(width,height))
        r.center=150,150
        screen.draw.rect(r,("blue"))

        width=width-10
        height+=10

pgzrun.go()