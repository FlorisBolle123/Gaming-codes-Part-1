import pgzrun

TITLE="Quiz Master"
WIDTH=870
HEIGHT=650

marquee_box=Rect(0,0,880,80)
question_box=Rect(20,100,650,150)
timer_box=Rect(700,100,150,150)
answer_box1=Rect(20,270,300,150)
answer_box2=Rect(370,270,300,150)
answer_box3=Rect(20,450,300,150)
answer_box4=Rect(470,450,300,150)
skip_box=Rect(700,270,150,330)

score=0
time_left=10
question_file_name="question.txt"
marquee_message=""
is_game_over=False

answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]
questions=[]
question_count=0
question_index=0

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"dark blue")
    screen.draw.filled_rect(timer_box,"light blue")
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"cyan")
    marquee_message="Welcome to quiz master..."
    marquee_message=marquee_message+f"Q: {question_index} of {question_count}"
    screen.draw.textbox(marquee_message,marquee_box,color="white")
    screen.draw.textbox(str(time_left),timer_box,color="white",shadow=(0.5,0.5),scolor="dim grey")
    screen.draw.textbox("skip",skip_box,color="black",angle=-90)
    screen.draw.textbox(question[0].strip(),question_box,color="white",shadow=(0.5,0.5),scolor="dim grey")

    index=1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color="black")
        index=index+1

def update():
    move_marquee()

def move_marquee():
    marquee_box.x=marquee_box.x-2
    if marquee_box.right <0:
        marquee_box.left=WIDTH
    
def read_question_file():
    global question_count,questions
    q_file=open(question_file_name,"r")
    for question in q_file:
        questions.append(question)
        question_count=question_count+1
    q_file.close()

def read_next_question():
    global question_index
    question_index=question_index+1
    return questions.pop(0).split(",")

read_question_file()
question=read_next_question()

pgzrun.go()