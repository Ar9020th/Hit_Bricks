from colorama import Fore as fg,Back as bg,Style as style
class Brick:
    def __init__(self,ipos,jpos,strength,columns,hiddenpower,explode=False,israinbow=False):
        self.__i=ipos
        self.__j=jpos
        self.__strength=strength
        self.__hiddenpower=hiddenpower
        self.__explode=explode
        self.__brick=[]
        self.__startfall=False
        self.__y=0
        self.__rainbow=israinbow
        for i in range(columns):
            self.__brick.append(' ')
    
    def getBrick(self):
        return self.__brick,self.__strength,self.__i,self.__j
    
    def decreaseStrength(self):
        self.__strength-=1
        # if(self.__strength == 0):
        #     if(self.__hiddenpower!=6):
    
    def getHiddenPower(self):
        return self.__i,self.__j,self.__hiddenpower
    
    def makeStrengthZero(self):
        self.__strength=0
    
    def getExplode(self):
        return self.__explode
    
    def getijcolumns(self):
        return self.__i,self.__j,len(self.__brick)
    
    def getStrength(self):
        return self.__strength
    
    def triggerFalling(self):
        self.__startfall=True
    
    def move_one_step_down(self):
        self.__i+=1
        return self.__i
    
    def changeStrength(self):
        if self.__strength==1:
            self.__strength=2
        elif self.__strength==2:
            self.__strength=3
        else:
            self.__strength=1
        
    def togglerainbow(self):
        self.__rainbow=False
    
    def getrainbow(self):
        return self.__rainbow
    
    def updatePower(self,stren):
        self.__hiddenpower=stren
