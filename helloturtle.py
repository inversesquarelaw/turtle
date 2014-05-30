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
    myTurtle.pensize(points[2][0])
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.pencolor('black')
    myTurtle.pensize(1)

def spiralHelper(lineLen, myTurtle):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        spiralHelper(lineLen-5, myTurtle)

def drawSpiral(points, color, myTurtle):
    myTurtle.pencolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    spiralHelper(points[1][0], myTurtle)
    myTurtle.pencolor('black')

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
    
    #           x1, y1     x2, y2  ,thickness
    myLine = [[-400,400],[-300,300],[5]]
    drawLine(myLine, 'blue', myTurtle)

    myTriangle = [[-400,-300],[-400,-250],[-350,-200]]
    drawTriangle(myTriangle, 'black', myTurtle)

    #            start   , length
    mySpiral = [[300,-300],[100]]
    drawSpiral(mySpiral, 'black', myTurtle)

    myWin.exitonclick()

main()
