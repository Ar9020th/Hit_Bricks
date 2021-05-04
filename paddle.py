class Paddle:

    def __init__(self,columns,ipos,jpos):
        self.__paddle=[]
        self.__i=ipos
        self.__j=jpos
        self.__columns=columns
        self.__paddle=[[' ' for k in range(columns)] for l in range(2)]
        for i in range(columns):
            self.__paddle[0][i]=self.__paddle[1][i]='_'
        self.__paddle[1][0]=self.__paddle[1][columns-1]='|'
        self.__grabPower=False
        self.__shootinginterval=0
        self.__shootingPower=False
    
    def getpaddle(self):
        return self.__paddle
    
    def getijcolumns(self):
        return self.__i,self.__j,self.__columns
    
    def moveleft(self):
        if self.__j != 1:
            self.__j-=1
            return True
        return False

    def moveright(self,cols):
        cols-=1
        cols-=self.__columns
        if self.__j != cols:
            self.__j+=1
            return True
        return False
    
    def expandPaddle(self,sc):
        ip=self.__j
        fp=self.__j+self.__columns-1
        self.__columns=30
        ef=min(sc-2,fp+5)
        eg=max(1,ip-5)
        if eg==1:
            self.__j=1
        
        elif ef==sc-2:
            self.__j=ef-29
        
        else:
            self.__j=eg
            
        self.__paddle=[[' ' for k in range(self.__columns)] for l in range(2)]
        for i in range(self.__columns):
            self.__paddle[0][i]=self.__paddle[1][i]='_'
        self.__paddle[1][0]=self.__paddle[1][self.__columns-1]='|'
    
    def shrinkPaddle(self):
        ip=self.__j+4
        self.__columns=12
        self.__paddle=[[' ' for k in range(self.__columns)] for l in range(2)]
        for i in range(self.__columns):
            self.__paddle[0][i]=self.__paddle[1][i]='_'
        self.__paddle[1][0]=self.__paddle[1][self.__columns-1]='|'

    def restorePaddle(self):
        self.__columns=20
        self.__j+=5
        self.__paddle=[[' ' for k in range(self.__columns)] for l in range(2)]
        for i in range(self.__columns):
            self.__paddle[0][i]=self.__paddle[1][i]='_'
        self.__paddle[1][0]=self.__paddle[1][self.__columns-1]='|'
    
    def activategrabPower(self):
        self.__grabPower=True
    
    def deactivatePower(self):
        self.__grabPower=False
    
    def getGrabPower(self):
        return self.__grabPower
    
    def geti(self):
        return self.__i
    
    def checkcollisionwithbombs(self,bombs):
        for b in bombs:
            if b[0]==(self.__i):
                if(b[1]>=self.__j and b[1]<(self.__j+self.__columns)):
                    return True,b
        
        return False,0
    
    def activateShootingPaddle(self):
        self.__paddle[0][0]='H'
        self.__paddle[0][self.__columns-1]='H'
        self.__shootingPower=True
    
    def deactivateShootingPaddle(self):
        self.__paddle[0][0]='_'
        self.__paddle[0][self.__columns-1]='_'
        self.__shootingPower=False
    
    def updateShootingInterval(self):
        self.__shootinginterval+=1
        self.__shootinginterval%=10
        if self.__shootinginterval == 0:
            return True
        return False
    
    def getShootingPower(self):
        return self.__shootingPower