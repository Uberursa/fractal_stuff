import turtle

redIter = 5
greenIter = 5
blueIter = 5


def main():
	turtle.bgcolor("#000000")
	turtle.screensize(canvwidth=2000, canvheight=2000)
	turtle.colormode(255)
	
	drawTurtle = turtle.Turtle()
	drawTurtle.up()
	drawTurtle.setpos((-50, 0))
	drawTurtle.down()
	drawTurtle.speed(0)
	drawTurtle.hideturtle()
	drawTurtle.pencolor(50, 0, 200)
	
	drawTurtle.left(90)
	
	ccurve(drawTurtle, 8, 10, 45)
	return
	
def ccurve(drawTurtle, iter, len, lowAngle):
	if (iter == 0):
		drawTurtle.left(lowAngle)
		#stepTurtle(drawTurtle, len)
		drawTurtle.forward(len)
		drawTurtle.right(135-lowAngle)
		#stepTurtle(drawTurtle, len)
		drawTurtle.forward(len)
		drawTurtle.left(lowAngle)
	else:
		drawTurtle.left(lowAngle)
		ccurve(drawTurtle, iter-1, len, lowAngle)
		drawTurtle.right(135-lowAngle)
		ccurve(drawTurtle, iter-1, len, lowAngle)
		drawTurtle.left(lowAngle)
	return
	
def stepTurtle(drawTurtle, len):
	currentColor = drawTurtle.pencolor()
	global redIter
	global greenIter
	global blueIter

	if (currentColor[0] + redIter > 255 or currentColor[0] + redIter < 0):
		redIter *= -1
	else:
		currentColor = (currentColor[0] + redIter, currentColor[1], currentColor[2])
		
	if (currentColor[1] + greenIter > 255 or currentColor[1] + greenIter < 0):
		greenIter *= -1
	else:
		currentColor = (currentColor[0], currentColor[1] + greenIter, currentColor[2])

	if (currentColor[2] + blueIter > 255 or currentColor[2] + blueIter < 0):
		blueIter *= -1
	else:
		currentColor = (currentColor[0], currentColor[1], currentColor[2] + blueIter)
	
	drawTurtle.pencolor(currentColor)
	drawTurtle.forward(len)
	return
	
main()