import turtle
import math
 
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700,700)



turtle.register_shape("wizardright.gif")
turtle.register_shape("wizardleft.gif")
turtle.register_shape("treasure.gif")
turtle.register_shape("wall.gif")


 

class Pen(turtle.Turtle):
   
    def __init__(self):
       
        turtle.Turtle.__init__(self)
        self.shape("wizardleft.gif")
        self.color("blue")
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
 

levels = [""]
 

level_1 = [

 "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XPXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXX",
 "X  XX   XXX XXXXXXXXXXXXXXXXXXXXXXXXX",
 "XX XX X XX  XXXXXXXXXXXXXXXXXXXXXXXXX",
 "XX  X X XX XXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXX   X XX XXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXX XXXXX XXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXX  XXXX  XXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXX XXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXX XXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXX XXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXX   X  XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXX X XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
 "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]
 
   
levels.append(level_1)
 

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
           
                        
            character = level[y][x]
            
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)
 
            
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                
                walls.append((screen_x,screen_y))
           
           
            
            if character == "P":
                pen.goto(screen_x, screen_y)

          
 

pen = Pen()
player = Player()
 

walls = []
 
 
setup_maze(levels[1])
 

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")
 

wn.tracer(0)
 

while True:
    
    wn.update()