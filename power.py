class Power:
    def __init__(self,type,i,j,dy=0):
        if(type==0):
            self.__dsgchar='#'
        if(type==1):
            self.__dsgchar='$'
        if(type==2):
            self.__dsgchar='%'
        if(type==3):
            self.__dsgchar='&'
        if(type==4):
            self.__dsgchar='!'
        if(type==5):
            self.__dsgchar='+'
        if(type==6):
            self.__dsgchar='{'
        self.__type=type
        self.__i=i
        self.__j=j
        self.__dy=dy
        self.__temp=' '
        self.__gravitationaleffect=10
        self.__holdinair=5
        self.__updatemovement=False
    
    def moveDown(self,ch,screencols):
        if self.__updatemovement==True:
            self.__updatemovement=False
            return 0
        self.__updatemovement=True
        if self.__dy != 0:
            if self.__gravitationaleffect>=0:
                self.__i-=1
                self.__i=max(self.__i,1)
                self.__gravitationaleffect-=1
            elif self.__holdinair>=0:
                self.__holdinair-=1
            else:
                self.__i+=1
            self.__j+=self.__dy
            if self.__j == screencols-2 or self.__j == 1:
                self.__dy=-1*self.__dy
            self.__temp=ch
        else:
            self.__i+=1
            self.__temp=ch
    
    def getijtemp(self):
        return self.__i,self.__j,self.__temp
    
    def getijdsgchar(self):
        return self.__i,self.__j,self.__dsgchar
    
    def getijtype(self):
        return self.__i,self.__j,self.__type
    
    def getij(self):
        return self.__i,self.__j
    
    def getdxdy(self):
        if self.__dy != 0:
            if self.__gravitationaleffect>=0:
                return -1,self.__dy
            elif self.__holdinair>=0:
                return 0,self.__dy
            else:
                return 1,self.__dy
        else:
            return 1,self.__dy
    