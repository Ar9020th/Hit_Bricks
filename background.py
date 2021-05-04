from colorama import init,Fore,Back,Style
init()
class Background:
    
    def __init__(self,screen_rows,screen_columns):
        self.__screen=[]
        self.__screenrows=screen_rows
        self.__screencolumns=screen_columns
        self.__screen=[[' ' for i in range(screen_columns)] for j in range(screen_rows)]
        
        for i in range(screen_rows):
            self.__screen[i][0]=Fore.GREEN+'X'+Style.RESET_ALL
            self.__screen[i][screen_columns-1]=Fore.GREEN+'X'+Style.RESET_ALL

        for i in range(screen_columns):
            self.__screen[0][i]=Fore.GREEN+'X'
            self.__screen[screen_rows-1][i]=Fore.GREEN+'X'+Style.RESET_ALL
    
    def addPaddleToScreen(self,paddle):
        ijcolumns=paddle.getijcolumns()
        locpaddle=paddle.getpaddle()
        posi=ijcolumns[0]
        posj=ijcolumns[1]
        # print(len(locpaddle[0]))
        for i in range(ijcolumns[2]):
            self.__screen[posi][i+posj]=locpaddle[0][i]
            self.__screen[posi+1][i+posj]=Back.BLUE+locpaddle[1][i]+Style.RESET_ALL
    
    def removePaddleFromScreen(self,paddle):
        ijcolumns=paddle.getijcolumns()
        posi=ijcolumns[0]
        posj=ijcolumns[1]
        # print(len(locpaddle[0]))
        for i in range(ijcolumns[2]):
            self.__screen[posi][i+posj]=' '
            self.__screen[posi+1][i+posj]=' '
    
    def addBrickToScreen(self,brick):
        bric,strength,x,y=brick.getBrick()
        if strength==4:
            for i in range(len(bric)):
                self.__screen[x][i+y]=Back.WHITE+' '+Style.RESET_ALL
        elif strength == 3:
            for i in range(len(bric)):
                self.__screen[x][i+y]=Back.RED+' '+Style.RESET_ALL
        elif strength == 2:
            for i in range(len(bric)):
                self.__screen[x][i+y]=Back.CYAN+' '+Style.RESET_ALL
        elif strength == 1:
            for i in range(len(bric)):
                self.__screen[x][i+y]=Back.YELLOW+' '+Style.RESET_ALL
        else:
            for i in range(len(bric)):
                self.__screen[x][i+y]=' '
    
    def removeBrickFromScreen(self,brick):
        bric,strength,x,y=brick.getBrick()
        for i in range(len(bric)):
            self.__screen[x][y+i]=' '

    def addBalltoScreen(self,ball):
        i,j=ball.getij()
        self.__screen[i][j]='O'

    def printScreen(self):
        for i in range(self.__screenrows):
            print("".join(self.__screen[i]))
    
    def removeBallFromScreen(self,ball,flag):
        i,j=ball.getij()
        if flag==2:
            self.__screen[i][j]='_'
        else:
            self.__screen[i][j]=' '
    
    def removePower(self,power):
        i,j,temp=power.getijtemp()
        self.__screen[i][j]=temp
    
    def addPowerToBg(self,power):
        i,j,dc=power.getijdsgchar()
        self.__screen[i][j]=dc
    
    def getCharAtIJ(self,i,j):
        return self.__screen[i][j]
    
    def clearbackground(self):
        for i in range(1,self.__screenrows-1):
            for j in range(1,self.__screencolumns-1):
                self.__screen[i][j]=' '
    
    def addUfoToBackground(self,ufo):
        x,y,ufo=ufo.getijufo()
        for i in range(len(ufo)):
            for j in range(len(ufo[0])):
                self.__screen[x+i][y+j]=Fore.BLUE+ufo[i][j]+Style.RESET_ALL
            
    def clearUFO(self,ufo):
        x,y,ufo=ufo.getijufo()
        for i in range(len(ufo)):
            for j in range(len(ufo[0])):
                self.__screen[x+i][y+j]=' '
    
    def addBombsToBackground(self,bombs):
        for b in bombs:
            self.__screen[b[0]][b[1]]='8'
    
    def removeBombsFromBackground(self,bombs):
        for b in bombs:
            self.__screen[b[0]][b[1]]=' '
    
    def removeCollidedBomb(self,b):
        self.__screen[b[0]][b[1]]=' '
    
    def addbulletsToScreen(self,bullets):
        for b in bullets:
            self.__screen[b[0]][b[1]]='V'
    
    def removeBulletsFromScreen(self,bullets):
        for b in bullets:
            self.__screen[b[0]][b[1]]=' '