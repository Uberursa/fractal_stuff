import turtle
import math

import threading

def main():
	print("dunno yet")
	
	#plan is to have 2 dragons for the base with k-curves for the leaves
	#try having the K-curves with different shades of green
	# don't know how to make the dragons interesting, may have one be brighter 
	#	than the other for some shading?
	
	#colors;
	#rightTrunk		205-133-63
	#leftTrunk		139-69-19
	#centerBranch	34-139-34
	
	turtle.bgcolor("#000000")
	turtle.screensize(canvwidth=2000, canvheight=2000)
	turtle.colormode(255)
	turtle.speed('fastest')
	
	rightTrunk = makeTurtle(205, 133, 63, 0, -30)
	leftTrunk = makeTurtle(139, 69, 19, -55, -30)
	
	leftTrunk.left(90)
	#dragonStart(leftTrunk, 7, 11, 90)
	
	rightTrunk.left(90)
	#dragonStart(rightTrunk, 7, 11, 90)
	
	centerBranch = makeTurtle(34, 139, 34, -130, 130)
	ccurve(centerBranch, 7, 14)
	
	farLeftBranch = makeTurtle(10, 110, 10, -130, 130)
	farLeftBranch.left(90)
	ccurve(farLeftBranch, 3, 28)
	
	turtle.done()
	return

#255, 0, 0. -50, 0
def makeTurtle(red, green, blue, xPos, yPos):
	drawTurtle = turtle.Turtle()
	drawTurtle.up()
	drawTurtle.setpos((xPos, yPos))
	drawTurtle.down()
	drawTurtle.speed(0)
	drawTurtle.hideturtle()
	drawTurtle.pencolor(red, green, blue)

	return drawTurtle

def updateColor(drawTurtle):
	return
	
def dragonStart(drawTurtle, iter, len, lowAngle):
	drawTurtle.forward(len)
	updateColor(drawTurtle)
	dragonX(drawTurtle, iter, len, lowAngle)
	return

def dragonX(drawTurtle, iter, len, lowAngle):
	if (iter > 0):
		dragonX(drawTurtle, iter-1, len, lowAngle)
		drawTurtle.right(180-lowAngle)
		dragonY(drawTurtle, iter-1, len, lowAngle)
		
		drawTurtle.forward(len)
		updateColor(drawTurtle)
		drawTurtle.right(lowAngle)
	else:
		drawTurtle.right(180-lowAngle)
		drawTurtle.forward(len)
		updateColor(drawTurtle)
		drawTurtle.right(lowAngle)
	return
	
def dragonY(drawTurtle, iter, len, lowAngle):
	if (iter > 0):
		drawTurtle.left(180-lowAngle)
		drawTurtle.forward(len)
		updateColor(drawTurtle)
		
		dragonX(drawTurtle, iter-1, len, lowAngle)
		drawTurtle.left(lowAngle)
		dragonY(drawTurtle, iter-1, len, lowAngle)
	else:
		drawTurtle.left(180-lowAngle)
		drawTurtle.forward(len)
		updateColor(drawTurtle)
		drawTurtle.left(lowAngle)
		
	return
	
def ccurve(drawTurtle, iter, len):
	if (iter == 0):
		drawTurtle.left(45)
		drawTurtle.forward(len)
		drawTurtle.right(90)
		drawTurtle.forward(len)
		drawTurtle.left(45)
	else:
		drawTurtle.left(45)
		ccurve(drawTurtle, iter-1, len)
		drawTurtle.right(90)
		ccurve(drawTurtle, iter-1, len)
		drawTurtle.left(45)
	return
	
main()