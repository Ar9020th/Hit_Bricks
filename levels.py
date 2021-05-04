from brick import *
import random
def getlayoutlevel1():
    brickobjs=[]
    x=12
    y=35
    t=0
    b=Brick(ipos=x+1,jpos=y-5,strength=4,columns=10,hiddenpower=7,explode=False,israinbow=True)
    brickobjs.append(b)
    b=Brick(ipos=x+1,jpos=y+85,strength=4,columns=10,hiddenpower=7,explode=False)
    brickobjs.append(b)
    for i in range(6):
        b=Brick(ipos=x,jpos=y,strength=3,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        b=Brick(ipos=x,jpos=y+80-t,strength=3,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        b=Brick(ipos=x+2,jpos=y+80-t,strength=2,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        t+=10
        b=Brick(ipos=x+2,jpos=y,strength=2,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        x+=1
        y+=5
    x-=1
    y+=5
    for i in range(2):
        b=Brick(ipos=x,jpos=y,strength=4,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        b=Brick(ipos=x,jpos=y+10,strength=4,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        x+=1
    for i in range(2):
        b=Brick(ipos=x,jpos=y,strength=1,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        y+=10
    x-=1
    y=23
    t=0
    for i in range(8):
        b=Brick(ipos=x,jpos=y,strength=2,columns=10,hiddenpower=7,explode=True)
        brickobjs.append(b)
        b=Brick(ipos=x,jpos=y+106-t,strength=2,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        x+=1
        y+=6
        t+=12
    x-=1
    y+=4
    b=Brick(ipos=x,jpos=y,strength=3,columns=12,hiddenpower=7,explode=True)
    brickobjs.append(b)
    random.shuffle(brickobjs)
    stren=0
    for i in range(10):
        brickobjs[i].updatePower(stren)
        stren+=1
        if stren == 3:
            stren=4
        stren%=7
    return brickobjs,6

def getLayoutlevel2():
    brickobjs=[]
    x=7
    y=15
    for i in range(5):
        b=Brick(ipos=x,jpos=y,strength=2,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        b=Brick(ipos=x,jpos=y+120,strength=2,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        b=Brick(ipos=x+13,jpos=y,strength=2,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        b=Brick(ipos=x+13,jpos=y+120,strength=2,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        x+=1
    y+=10
    for i in range(11):
        b=Brick(ipos=x,jpos=y,strength=3,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        b=Brick(ipos=x+7,jpos=y,strength=3,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        y+=10
    x=7
    y=75
    for i in range(5):
        if i==0 or i==4:
            b=Brick(ipos=x,jpos=y,strength=1,columns=10,hiddenpower=7,explode=False)
            brickobjs.append(b)
        elif i==1 or i==3:
            for j in range(y-10,y+11,10):
                b=Brick(ipos=x,jpos=j,strength=1,columns=10,hiddenpower=7,explode=False)
                brickobjs.append(b)
        else:
            for j in range(y-20,y+21,10):
                b=Brick(ipos=x,jpos=j,strength=1,columns=10,hiddenpower=7,explode=False)
                brickobjs.append(b)
        x+=1
    x=20
    y=75
    for i in range(5):
        if i==0 or i==4:
            b=Brick(ipos=x,jpos=y,strength=1,columns=10,hiddenpower=7,explode=False)
            brickobjs.append(b)
        elif i==1 or i==3:
            for j in range(y-10,y+11,10):
                b=Brick(ipos=x,jpos=j,strength=1,columns=10,hiddenpower=7,explode=False)
                brickobjs.append(b)
        else:
            for j in range(y-20,y+21,10):
                b=Brick(ipos=x,jpos=j,strength=1,columns=10,hiddenpower=7,explode=False)
                brickobjs.append(b)
        x+=1
    x=13
    y=15
    for i in range(6):
        b=Brick(ipos=x,jpos=y,strength=1,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        b=Brick(ipos=x,jpos=y+120,strength=1,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        x+=1
    x=13
    y=55
    for i in range(5):
        b=Brick(ipos=x,jpos=y,strength=2,columns=10,hiddenpower=7,explode=True)
        brickobjs.append(b)
        b=Brick(ipos=x+5,jpos=y,strength=2,columns=10,hiddenpower=7,explode=True)
        brickobjs.append(b)
        y+=10
    y=65
    x=14
    for i in range(3):
        b=Brick(ipos=x,jpos=y,strength=3,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        b=Brick(ipos=x+3,jpos=y,strength=3,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        y+=10
    x=15
    y=75
    b=Brick(ipos=x,jpos=y,strength=4,columns=10,hiddenpower=7,explode=False)
    brickobjs.append(b)
    b=Brick(ipos=x+1,jpos=y,strength=4,columns=10,hiddenpower=7,explode=False)
    brickobjs.append(b)
    x=14
    y=55
    for i in range(4):
        b=Brick(ipos=x,jpos=y,strength=2,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        b=Brick(ipos=x,jpos=y+40,strength=2,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        x+=1
    
    random.shuffle(brickobjs)
    stren=0
    for i in range(10):
        brickobjs[i].updatePower(stren)
        stren+=1
        if stren == 3:
            stren=4
        stren%=7
    return brickobjs,2

def spawnbricks():
    brickobjs=[]
    y=5
    streng=1
    for i in range(15):
        b=Brick(ipos=17,jpos=y,strength=streng,columns=10,hiddenpower=7,explode=False)
        brickobjs.append(b)
        y+=10
        if streng == 1:
            streng =2
        elif streng == 2:
            streng =3
        else:
            streng=1
    return brickobjs,0

def testbrick():
    brickobjs=[]
    b=Brick(ipos=17,jpos=120,strength=1,columns=10,hiddenpower=7,explode=False)
    brickobjs.append(b)
    return brickobjs,0