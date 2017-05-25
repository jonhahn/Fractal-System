'''
Drawing a Koch snowflake 
'''


import turtle as tu
import math

def Koch(length):
    """draw a Koch fractal curve recursively"""
    if length <= 3 :
        tu.fd(length)
        return
    Koch(length/3)
    tu.lt(60)
    Koch(length/3)
    tu.rt(120)
    Koch(length/3)
    tu.lt(60)
    Koch(length/3)
    return


def Solution(length, draw):

    #face up at start
    if length >=.1:
        #Draw right third
        Solution(length/3, 0)

        if draw:
            tu.dot(8,'red')
        #Draw left third
        Solution2(length, draw)
    return

def Solution2(length, draw):
    if draw:
        tu.pendown()
    else:
        tu.penup()
    if length >=.1:
        #Draw middle third
        tu.left(90)
        tu.fd(2*length/9)
        tu.right(90)
        tu.fd(math.sqrt(3.0)/3.0*2.0/9.0 * length)

        Solution2(length/3, draw)


def DrawAxes(length):
    tu.speed(0)
    # move to starting position
    tu.penup()
    tu.backward(length/2.0)
    tu.right(90)
    tu.fd(length/3.0)
    tu.left(90)
    tu.pendown()


    #draw axes
    tu.left(90)
    tu.color('gray')
    tu.fd(length)
    tu.left(180)
    tu.fd(length*1.5)
    tu.backward(length*.5)
    tu.left(90)
    tu.fd(length*1.5)
    tu.left(180)
    tu.fd(length*.5)
    tu.left(90)
    tu.fd(10)
    tu.backward(20)
    tu.fd(10)
    tu.right(90)
    tu.fd(length*1.5)
    tu.backward(length*.5)

    tu.left(180)


def DrawArrows(length):
    #face up to start
    tu.color('black')
    DrawArrow(-length/8, -10 -length/3.0, 90)
    DrawArrow(0, -10 - length/3.0, 90)
    DrawArrow(length/8, -10 - length/3.0, 90)
    
    DrawArrow(-length/4, -40 -length/3.0, 90)
    DrawArrow(-length/8, -40 -length/3.0, 90)
    DrawArrow(0, -40 - length/3.0, 90)
    DrawArrow(length/8, -40 - length/3.0, 90)
    DrawArrow(length/4, -40 -length/3.0, 90)

    DrawArrow(0, -length/3.0 + length/3.0, 180)
    DrawArrow(-length/3.0, -length/3.0 + length/3.0, 180)
    DrawArrow(-length/6.0, -length/3.0 + length/3.0, 180)
    DrawArrow(length/6.0, -length/3.0 + length/3.0, 180)
    DrawArrow(length/3.0, -length/3.0 + length/3.0, 180)
    DrawArrow(length/3.0, -length/3.0 + length/4.0, 180)
    DrawArrow(-length/3.0, -length/3.0 + length/4.0, 180)

def DrawArrow(xc, yc, head):
    tu.seth(head)
    tu.penup()
    tu.setx(xc)
    tu.sety(yc)
    tu.pendown()
    tu.fd(20)
    tu.left(135)
    tu.fd(5)
    tu.right(180)
    tu.fd(5)
    tu.right(90)
    tu.fd(5)



tu.title('Koch fractal curve')
length = 600.0

DrawAxes(length)


tu.color('black')
Koch(length)
tu.dot(8, 'blue')

'''
tu.left(90)
tu.color('blue')
Solution(length, 1)
tu.dot(8,'red')
tu.left(90)
tu.fd(100)
'''

DrawArrows(length)
tu.penup()
tu.setx(-500)
tu.done()



