import math
from tkinter import *
from random import *
def nextpoint(xdep,ydep,radius,length):
"""
Calculate the next point of the tree by using the trig formula for sinus and cosinus
sin = OppositeSide/Hypotenuse
cos = AdjacentSide/Hypotenuse
Arguments :
- Coordinate of start : xdep,ydep [int,int]
- angle wanted : radius [int]
- length of the branch : length [float rounded in int]
Returns:
- Coordinate of the new point [int,int]
"""
    y2 = math.sin(math.radians(radius+90))*length + ydep
    x2 = math.cos(math.radians(radius+90))*length + xdep
    return x2,y2
def color(last):
"""
Pick a color by increasing the amount of green in the precedent color
It use Hexa to represent colors
Arguments :
- Last color to increment : last [string]
Returns:
- New color in hex [string]
"""
    chaine = last
    nbl = chaine[3]+chaine[4]
    nb=int(nbl)+4
    res = chaine[0]+chaine[1]+chaine[2]+str(nb)+chaine[5]+chaine[6]
    return res

def generation(x1,y1,x2,y2,radius,length,width,coul):
"""
Recursive function who make everything work.
It include a bit of random in the choice of the angle and make sure the length stay an integer.
Then it call the nextpoint function for the two angle chosen and draw the previous line
To go from a generation to an other, it divide the length and the width of a branch by 1.5 and call the color function.
Arguments :
- Coordinate of the start point : x1,y1 [int,int]
- Coordinate of the end point : x2,y2 [int,int]
- Angle of the last segment : radius [int]
- length of the branch drawn  : length [float]
- width of the branch drawn : width [float]
- color of the branch drawn : coul [string]
Returns :
- Nothing but a 0 to stop the Recursion
- As side effect, it draw on the canvas
"""
    if width <= 1:
        return 0
    rand = randint(0,20)
    randbin = randint(0,1)
    if randbin==1:
        radius+=rand
    else:
        radius-=rand
    x3,y3=nextpoint(x2,y2,radius-45,int(length))
    x4,y4=nextpoint(x2,y2,radius+45,int(length))
    drawline(x1,y1,x2,y2,coul,width)
    nextcoul = color(coul)
    generation(x2,y2,x3,y3,radius-45,length/1.5,width-1.5,nextcoul)
    generation(x2,y2,x4,y4,radius+45,length/1.5,width-1.5,nextcoul)

def generateTree(xdep,couldep,widthdep,lengthdep):
"""
Start the recursion with the parameters wanted
Arguments :
- Position wanted on the X-Axis : xdep [int]
- Color of start wanted: couldep [string]
- Width of the trunk : widthdep [int]
- length of the trunk : lengthdep [int]
Returns :
- Nothing.
"""
    generation(600,xdep,600-lengthdep,xdep,90,lengthdep,widthdep,couldep)
def generateForest(nbtree):
"""
Start the forest generation
It choose random position for the tree, a random start color in a array and a random length of start
To avoid the superposition of tree, the precedent position of start are locked in a list
Arguments :
- Number of tree wanted : nbtree [int]
"""
    tabTree = []
    colors = ["#591002","#00108e","#e2103f","#34103f"]
    for i in range(0,nbtree):
        xdep = randrange(100,1100,200)
        while xdep in tabTree:
            xdep = randrange(100,1100,200)
        tabTree.append(xdep)
        color = randint(0,3)
        length = randint(60,100)
        generateTree(xdep,colors[color],20,length)
def middlepoint(xdep,ydep,xarr,yarr):
"""
Calculate a point in the middle of a segment to create a slight curve in the branch
It put a bit of random in the position of the point.
Arguments :
- Start coordinate of the branch : xdep, ydep [int,int]
- End coordinate of the branch : xarr, yarr [int,int]
Returns :
- Coordinate of the middlepoint
"""
    ymid=int((yarr+ydep)/2)
    xmid = int((xarr+xdep)/2)
    xrand = xmid+randrange(-10,10)
    yrand = ymid+randrange(-10,10)
    return xrand,yrand

def drawline(y1,x1,y2,x2,coul,w):
"""
Draw a line in a canvas,
It go through 3 point, the start, the end and a point in the middle caluclated with the function middlepoint
Arguments :
- Coordinate of start : x1, y1 [int,int]
- Coordinate of end : x2, y2 [int,int]
- Color chosen : coul [string]
- width of the branch : w [float]
Returns :
- Side Effect : draw a line in the canvas, and update the display
"""
    x3,y3=middlepoint(x1,y1,x2,y2)
    can1.create_line(x1,y1,x3,y3,x2,y2,width=w,fill=coul,smooth=True)
    can1.update()
def start():
"""
callBack for the button "Generate"
The number of tree wanted is written in the code
"""
    can1.delete("all")
    generateForest(4)
    print("done")
# Main Program
fen1 = Tk()

can1 = Canvas(fen1,bg='#000015',height=600,width=1200)
can1.pack()
bou2 = Button(fen1,text='Generate',command=start)
bou2.pack(side = LEFT)

fen1.mainloop()
