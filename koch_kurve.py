import turtle
import math
# this would be better as a part of the turtle object
redFlag = False
greenFlag = False
blueFlag = False

def main():
	toFile("test")

	turtle.bgcolor("#000000")
	turtle.screensize(canvwidth=2000, canvheight=500)
	turtle.colormode(255)
	
	drawTurtle = turtle.Turtle()
	drawTurtle.up()
	drawTurtle.setpos((-50, 0))
	drawTurtle.down()
	drawTurtle.speed(0)
	drawTurtle.pencolor((240, 10, 100))
	drawTurtle.hideturtle()
	
	kochLine(200, 1, drawTurtle)
	drawTurtle.right(120)
	
	kochLine(200, 2, drawTurtle)
	drawTurtle.right(120)
	
	kochLine(200, 3, drawTurtle)
	drawTurtle.right(120)
	
	turtle.done()
	return
	
def updateColor(drawTurtle):
	currentColor = drawTurtle.pencolor()
	global redFlag
	global greenFlag
	global blueFlag

	
	if (currentColor[0] <= 10 and not redFlag):
		redFlag = True
		toFile("red 10")
	elif (currentColor[0] >= 240 and redFlag):
		redFlag = False
		toFile("red 240")
	
	if (currentColor[1] <= 10 and not greenFlag):
		greenFlag = True
	elif (currentColor[1] >= 240 and greenFlag):
		greenFlag = False
	
	if (currentColor[2] <= 10):
		blueFlag = True
	elif (currentColor[2] >= 240):
		blueFlag = False
		
	if (redFlag):
		currentColor = (currentColor[0] + 10, currentColor[1], currentColor[2])
		toFile(str(currentColor[0]))
	else:
		currentColor = (currentColor[0] - 10, currentColor[1], currentColor[2])
		toFile(str(currentColor[0]))
		
	if (greenFlag):
		currentColor = (currentColor[0], currentColor[1] + 10, currentColor[2])
	else:
		currentColor = (currentColor[0], currentColor[1] - 10, currentColor[2])

	if (blueFlag):
		currentColor = (currentColor[0], currentColor[1], currentColor[2] + 10)
	else:
		currentColor = (currentColor[0], currentColor[1], currentColor[2] - 10)
	
	drawTurtle.pencolor(currentColor)
	return
	
def kochLine(len, iter, drawTurtle):
	if (iter > 0):
		kochLine(len/3, iter-1, drawTurtle)
		
		drawTurtle.left(60)
		kochLine(len/3, iter-1, drawTurtle)
		
		drawTurtle.right(120)
		kochLine(len/3, iter-1, drawTurtle)
		
		drawTurtle.left(60)
		kochLine(len/3, iter-1, drawTurtle)
	else:
		drawTurtle.forward(len/3)
		
		drawTurtle.left(60)
		updateColor(drawTurtle)
		drawTurtle.forward(len/3)
	
		drawTurtle.right(120)
		updateColor(drawTurtle)
		drawTurtle.forward(len/3)
		
		drawTurtle.left(60)
		updateColor(drawTurtle)
		drawTurtle.forward(len/3)
	
	return
	
def toFile(str):
	with open("out.txt", "a") as file:
		file.write(str)
	
	return
	
main()