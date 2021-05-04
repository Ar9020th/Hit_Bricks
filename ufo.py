class UFO:
    def __init__(self,i,j):
        self.__i=i
        self.__j=j
        arr1=[' ',' ',' ',' ',' ',' ',' ','_','.','-','-','-','.','_',' ',' ',' ',' ',' ',' ',' ']
        arr2=[' ' for i in range(21)]
        arr2[7]='.'
        arr2[13]='.'
        arr3=[' ','_','.','-','~','=','=','=','=','=','=','=','=','=','=','=','~','-','.','_',' ']
        arr4=["(","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_","_",")"]
        ufo=[]
        ufo.append(arr1)
        ufo.append(arr2)
        ufo.append(arr3)
        ufo.append(arr4)
        self.__ufo=ufo
        self.__timeinterval=1
        self.__bombs=[]
    
    def getijufo(self):
        return self.__i,self.__j,self.__ufo
    
    def updatej(self,columns,updateval):
        if updateval == 1:
            if (self.__j+21)!=(columns-1):
                self.__j+=1
        else:
            if self.__j!=1:
                self.__j-=1

    def movebombdown(self,screenrows):
        for b in self.__bombs:
            if b[0] == (screenrows-2):
                self.__bombs.remove(b)
            else:
                b[0]+=1
    
    def getbombs(self):
        return self.__bombs
    
    def updatetimeinterval(self):
        if self.__timeinterval == 0:
            self.__bombs.append([self.__i+4,self.__j+10])
        self.__timeinterval+=1
        self.__timeinterval%=100

    def removeCollidedBomb(self,bomb):
        self.__bombs.remove(bomb)