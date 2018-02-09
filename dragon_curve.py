import turtle
import math

# redFlag = False
# greenFlag = False
# blueFlag = False

firstStage = True
secondStage = False
thirdStage = False
fourthStage = False

#L-rules
#var: XY
#constants:F+-
#start:FX
#rules: 
#	X=X+YF+
#	Y=-FX-Y
# angle=90

def main():
	turtle.bgcolor("#000000")
	turtle.screensize(canvwidth=2000, canvheight=2000)
	turtle.colormode(255)
	turtle.speed(0)
	
	drawTurtle = turtle.Turtle()
	drawTurtle.up()
	drawTurtle.setpos((-50, 0))
	drawTurtle.down()
	drawTurtle.speed(0)
	drawTurtle.hideturtle()
	drawTurtle.pencolor(255, 0, 0)
	
	dragonStart(drawTurtle, 8, 10)
	
	# global firstStage
	# global secondStage
	# global thirdStage
	
	# firstStage = True
	# secondStage = False
	# thirdStage = False
	
	# drawTurtle2 = turtle.Turtle()
	# drawTurtle2.up()
	# drawTurtle2.setpos((-50, 0))
	# drawTurtle2.right(180)
	# drawTurtle2.down()
	# drawTurtle2.speed(0)
	# drawTurtle2.hideturtle()
	# drawTurtle2.pencolor(255, 0, 0)
	
	# dragonStart(drawTurtle2, 8, 10)
	
	# firstStage = True
	# secondStage = False
	# thirdStage = False
	
	# drawTurtle3 = turtle.Turtle()
	# drawTurtle3.up()
	# drawTurtle3.setpos((-50, 0))
	# drawTurtle3.right(90)
	# drawTurtle3.down()
	# drawTurtle3.speed(0)
	# drawTurtle3.hideturtle()
	# drawTurtle3.pencolor(255, 0, 0)
	
	# dragonStart(drawTurtle3, 8, 10)
	
	# firstStage = True
	# secondStage = False
	# thirdStage = False
	
	# drawTurtle4 = turtle.Turtle()
	# drawTurtle4.up()
	# drawTurtle4.setpos((-50, 0))
	# drawTurtle4.left(90)
	# drawTurtle4.down()
	# drawTurtle4.speed(0)
	# drawTurtle4.hideturtle()
	# drawTurtle4.pencolor(255, 0, 0)
	
	# dragonStart(drawTurtle4, 8, 10)

	
	ts = turtle.getscreen()
	ts.getcanvas().postscript(file="duck.jpg")
	
	turtle.done()
	return

def updateColor(drawTurtle):
	currentColor = drawTurtle.pencolor()
	# global redFlag
	# global greenFlag
	# global blueFlag
	
	global firstStage
	global secondStage
	global thirdStage
	
	#red -> orange -> yellow -> white -> blue
	
	if (currentColor[1] == currentColor[0] and firstStage):
		firstStage=False
		secondStage=True
	
	if (secondStage and currentColor[0] == currentColor[2]):
		secondStage = False
		thirdStage=True
		
	if (firstStage):
		currentColor = (currentColor[0] , currentColor[1] + 1, currentColor[2])
	elif (secondStage):
		currentColor = (currentColor[0] , currentColor[1], currentColor[2]+5)
	elif (thirdStage):
		currentColor = (currentColor[0]-1 , currentColor[1]-1, currentColor[2])
	
	# if (currentColor[0] <= 10 and not redFlag):
		# redFlag = True
	# elif (currentColor[0] >= 240 and redFlag):
		# redFlag = False
	
	# if (currentColor[1] <= 10 and not greenFlag):
		# greenFlag = True
	# elif (currentColor[1] >= 240 and greenFlag):
		# greenFlag = False
	
	# if (currentColor[2] <= 10):
		# blueFlag = True
	# elif (currentColor[2] >= 240):
		# blueFlag = False
		
	# if (redFlag):
		# currentColor = (currentColor[0] , currentColor[1], currentColor[2])
	# else:
		# currentColor = (currentColor[0] - 1, currentColor[1] - 2, currentColor[2])
		
	# if (greenFlag):
		# currentColor = (currentColor[0], currentColor[1] + 10, currentColor[2])
	# else:
		# currentColor = (currentColor[0], currentColor[1] - 10, currentColor[2])

	# if (blueFlag):
		# currentColor = (currentColor[0], currentColor[1], currentColor[2] + 1)
	# else:
		# currentColor = (currentColor[0], currentColor[1], currentColor[2] - 1)
	
	drawTurtle.pencolor(currentColor)
	return
	

def dragonStart(drawTurtle, iter, len):
	drawTurtle.forward(len)
	updateColor(drawTurtle)
	dragonX(drawTurtle, iter, len)
	return

def dragonX(drawTurtle, iter, len):
	if (iter > 0):
		dragonX(drawTurtle, iter-1, len)
		drawTurtle.right(120)
		dragonY(drawTurtle, iter-1, len)
		
		drawTurtle.forward(len)
		updateColor(drawTurtle)
		drawTurtle.right(60)
	else:
		drawTurtle.right(120)
		drawTurtle.forward(len)
		updateColor(drawTurtle)
		drawTurtle.right(60)
	return
	
def dragonY(drawTurtle, iter, len):
	if (iter > 0):
		drawTurtle.left(120)
		drawTurtle.forward(len)
		updateColor(drawTurtle)
		
		dragonX(drawTurtle, iter-1, len)
		drawTurtle.left(60)
		dragonY(drawTurtle, iter-1, len)
	else:
		drawTurtle.left(120)
		drawTurtle.forward(len)
		updateColor(drawTurtle)
		drawTurtle.left(60)
		
	return
	
main()