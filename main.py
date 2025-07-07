import pgzrun
import random

#screen size
WIDTH=800
HEIGHT=600

CENTRE=(400,300)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["battery","bottle","chipbag","paperbag","plasticbag"]

game_over = False
game_complete = False
current_level = 1

items=[]
animations=[]

#anounce the draw function
def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("background", (0,0))
    if game_over:
        display_message("Game over","Try again...")
    elif game_complete:
        display_message("You won","Well done...")
    else: 
        for item in items:
            item.draw()

#global items
def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

# this function helps you animate the items and the layout
def make_items(number_of_extra_items):
    items_to_create=get_option_to_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

# this helps you randomly choose items
def get_option_to_create(number_of_extra_items):
    items_to_create=["paperbag"]
    for i in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

# This is the function that draws the image/item on the screen
def create_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item=Actor(option+"img")
        new_items.append(item)
    return new_items

#this makes the layout of where everything is
def layout_items(items_to_layout):
    number_of_gaps=len(items_to_layout)+1
    gap_size=WIDTH / number_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos=(index+1)*gap_size
        item.x=new_x_pos
#This makes the animations for the items
def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = START_SPEED - current_level
        item.anchor=("center","bottom")
        animation = animate(item,duration=duration,on_finished=handle_game_over,y=HEIGHT)
        animations.append(animation)