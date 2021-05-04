import os
from paddle import Paddle
import numpy as np
from input import *
from background import *
import sys
from brick import *
import time
from ball import *
from power import *
from levels import *
from ufo import *
def cursor_hide():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

def cursor_show():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

def movebulletsupwards(bullets):
    for b in bullets:
        if b[0]==1:
            bullets.remove(b)
        else:
            b[0]-=1
    return bullets

def checkForBulletHit(bullet,brick):
    i,j,cols=brick.getijcolumns()
    if(bullet[0]==i+1):
        if(bullet[1]>=j and bullet[1]<(j+cols)):
            return True
    return False

screen_rows=os.get_terminal_size().lines
screen_columns=os.get_terminal_size().columns
screen_rows-=10
screen_columns-=40
bgscreen=Background(screen_rows=screen_rows,screen_columns=screen_columns)
paddle=Paddle(columns=20,ipos=37,jpos=80)
brickobjarray,num_of_unbreakable=getlayoutlevel1()
for i in range(len(brickobjarray)):
    bgscreen.addBrickToScreen(brickobjarray[i])
ball=Ball(i=37,j=90,dx=-1,dy=1)
extraBalls=[]
bgscreen.addPaddleToScreen(paddle)
bgscreen.addBalltoScreen(ball)
bgscreen.printScreen()
poweruparray=[-1 for i in range(7)]
powerUps=[]
getCh=Get()
score=0
inittime=time.time()
timeplayed=0
lives=3
current_level=1
explodingbricks=[]
print("\033c")
levelstime=[-1 for i in range(3)]
triggerFall=[False for i in range(3)]
bullets=[]
newLive=False
ufolife=50
hasspawned=False
while True:
    ctime=time.time()
    if ufolife==0:
        os.system('aplay -q ./sounds/gameover.wav&') 
        print("\033c")
        print(f"You Won the Game..............Your Score {score}")
        cursor_show()
        break
    if paddle.getShootingPower() == True:
        if paddle.updateShootingInterval() == True:
            x,y,cols=paddle.getijcolumns()
            bullets.append([x-1,y])
            bullets.append([x-1,y+cols-1])
    
    if current_level==3 and ufolife==25:
        if hasspawned == False:
            brickobjarray,num_of_unbreakable=spawnbricks()
            for b in brickobjarray:
                bgscreen.addBrickToScreen(b)
            hasspawned=True

    if ufolife == 20:
        hasspawned=False
    
    if current_level==3 and ufolife==10:
        if hasspawned == False:
            for b in brickobjarray:
                bgscreen.removeBrickFromScreen(b)
            brickobjarray,num_of_unbreakable=spawnbricks()
            for b in brickobjarray:
                bgscreen.addBrickToScreen(b)
            hasspawned=True
    
    if ufolife==5:
        hasspawned=False
    
    bgscreen.removeBulletsFromScreen(bullets)
    for bul in bullets:
        for bri in brickobjarray:
            if checkForBulletHit(bul,bri) == True:
                if bri.getStrength() == 4:
                    bullets.remove(bul)
                    continue   
                bgscreen.removeBrickFromScreen(bri)
                bri.decreaseStrength()
                bgscreen.addBrickToScreen(bri)
                if bri.getStrength() == 0:
                    brickobjarray.remove(bri)
                bullets.remove(bul)
                break
    bullets=movebulletsupwards(bullets)
    bgscreen.addbulletsToScreen(bullets)
    if current_level == 3:
        bombs=ufo.getbombs()
        checkcoli,bom=paddle.checkcollisionwithbombs(bombs)
        if checkcoli == True:
            os.system('aplay -q ./sounds/losinglife.wav&')
            lives-=1
            ufo.removeCollidedBomb(bom)
        bgscreen.removeBombsFromBackground(bombs)
        ufo.movebombdown(screen_rows)
        ufo.updatetimeinterval()
        bgscreen.addBombsToBackground(bombs)
        
    if levelstime[current_level-1] == -1:
        levelstime[current_level-1]=ctime
    
    for b in brickobjarray:
        if b.getrainbow() == True:
            bgscreen.removeBrickFromScreen(b)
            b.changeStrength()
            bgscreen.addBrickToScreen(b)

    else:
        if int(ctime)-int(levelstime[current_level-1]) >=20:
            for b in brickobjarray:
                b.triggerFalling()
            triggerFall[current_level-1]=True
    if int(ctime)-int(inittime)-timeplayed:
        timeplayed+=1
    # if num_of_unbreakable>=len(brickobjarray):
    #     brickobjarray,num_of_unbreakable=getLayoutlevel2()
    if lives==0:
        os.system('aplay -q ./sounds/gameover.wav&') 
        print("\033c")
        print("Game Over")
        cursor_show()
        break

    if newLive==True:
        os.system('aplay -q ./sounds/losinglife.wav&')
        for i in range(7):
            if poweruparray[i]!=-1:
                if (i>=0 and i<=1):
                    poweruparray[i]=-1
                    bgscreen.removePaddleFromScreen(paddle)
                    paddle.restorePaddle()
                    bgscreen.addPaddleToScreen(paddle)
                elif i==2:
                    for i in range(len(extraBalls)):
                        bgscreen.removeBallFromScreen(extraBalls[i],1)
                    extraBalls=[]
                elif i==4:
                    ball.deactivatePower4()
                    for b in extraBalls:
                        b.deactivatePower4()
                elif i==5:
                    paddle.deactivatePower()
                elif i==6:
                    paddle.deactivateShootingPaddle()
        poweruparray=[-1 for i in range(7)]
        bgscreen.removeBallFromScreen(ball,1)
        i,j,col=paddle.getijcolumns()
        ball=Ball(i=37,j=j+col//2,dx=-1,dy=1)
        bgscreen.addBalltoScreen(ball)
        newLive=False
    # os.system('sleep 0.02')
    # sys.stderr.write("\x1b[2J\x1b[H")
    # time.sleep(0.02)
    for i in range(7):
        if poweruparray[i]!=-1:
            if(poweruparray[i]<ctime):
                if (i>=0 and i<=1):
                    poweruparray[i]=-1
                    bgscreen.removePaddleFromScreen(paddle)
                    paddle.restorePaddle()
                    bgscreen.addPaddleToScreen(paddle)
                elif i==2:
                    poweruparray[i]=-1
                    for i in range(len(extraBalls)):
                        bgscreen.removeBallFromScreen(extraBalls[i],1)
                    extraBalls=[]
                elif i==4:
                    poweruparray[i]=-1
                    ball.deactivatePower4()
                    for b in extraBalls:
                        b.deactivatePower4()
                elif i==5:
                    poweruparray[i]=-1
                    paddle.deactivatePower()
                elif i==6:
                    poweruparray[i]=-1
                    paddle.deactivateShootingPaddle()
    sys.stdout.write('\033[H')
    if current_level !=3:
        if paddle.getShootingPower() == True and poweruparray[6]!=-1:
            print(f"Score :{score}             TimePlayed:{timeplayed}           Lives:{lives}             Power Time Left:{int(poweruparray[6]-ctime)}")
        else:
            print(f"Score :{score}             TimePlayed:{timeplayed}           Lives:{lives}")

    else:
        if paddle.getShootingPower() == True:
            print(f"Score :{score}             TimePlayed:{timeplayed}           Lives:{lives}                 Ufo Life:{ufolife}             Power Time Left:{int(poweruparray[6]-ctime)}")
        else:
            print(f"Score :{score}             TimePlayed:{timeplayed}           Lives:{lives}                 Ufo Life:{ufolife}")

    tempexp=[]
    for expb in explodingbricks:
        ex,ey,ec=expb.getijcolumns()
        indx=0
        for b in brickobjarray:
            x,y,c=b.getijcolumns()
            if abs(x-ex)<=1:
                if abs(y-ey)<=c:
                    os.system('aplay -q ./sounds/explosion_brick.wav&') 
                    x,y,hp=b.getHiddenPower()
                    if hp!=7:
                        powerUps.append(Power(type=hp,i=x,j=y))
                    brickobjarray[indx]=-1
                    score+=5*b.getStrength()
                    b.makeStrengthZero()
                    bgscreen.addBrickToScreen(b)
                    if b.getExplode():
                        tempexp.append(b)
            indx+=1
        tempboj=[]
        for b in brickobjarray:
            if b!=-1:
                tempboj.append(b)
        brickobjarray=tempboj
    explodingbricks=tempexp
    for pu in powerUps:
        bgscreen.removePower(pu)
        i,j=pu.getij()
        dx,dy=pu.getdxdy()
        ch=bgscreen.getCharAtIJ(i+dx,j+dy)
        if(i!=screen_rows-2):
            pu.moveDown(ch,screen_columns)
            bgscreen.addPowerToBg(pu)
            x,y,type=pu.getijtype()
            px,py,pc=paddle.getijcolumns()
            if x==px:
                if y>=py and y<(py+pc):
                    os.system('aplay -q ./sounds/powerupcatch.wav&') 
                    poweruparray[type]=ctime+10
                    if type==0:
                        bgscreen.removePaddleFromScreen(paddle)
                        paddle.expandPaddle(screen_columns)
                        bgscreen.addPaddleToScreen(paddle)
                    if type==1:
                        bgscreen.removePaddleFromScreen(paddle)
                        paddle.shrinkPaddle()
                        bgscreen.addPaddleToScreen(paddle)
                    if type==2:
                        x,y=ball.getij()
                        power4=ball.getPower()
                        dx,dy=ball.getdxdy()
                        nball=Ball(i=x,j=y,dx=dx,dy=-1*dy,onPaddle=False,power4=power4)
                        bgscreen.addBalltoScreen(nball)
                        leneb=len(extraBalls)
                        extraBalls.append(nball)
                        for i in range(leneb):
                            x,y=extraBalls[i].getij()
                            dx,dy=extraBalls[i].getdxdy()
                            nball=Ball(i=x,j=y,dx=dx,dy=-1*dy,onPaddle=False,power4=power4)
                            extraBalls.append(nball)
                            bgscreen.addBalltoScreen(nball)
                    if type==4:
                        ball.activatePower4()
                        for b in extraBalls:
                            b.activatePower4()
                    if type==5:
                        paddle.activategrabPower()
                    if type==6:
                        paddle.activateShootingPaddle()
                    powerUps.remove(pu)
        else:
            powerUps.remove(pu)
        
    bgscreen.printScreen()
    cursor_hide()
    ch=input_to(getCh,timeout=0.03)
    if ch!=None:
        time.sleep(0.02)
    
    if ball.checkOnPaddle() == False:
        checkbottom=ball.collisionwithwall(screen_columns,screen_rows)
        if checkbottom==False:
            if(len(extraBalls)):
                bgscreen.removeBallFromScreen(ball,flag=1)
                ball=extraBalls[0]
                extraBalls.remove(ball)
            else:
                newLive=True
                lives-=1
                continue
        tput=ball.collisionwithpaddle(paddle=paddle)
        if tput:
            if tput == 2:
                if triggerFall[current_level-1] == True:
                    xit=0
                    for b in brickobjarray:
                        bgscreen.removeBrickFromScreen(b)
                        xit=max(xit,b.move_one_step_down())
                    
                    for b in brickobjarray:
                        bgscreen.addBrickToScreen(b)
                    
                    if xit==(paddle.geti()-1):
                        os.system('aplay -q ./sounds/gameover.wav&') 
                        print("\033c")
                        print("Game Over")
                        cursor_show()
                        break
            if current_level == 3:
                xy=ball.collisonWithUfo(ufo,screen_columns=screen_columns)
                if xy == True:
                    ufolife-=5
            rmidxs,explodeidxs,noe=ball.collisionwithbrick(brickobjarray,bgscreen)
            score+=5*noe
            if(len(explodeidxs)):
                for i in range(len(explodeidxs)):
                    explodingbricks.append(brickobjarray[explodeidxs[i]])
            if(len(rmidxs)):
                tempar=[]
                for i in range(len(rmidxs)):
                    x,y,hp=brickobjarray[rmidxs[i]].getHiddenPower()
                    brickobjarray[rmidxs[i]]=-1
                    if hp!=7:
                        powerUps.append(Power(type=hp,i=x,j=y,dy=ball.getdy()))
                for i in range(len(brickobjarray)):
                    if(brickobjarray[i]!=-1):
                        tempar.append(brickobjarray[i])
                brickobjarray=tempar
            bgscreen.removeBallFromScreen(ball,1)
            if ball.settriggermove() == 1:
                ball.moveBall()
            bgscreen.addBalltoScreen(ball)
    
    for nball in extraBalls:
        if nball.checkOnPaddle() == False:
            checkbottom=nball.collisionwithwall(screen_columns,screen_rows)
            if checkbottom==False:
                bgscreen.removeBallFromScreen(nball,flag=1)
                extraBalls.remove(nball)
                continue
            tput=nball.collisionwithpaddle(paddle=paddle)
            if tput:
                rmidxs,explodeidxs,noe=nball.collisionwithbrick(brickobjarray,bgscreen)
                score+=5*noe
                if(len(explodeidxs)):
                    for i in range(len(explodeidxs)):
                        explodingbricks.append(brickobjarray[explodeidxs[i]])
                if(len(rmidxs)):
                    tempar=[]
                    for i in range(len(rmidxs)):
                        x,y,hp=brickobjarray[rmidxs[i]].getHiddenPower()
                        brickobjarray[rmidxs[i]]=-1
                        if hp!=7:
                            powerUps.append(Power(type=hp,i=x,j=y,dy=nball.getdy()))
                    for i in range(len(brickobjarray)):
                        if(brickobjarray[i]!=-1):
                            tempar.append(brickobjarray[i])
                    brickobjarray=tempar
                bgscreen.removeBallFromScreen(nball,1)
                nball.moveBall()
                bgscreen.addBalltoScreen(nball)

    if ch==' ':
        if ball.toggleOnPaddle() == True:
            bgscreen.removeBallFromScreen(ball,2)
            ball.moveBall()
            bgscreen.addBalltoScreen(ball)
        for b in extraBalls:
            if b.toggleOnPaddle() == True:
                bgscreen.removeBallFromScreen(b,2)
                b.moveBall()
                bgscreen.addBalltoScreen(b)

    if ch=='a':
        # time.sleep(0.02)
        bgscreen.removePaddleFromScreen(paddle)
        if current_level == 3:
            bgscreen.clearUFO(ufo)
            ufo.updatej(screen_columns,-1)
            bgscreen.addUfoToBackground(ufo)
        if paddle.moveleft() == True:
            bgscreen.addPaddleToScreen(paddle)
            if ball.checkOnPaddle() == True:
                ball.shiftBall(k=-1)
                bgscreen.addBalltoScreen(ball)
        else:
            bgscreen.addPaddleToScreen(paddle)
    
    if ch=='d':
        # time.sleep(0.02)
        bgscreen.removePaddleFromScreen(paddle)
        if current_level==3:
            bgscreen.clearUFO(ufo)
            ufo.updatej(screen_columns,1)
            bgscreen.addUfoToBackground(ufo)
        if paddle.moveright(screen_columns) == True:
            bgscreen.addPaddleToScreen(paddle)
            if ball.checkOnPaddle() == True:
                ball.shiftBall(k=1)
                bgscreen.addBalltoScreen(ball)
        else:
            bgscreen.addPaddleToScreen(paddle)

    if ch=='q':
        cursor_show()
        break

    if ch=='l':
        if current_level==1:
            current_level=2
            bgscreen.clearbackground()
            brickobjarray,num_of_unbreakable=getLayoutlevel2()
            paddle=Paddle(columns=20,ipos=37,jpos=80)
            for i in range(len(brickobjarray)):
                bgscreen.addBrickToScreen(brickobjarray[i])
            ball=Ball(i=37,j=90,dx=-1,dy=1)
            extraBalls=[]
            bgscreen.addPaddleToScreen(paddle)
            bgscreen.addBalltoScreen(ball)
            poweruparray=[-1 for i in range(7)]
            powerUps=[]
        
        elif current_level == 2:
            current_level=3
            ufo=UFO(10,80)
            bgscreen.clearbackground()
            bgscreen.addUfoToBackground(ufo)
            paddle=Paddle(columns=20,ipos=37,jpos=80)
            ball=Ball(i=37,j=90,dx=-1,dy=1)
            extraBalls=[]
            bgscreen.addPaddleToScreen(paddle)
            bgscreen.addBalltoScreen(ball)
            poweruparray=[-1 for i in range(7)]
            powerUps=[]
            brickobjarray=[]
            explodingbricks=[]
            num_of_unbreakable=0

    sys.stdin.flush()
    sys.stdout.flush()
    # time.sleep(0.02)
