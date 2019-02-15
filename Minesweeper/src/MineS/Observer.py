'''
Created on 25 oct. 2018

@author: Diego Sanchez
'''
from abc import ABC, abstractmethod


class Observer(ABC):
    
    
    @abstractmethod
    def notify(self,x,y):
        pass