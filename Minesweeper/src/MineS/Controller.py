'''
Created on 21 nov. 2018

@author: Diego Sanchez
'''
from MineS.Model import Model
#from MineS.View import View
#from MineS.Observer import Observer
class Controller():
      
    def __init__(self,rows,cols,numMines):
        self.rows=rows
        self.cols=cols
        self.numMines=numMines
        
        
        self._model = Model(self.rows, self.cols,self.numMines)
            
    def isBomb(self,x,y):
        return self._model.isBomb(x,y)
    
    def countMines(self,x,y):
        return self._model.countMines(x, y)
        
    def resize(self,stri):
        self._model.resize(stri)
        
    def register(self,view):
        self._model.register(view)
        