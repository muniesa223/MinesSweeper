'''
Created on 21 nov. 2018

@author: Diego Sanchez
'''
from MineS.Controller import Controller
from MineS.Model import Model
from MineS.View import View
class main():
    
    rows=4
    cols=4
    numMines=3
    controller=Controller(rows,cols,numMines)
    view=View(controller,rows,cols)
   