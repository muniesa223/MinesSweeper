'''
Created on 24 nov. 2018

@author: Diego
'''
import time
import tkinter as tk


class Clock(tk.Frame):
    
    def __init__(self):
        super(Clock, self).__init__()
        self.stoped=False
       
       
        self.Label1=tk.Label(self, text = 'Seconds:',font=("Helvetica", 12)).grid(row = 0, columnspan = 3)
        
        self.Label2=tk.Label(self, text = 'Minutes:',font=("Helvetica", 12)).grid(row = 1, column = 0)
        
        self.minLabel=tk.Label(self)
        self.secLabel=tk.Label(self)
       
        self.minLabel.grid(column=4, row=1, sticky=tk.N+tk.S+tk.E+tk.W)
        self.secLabel.grid(column=4, row=0)
        
        
        
        self.counter_sec=0
        self.counter_min=0
        self.update_clock()

    def update_clock(self):
        
        if self.counter_sec==60:
            self.counter_min=self.counter_min+1
            self.counter_sec=0
            self.minLabel.configure(text=self.counter_min)
            self.secLabel.configure(text=self.counter_sec)
            #self.configure(text=self.counter_min + self.counter_sec)
            if self.stoped==False:
                self.after(1000, self.update_clock)
        else:
            self.counter_sec=self.counter_sec+1
            self.secLabel.configure(text=self.counter_sec)
            self.minLabel.configure(text=self.counter_min)
            #self.configure(text=self.counter_min + self.counter_sec)
            if self.stoped==False:
                self.after(1000, self.update_clock)
                
    def stop(self):
        self.counter_sec=0
        self.counter_min=0
        self.stoped=True

    def restart(self):
        self.stoped=False
        
        
        