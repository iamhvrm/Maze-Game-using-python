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
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
 
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wizardleright.gif")
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
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXX                XXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXX  XXXXXXXX",
"XXXXXXX  XXXXXXXX   XXXXX   XXXXXX",
"XXXXXX  XXX     X X      XX  XXXXX",
"XXXXX  XXX  XXXXX XXXX   XX  XXXXX",
"XXXX  XXX  X          XX  XX  XXXX",
"XXX  XXX  X   XXXXXXXX  X  XX  XXX",
"XX  XXX  X  XX       XX  X  XX  XX",
"XX   X  X  XX  XXXXX  XX XX XXX XX",
"XXXX X X  XX  XXXXXXX  X XX XXX XX",
"XX   XXX  XX  XXXXXXX  X XX XXXXXX",
"XX XXX XX  Xo XXXXXXX  X XX XXX XX",
"XX XXX  XX  X  XXXXX  XX XX XXX XX",
"XX  XXX  XX  X        X  XX XXX XX",
"XX    XX  XX  XXXX XXX  XX  XX  XX",
"XX X   XX   X          XX  XX  XXX",
"XX  X   XXX XXXXXXXXXXX   XX  XXXX",
"XXX XXX  XX             XX   XXXXX",
"XXX XXXX  XXXXX XXXXXXXXXX  XXXXXX",
"XX  XXXXX  XXXX    XXXXXX  XXXXXXX",
"XX XXXXXXX  XXXXXX XXXXX  XXXXXXXX",
"XX                       XXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

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
                pen.stamp()
               
 
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