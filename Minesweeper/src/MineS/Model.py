'''
Created on 21 nov. 2018

@author: Diego Sanchez
'''

import random
from MineS.Observable import Observable

class Model(Observable):

    def __init__(self, rows, cols, numMines):
        
        self.loose = False
        super().__init__()
        self.rows = rows
        self.cols = cols
        
        self.num_mines=numMines
        self.num_accerts=0       
        
        self.grid = [[0]*self.rows for i in range(self.cols)]
          
        for i in range(1,self.num_mines):
            self.setMines()
          
    def resize(self,str):
        if str=="Small":
            self.rows=6
            self.cols=6
            self.num_mines=6
            self.num_accerts=0
            self.grid = [[0]*self.rows for i in range(self.cols)]
            self.setMines()
        elif str=="Medium":
            self.rows=9
            self.cols=9
            self.num_mines=10
            self.num_accerts=0
            self.grid = [[0]*self.rows for i in range(self.cols)]
            self.setMines()
        else:
            self.rows=12
            self.cols=12
            self.num_mines=15
            self.num_accerts=0
            self.grid = [[0]*self.rows for i in range(self.cols)]
            self.setMines()
            
    def checkWin(self):
        if self.num_accerts == ( (self.rows*self.cols)-self.num_mines + 1 ):
            return True
        else:
            return False
            
    def countMines(self,x,y):
        print(self.grid)
        xs=[x-1,x,x+1]
        ys=[y-1,y,y+1]
        count=0
        for i in range(3):
            for u in range(3):
                if(i==1 and u==1):
                    continue
                else:
                    if self.existPosition(xs[i], ys[u]) and self.grid[xs[i]][ys[u]]==1:
                        count=count+1
       
        return count
    
    def existPosition(self,x,y):
        if(x<0 or y<0 or x>=self.rows or y>=self.cols):
            return False
        else:
            return True
                   
    def setMines(self):
        x= random.randrange(0, self.rows-1, 1)
        y= random.randrange(0, self.cols-1, 1)
        if self.grid[x][y] != 1:
            self.grid[x][y]=1
        else:
            self.setMines()
            
    def isBomb(self,x,y):
        if self.grid[x][y] == 1:
            self.setLoose(x,y)
            return True
        else:
            self.num_accerts=self.num_accerts+1
            if self.checkWin()==True:
                self.victory()
            return False
        
    def setLoose(self,x,y):
        self.loose=True
        self.notify_all("Loose",x,y)
            
    def sumAccert(self):
        self.accerts=self.accerts + 1
        if self.accerts == [self.row*self.cols]-self.num_mines:
            self.victory()
            
    def victory(self):
        self.notify_all("Victory",0,0)