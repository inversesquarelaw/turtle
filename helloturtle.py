import turtle

def drawTriangle(points,color,myTurtle):
    myTurtle.pencolor(color)
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()
    myTurtle.pencolor('black')

def drawQuad(points, color, myTurtle):
    myTurtle.pencolor(color)
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[3][0],points[3][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()
    myTurtle.pencolor('black')

def drawCircle(points, color, myTurtle):
    myTurtle.pencolor(color)
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.circle(points[0][2])
    myTurtle.end_fill()
    myTurtle.pencolor('black')

def drawLine(points, color, myTurtle):
    myTurtle.pencolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.goto(points[1][0],points[1][1])

def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()

    #            corner 1, corner 2, corner 3
    myTriangle = [[-100,-50],[0,100],[100,-50]]
    drawTriangle(myTriangle, 'black', myTurtle)

    #         bottom left, top left, top right, bottom right
    myQuad = [[-200,-100],[-200,100],[-100,100],[-100,-100]]
    drawQuad(myQuad, 'green', myTurtle)

    #           x,   y, , radius
    myCircle = [[100, 100, 150]]
    drawCircle(myCircle, 'red', myTurtle)
    
    #           x1, y1     x2, y2
    myLine = [[-400,400],[-300,300]]
    drawLine(myLine, 'blue', myTurtle)

    myWin.exitonclick()

main()
