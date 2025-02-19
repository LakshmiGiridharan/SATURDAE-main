import turtle as t


# x - x coordinate in pixels
# y - y coordinate in pixels
# c - colour

def bed(x, y, z, c):
    if c == 1:
        t.color('white')
    elif c == 2:
        t.color('green')
    else:
        t.color('black')
    t.speed(8)
    t.pensize(1)
    t.bgcolor('white')
    t.up()
    t.home()
    t.setx(x)
    t.sety(y)
    t.left(90 - z)
    t.down()
    t.forward(70)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.up()
    t.forward(55)
    t.right(90)
    t.forward(7)
    t.left(90)
    t.down()
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.up()
    t.backward(26)
    t.right(90)
    t.down()
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.up()
    t.forward(33)
    t.right(90)
    t.backward(5)
    t.right(90)
    t.down()
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(135)
    t.forward(14)
    t.up()
    t.hideturtle()


def sofa(x, y, z, c):
    t.speed(8)
    t.pensize(1)
    t.bgcolor('white')
    if c == 1:
        t.color('white')
    elif c==2:
        t.color('green')
    else:
        t.color('black')
    t.up()
    t.home()
    t.setx(x)
    t.sety(y)
    t.left(90 - z)
    t.down()
    t.forward(20)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(50)
    t.up()
    t.backward(25)
    t.right(90)
    t.down()
    t.forward(20)
    t.setx(x)
    t.sety(y)
    t.forward(20)
    t.down()
    t.forward(5)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(5)
    t.up()
    t.backward(5)
    t.left(90)
    t.down()
    t.forward(5)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(5)
    t.up()
    t.forward(50)
    t.down()
    t.forward(5)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(5)
    t.up()
    t.hideturtle()
   
   
# window
def window(x, y, z, c):
    t.speed(8)
    t.pensize(2)
    t.bgcolor('white')
    if c == 1:
        t.color('white')
    elif c == 2:
        t.color('green')
    else:
        t.color('orange')
    t.up()
    t.home()
    t.setx(x)
    t.sety(y)
    t.left(90 - z)
    t.down()
    t.backward(4)
    t.up()
    t.forward(2)
    t.down()
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(2)
    t.backward(4)
    t.up()
    t.hideturtle()
  
# table
def table(x, y, z, c):
    if c == 1:
        t.color('white')
    elif c == 2:
        t.color('green')
    else:
        t.color('black')
    t.speed(8)
    t.pensize(1)
    t.bgcolor('white')
    t.up()
    t.home()
    t.setx(x)
    t.sety(y)
    t.left(90 - z)
    t.forward(15)
    t.right(90)
    t.forward(15)
    t.left(90)
    t.down()
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.up()
    t.right(90)
    t.forward(5)
    t.left(90)
    t.down()
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.up()
    t.forward(12)
    t.right(90)
    t.down()
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(12)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.down()
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.up()
    t.forward(12)
    t.right(90)
    t.down()
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(12)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.down()
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.up()
    t.forward(12)
    t.right(90)
    t.down()
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(12)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.down()
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.up()
    t.forward(12)
    t.right(90)
    t.down()
    t.forward(20)
    t.up()
    t.hideturtle()


# door
def door(x, y, z, c):
    t.speed(8)
    t.pensize(2)
    t.bgcolor('white')
    if c == 1:
        t.color('white')
    elif c == 2:
        t.color('green')
    else:
        t.color('orange')
    t.up()
    t.home()
    t.setx(x)
    t.sety(y)
    t.right(90 - z)
    t.down()
    t.forward(25)
    t.left(90)
    t.circle(25, extent=90)
    t.left(90)
    t.forward(25)
    t.up()
    t.hideturtle()


def tv(x, y, z, c):
    t.speed(8)
    t.pensize(1)
    t.bgcolor('white')
    if c == 1:
        t.color('white')
    elif c == 2:
        t.color('green')
    else:
        t.color('black')
    t.up()
    t.home()
    t.setx(x)
    t.sety(y)
    t.left(90 - z)
    t.down()
    t.forward(10)
    t.right(90)
    t.forward(45)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(45)
    t.right(90)
    t.up()
    t.forward(7)
    t.right(90)
    t.forward(5)
    t.down()
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(35)
    t.up()
    t.backward(10)
    t.left(35)
    t.down()
    t.forward(8)
    t.up()
    t.backward(8)
    t.right(35)
    t.backward(15)
    t.left(145)
    t.down()
    t.forward(8)
    t.up()
    t.hideturtle()
    
    
def singlebed(x, y, z, c):
    if c == 1:
        t.color('white')
    elif c == 2:
        t.color('green')
    else:
        t.color('black')
    t.speed(8)
    t.pensize(1)
    t.bgcolor('white')
    t.up()
    t.home()
    t.setx(x)
    t.sety(y)
    t.left(90 - z)
    t.down()
    t.forward(60)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.up()
    t.forward(45)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.down()
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(20)
    t.up()
    t.backward(15)
    t.left(90)
    t.forward(5)
    t.down()
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(135)
    t.forward(14)
    t.left(45)
    t.forward(20)
    t.up()
    t.hideturtle()
    
    
def sidetable(x, y, z, c):
    t.speed(8)
    t.pensize(1)
    t.bgcolor('white')
    if c == 1:
        t.color('white')
    elif c == 2:
        t.color('green')
    else:
        t.color('black')
    t.up()
    t.home()
    t.setx(x)
    t.sety(y)
    t.left(90 - z)
    t.forward(2)
    t.down()
    t.forward(15)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(25)
    t.up()
    t.backward(3)
    t.left(90)
    t.down()
    t.forward(2)
    t.left(90)
    t.forward(19)
    t.left(90)
    t.forward(2)
    t.up()
    t.hideturtle()


def bathroom(x, y, z):
    t.setx(x)
    t.sety(y)
    t.speed(8)
    t.pensize(1)
    t.color('black')
    t.down()
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(18)
    t.left(90)
    t.forward(5)
    t.left(90)
    t.forward(17)
    t.left(90)
    t.up()
    t.forward(5)
    t.down()
    t.forward(15)
    t.circle(8, extent=180)   
    t.forward(15)
    t.up()
    t.left(90)
    t.forward(12)
    t.left(90)
    t.forward(3)
    t.down()
    t.forward(12)
    t.circle(4, extent=180)
    t.forward(12)
    t.left(90)
    t.forward(9)
    t.up()
    t.hideturtle()
    