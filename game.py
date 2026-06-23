import turtle
import time 
import random
delay=0.2
score=0
segments=[]
screen=turtle.Screen()
screen.bgcolor("#ffffff")
screen.setup(width=600,height=600)
screen.tracer(0)

snake=turtle.Turtle()
snake.shape("square")
snake.speed(0)
snake.goto(0,0)
snake.penup()
snake.color("black")
snake.direction="stop"

def move():
    x=snake.xcor()
    y=snake.ycor()
    if snake.direction=="Up":
     snake.sety(y+20)
     snake.seth(90)
    if snake.direction=="Down":
     snake.sety(y-20)
     snake.seth(270)
    if snake.direction=="Right":
     snake.setx(x+20)
     snake.seth(0)
    if snake.direction=="Left":
     snake.setx(x-20)
     snake.seth(180)

def go_down():
    snake.direction="Down"
def go_up():
    snake.direction="Up"
def go_left():
    snake.direction="Left"
def go_right():
    snake.direction="Right"

screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_left,"Left")
screen.onkeypress(go_right,"Right")
    
#score pem setup
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)  # Position at the top of the screen
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

#food set up
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("green")
food.penup()
food.goto(0, 220)

colors=["red","orange","pink","green","purple","blue","yellow","grey"] 

bom = [] 
for i in range(3):
    new_bom = turtle.Turtle()
    new_bom.speed(0)
    new_bom.shape("circle")
    new_bom.color("#FF0000")
    new_bom.penup()
    new_bom.hideturtle()
    new_bom.goto(1000, 1000)
    bom.append(new_bom)

bom_alert=turtle.Turtle()
bom_alert.speed(0)
bom_alert.color("#FF0000")
bom_alert.penup()
bom_alert.hideturtle()
bom_alert.goto(0,230)

extra_foods = []
for i in range(4):
    f = turtle.Turtle()
    f.speed(0)
    f.shape("square")
    f.color("green")
    f.penup()
    f.hideturtle()      
    f.goto(1000, 1000)  
    extra_foods.append(f)

running = True

def quit_game():
    global running
    running = False

screen.listen()
screen.onkeypress(quit_game, "q")

while running:
    try:
        screen.update()
        
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            x = snake.xcor()
            y = snake.ycor()
            segments[0].goto(x, y) 
            
        move()

        if snake.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

            score += 10
            pen.clear()
            pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")
            new_segment.color(random.choice(colors))
            new_segment.penup()
            segments.append(new_segment)
    
            if score == 50:
                delay = 0.15
            elif score == 100:
                delay = 0.1

        if score >= 350:
            for f in extra_foods:
                if not f.isvisible():
                    f.goto(random.randint(-270, 270), random.randint(-270, 270))
                    f.showturtle()
                for f in extra_foods:
                    if f.isvisible() and snake.distance(f) < 20:
                        f.goto(random.randint(-270, 270), random.randint(-270, 270))
                        score += 10
                        pen.clear()
                        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

                    new_segment = turtle.Turtle()
                    new_segment.speed(0)
                    new_segment.shape("circle")
                    new_segment.color(random.choice(colors))
                    new_segment.penup()
                    segments.append(new_segment)

        if snake.xcor() > 290: snake.setx(-290)
        elif snake.xcor() < -290: snake.setx(290)
        if snake.ycor() > 290: snake.sety(-290)
        elif snake.ycor() < -290: snake.sety(290)
 
        if score == 200:
            screen.bgcolor("#808080")
            delay = 0.05
        if score == 230:
            screen.bgcolor("#A6D892")
        if score == 350:
            screen.bgcolor("#ffffff")

        if score >= 300:
            bom_alert.clear()
            bom_alert.write("DON'T EAT THE BOM!", align="center", font=("Courier", 18, "bold")) 
            for b in bom:
                if not b.isvisible():
                    bx = random.randint(-270, 270)
                    by = random.randint(-270, 270)
                    b.goto(bx, by)
                    b.showturtle()

                if snake.distance(b) < 20:
                    bx = random.randint(-270, 270)
                    by = random.randint(-270, 270)
                    b.goto(bx, by)
                    score -= 10
                    pen.clear()
                    pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
                    if len(segments) > 0:
                        last_seg = segments.pop()
                        last_seg.hideturtle()

        time.sleep(delay) 

    except: 
        running = False

