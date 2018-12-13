import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700,700)
wn.tracer(0)

"""images=[ "treasure.gif","wizard_left.gif", "wizard_right.gif","wall.gif", "enemy_left.gif","enemy_right.gif" ]

for image in images
	turtle.register_shapes(image)"""

turtle.register_shape("wizard_left.gif")
turtle.register_shape("wizard_right.gif")
turtle.register_shape("treasure.gif")
turtle.register_shape("wall1.gif")
turtle.register_shape("enemy_left.gif")
turtle.register_shape("enemy_right.gif")
turtle.register_shape("youwon.gif")


 
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
        self.shape("wizard_right.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

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

        self.shape("wizard_right.gif")
 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
 
    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 

        self.shape("wizard_right.gif")
 
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
    	a=self.xcor()-other.xcor()
    	b=self.ycor()-other.ycor()
    	distance=math.sqrt((a**2)+(b**2))

    	if distance<5:
    		return True
    	else:
    		return False
class Treasure(turtle.Turtle):
	def __init__(self,x,y):
		turtle.Turtle.__init__(self)
		self.shape("treasure.gif")
		self.color("blue")
		self.penup()
		self.gold=100
		self.goto(x,y)

	def destroy(self):
		self.goto(2000,2000)
		self.hideturtle()

class Enemy(turtle.Turtle):
	def __init__(self,x,y):
		turtle.Turtle.__init__(self)
		self.shape("enemy_left.gif")
		self.color("red")
		self.penup()
		self.speed()
		self.gold=25
		self.goto(x,y)
		self.direction=random.choice(["up","down","left","right"])
	def move(self):
		if self.direction=="up":
			dx=0
			dy=24
		elif self.direction=="down":
			dx=0
			dy=-24
		elif self.direction=="left":
			dx=24
			dy=0
			self.shape("enemy_right.gif")
		else:
			dx=0
			dy=0

		move_to_x=self.xcor()+dx
		move_to_y=self.ycor()+dy

		if (move_to_x,move_to_y) not in walls:
			self.goto(move_to_x,move_to_y)
		else:
			self.direction=random.choice(["up","down","right","left"])


		turtle.ontimer(self.move, t=random.randint(100,300))
	def destroy(self):
		self.goto(2000,2000)
		self.hideturtle()

levels=[""]

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXX                XXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXX  XXXXXXXX",
"XXXXXXX  XXXXXXXX   XXXXX   XXXXXX",
"XXXXXX  XXX     X X  E   XX  XXXXX",
"XXXXX  XXX  XXXXX XXXX   XX  XXXXX",
"XXXX  XXX  X          XX  XX  XXXX",
"XXX  XXX  X   XXXXXXXX  X  XX  XXX",
"XX  XXX  X  XX       XX  X  XX  XX",
"XX   X  X  XX  XXXXX  XX XX XXX XX",
"XXXX X X  XX  XXXXXXX  X XX XXXTXX",
"XX   XXX  XX  XXXXXXX  X XX XXXXXX",
"XX XXX XX  X  XXXXXXX  X XX XXX XX",
"XX XXX  XX  X  XXXXX  XX XX XXX XX",
"XX  XXX  XX  X        X  XX XXX XX",
"XX    XX  XX  XXXX XXX  XX  XX  XX",
"XX X   XX   X          XX  XX  XXX",
"XX  X   XXX XXXXXXXXXXX   XX  XXXX",
"XXX XXX  XX             XX   XXXXX",
"XXX XXXX  XXXXX XXXXXXXXXX  XXXXXX",
"XX  XXXXX  XXXX    XXXXXX  XXXXXXX",
"XX XXXXXXX  XXXXXX XXXXX  XXXXXXXX",
"XX          E            XXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

treasures=[]

enemies=[]

levels.append(level_1)

def setup_maze(level):
	for y in range(len(level)):
		for x in range(len(level[y])):

			character=level[y][x]

			screen_x=-288+(x*24)
			screen_y=288-(y*24)


			if character =="X":
				pen.goto(screen_x, screen_y)
				pen.shape("wall1.gif")
				pen.stamp()
				walls.append((screen_x, screen_y))

			if character =="T":
				treasures.append(Treasure(screen_x, screen_y)) 
				
			

			if character =="P":
				player.goto(screen_x, screen_y)
	
			if character =="E":
				enemies.append(Enemy(screen_x, screen_y))



pen=Pen()
player=Player()


walls=[]

setup_maze(levels[1])


turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

wn.tracer(0)

for enemy in enemies:
	turtle.ontimer(enemy.move, t=250)

while True:

	for treasure in treasures:
		if player.is_collision(treasure):
			player.gold+=treasure.gold
			print("player Gold:{}".format(player.gold))
			treasure.destroy()
			treasures.remove(treasure)
			open("youwon.gif")


	for enemy in enemies:
		if player.is_collision(enemy):
			print("PLayer Dies!")
	
	wn.update()