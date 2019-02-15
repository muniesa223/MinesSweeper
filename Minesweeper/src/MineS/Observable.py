'''
Created on 24 oct. 2018

@author: Diego Sanchez
'''

from MineS.Observer import Observer


class Observable():
     
    def __init__(self):
        self._observers = set()

    def register(self, observer: Observer):
        self._observers.add(observer)

    def notify_all(self,stri,x,y):
        for observer in self._observers:
            observer.notify(stri,x,y)