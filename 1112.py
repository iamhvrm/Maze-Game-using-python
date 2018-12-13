import turtle
import math
 
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700,700)


#registershapes
turtle.register_shape("wizardright.gif")
turtle.register_shape("wizardleft.gif")
turtle.register_shape("treasure.gif")
turtle.register_shape("wall.gif")


 
#create pen
class Pen(turtle.Turtle):
   
    def __init__(self):
       
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
 
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wizardright.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold=0
 
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
 
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
 
    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor() 
 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
 
    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 
 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
 
#create level list
levels = [""]
 
#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"Xp   XXXXXXX        XXXXX",
"X           XXXXXX  XXXXX",
"X  XXXXXXX          XXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXX",
"X                       X",
"XXXXXXX  XXXXXXXXXXXXXXXX",
"XXXXXX   XXXXXXXXXXXXXXXX",
"XXXXXX                  X",
"XXXXXX   XXXXXXXXXXXXXXXX",
"XXXXXX   XXXXXXXXXXXXXXXX",
"X                       X",
"XXXXX    XXXXXXXXXX   XXX",
"X        XXXXXXXXXXXXXXXX",
"XXXXXX   XXXXXXXXXXXXXXXX",
"X                        ",
"XXXXXXXXXXXXX   XXXXXXXXX",
"XXXXXX   XXXX   XXXXXXXXX",
"XXXXX    XXXX           X",
"X                      XX",
"XXXXXXX   YXXXXXXXXXXXXXX",
"XXXXXX     XXXXX     XXXX",
"XXXXXX                XXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
 
   
levels.append(level_1)
 
#Create Level Setup Fuction
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
           
            #Get the caracter at each x,y cordinate            
            character = level[y][x]
            #Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
 
            #Check if it is an X
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                #Add coordinates to wall list
                walls.append((screen_x,screen_y))
           
           
            #Check if it is a P (Player)
            if character == "P":
                pen.goto(screen_x, screen_y)
               
 
#class instances
pen = Pen()
player = Player()
 
#Create wall cordinate List
walls = []
 
 
setup_maze(levels[1])
 

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")
 
#Turn off screen updates
wn.tracer(0)
 
#main game loop
while True:
    #Update screen
    wn.update()