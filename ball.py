import os
class Ball:
    def __init__(self,i,j,dx,dy,onPaddle=True,power4=False):
        self.__i=i
        self.__j=j
        self.__dx=dx
        self.__dy=dy
        self.__onPaddle=onPaddle
        self.__power4=power4
        self.__triggermove=0
        self.__updatedxdy=False
        self.__updatedxdyufo=False
    
    def settriggermove(self):
        self.__triggermove+=1
        self.__triggermove%=2
        return self.__triggermove 
    
    def moveBall(self):
        self.__i+=self.__dx
        self.__j+=self.__dy
    
    def getij(self):
        return self.__i,self.__j
    
    def getdxdy(self):
        return self.__dx,self.__dy
    
    def checkOnPaddle(self):
        return self.__onPaddle
    
    def shiftBall(self,k):
        self.__j+=k
    
    def toggleOnPaddle(self):
        if self.__onPaddle==False:
            return False
        self.__onPaddle=False
        return True
    
    def collisionwithwall(self,columns,rows):
        if self.__updatedxdy == True:
            self.__updatedxdy=False
            return -1
        self.__updatedxdy=True
        if self.__i == 1:
            self.__dx=-1*self.__dx
        if self.__i == rows-2:
            return False
        if self.__j == 1 or self.__j == columns-2:
            self.__dy=-1*self.__dy
        return True
    
    def collisionwithpaddle(self,paddle):
        if self.__updatedxdy == True:
            self.__updatedxdy=False
            return -1
        self.__updatedxdy=True
        pi,pj,pc=paddle.getijcolumns()
        grabPower=paddle.getGrabPower()
        if self.__i==pi:
            if self.__j >=pj and self.__j < (pj+pc):
                if(grabPower):
                    self.__onPaddle=True
                    self.__dx=-1*self.__dx
                    return 0
                else:
                    pos=pj+pc//2
                    self.__dx=-1*self.__dx
                    if(self.__j < pos):
                        # self.__dx=-1*self.__dx
                        self.__dy=-1
                    else:
                        self.__dy=1
                    return 2
        return 1
    
    def collisionwithbrick(self,brickarray,bg):
        if self.__updatedxdy == True:
            self.__updatedxdy=False
            return [],[],0
        self.__updatedxdy=True
        indx=[]
        explodeidxs=[]
        idx=0
        noe=0
        for brick in brickarray:
            b,s,i,j=brick.getBrick()
            if self.__i == i-1 or self.__i == i+1:
                if self.__j>=j and self.__j<(j+len(b)):
                    noe+=1
                    if self.__power4:
                        if brick.getExplode():
                            explodeidxs.append(idx)
                            noe+=brick.getStrength()-1                            
                        brick.makeStrengthZero()
                        bg.addBrickToScreen(brick)
                        indx.append(idx)
                    else:
                        if brick.getExplode():
                            explodeidxs.append(idx)
                            noe+=brick.getStrength()-1                            
                            brick.makeStrengthZero()
                            if(s>1):
                                indx.append(idx)
                        else:
                            if s!=4:
                                os.system('aplay -q ./sounds/collisionballwithbrick.wav&')                           
                                brick.decreaseStrength()
                        self.__dx=-1*self.__dx
                        if brick.getrainbow() == True:
                            brick.togglerainbow()
                        bg.addBrickToScreen(brick)
                        if(s==1):
                            indx.append(idx)
                elif abs(self.__j-j)==1:
                    noe+=1
                    if self.__power4:
                        if brick.getExplode():
                            explodeidxs.append(idx)
                            noe+=brick.getStrength()-1                            
                        brick.makeStrengthZero()
                        if brick.getrainbow() == True:
                            brick.togglerainbow()
                        bg.addBrickToScreen(brick)
                        indx.append(idx)
                    else:
                        if brick.getExplode():
                            explodeidxs.append(idx)
                            noe+=brick.getStrength()-1                            
                            brick.makeStrengthZero()
                            if(s>1):
                                indx.append(idx)
                        else:
                            if s!=4:
                                os.system('aplay -q ./sounds/collisionballwithbrick.wav&')                             
                                brick.decreaseStrength()                            
                        self.__dy=-1*self.__dy
                        self.__dx=-1*self.__dx
                        if brick.getrainbow() == True:
                            brick.togglerainbow()
                        bg.addBrickToScreen(brick)
                        if(s==1):
                            indx.append(idx)
            elif self.__i == i:
                if self.__j==j-1 or self.__j==(j+len(b)):
                    noe+=1
                    if self.__power4:
                        if brick.getExplode():
                            explodeidxs.append(idx)
                            noe+=brick.getStrength()-1                            
                        brick.makeStrengthZero()
                        if brick.getrainbow() == True:
                            brick.togglerainbow()
                        bg.addBrickToScreen(brick)
                        indx.append(idx)
                    else:
                        if brick.getExplode():
                            explodeidxs.append(idx)
                            noe+=brick.getStrength()-1                            
                            brick.makeStrengthZero()
                            if(s>1):
                                indx.append(idx)
                        else:
                            if s!=4:
                                os.system('aplay -q ./sounds/collisionballwithbrick.wav&')                            
                                brick.decreaseStrength()                            
                        self.__dy=-1*self.__dy
                        if brick.getrainbow() == True:
                            brick.togglerainbow()
                        bg.addBrickToScreen(brick)
                        if(s==1):
                            indx.append(idx)
            idx+=1
            
        return indx,explodeidxs,noe
    
    def activatePower4(self):
        self.__power4=True
    
    def deactivatePower4(self):
        self.__power4=False
    
    def getPower(self):
        return self.__power4
    
    def getdy(self):
        return self.__dy
    
    def collisonWithUfo(self,ufo,screen_columns):
        if self.__updatedxdyufo == True:
            self.__updatedxdyufo=False
            return -1
        self.__updatedxdyufo=True
        x,y,ufo=ufo.getijufo()
        f=open('adwqw.txt','a')
        f.write(f'{x}\n')
        f.write(f'{self.__i}\n')
        f.write(f'..........\n')
        if self.__i == x-1:
            if self.__j >=(y+6) and self.__j<=(y+14):
                if self.__dx==-1 and self.__dy==-1:
                    self.__dy=1
                elif self.__dx==1 and self.__dy==1:
                    self.__dx=-1
                elif self.__dx==1 and self.__dy==-1:
                    self.__dy=1
                else:
                    self.dy=-1
                return True
        elif (self.__i==(x+4)) or (self.__i==(x+2)):
            if self.__j>y and self.__j<=(y+21):
                self.__dx=-1*self.__dx
                return True
        
        elif self.__i == (x+1):
            if self.__j == y+6:
                self.__dy=-1*self.__dy
                return True
        
        elif self.__i == (x+3):
            if self.__j==max(1,y-1) or self.__j==min(screen_columns-2,y+21):
                self.__dy=-1*self.__dy
                return True
        return False




    


            
