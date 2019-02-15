'''
Created on 21 nov. 2018

@author: Diego Sanchez
'''
import tkinter as tk
from MineS.Observer import Observer
from MineS.Clock import Clock
from tkinter import ttk
from MineS.Controller import Controller
import  time

class View(Observer):
   
    def __init__(self,Controller, rows, cols):
        
        self.controller=Controller
        self.controller.register(self)
        
        #MODEL
        self.rows = rows
        self.cols = cols
        
        #VIEW
        self.window = tk.Tk()
        self.window.title("Minesweeper")
        self.window.geometry('400x400')
        self.table = 0
        self.buttons = [[tk.Button()]*self.rows for i in range(self.cols)]
        self.layout=self.create_grid()
        self.colors = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']
        self.clk=Clock()
        #MENU
        self.size=ttk.Combobox(state="readonly")
        self.size.set("Small")
        
        self.create_menu()    
        
         
        self.window.mainloop()   

        
          
    def create_grid(self):
        
        tk.Grid.rowconfigure(self.window, 0, weight=1)
        tk.Grid.columnconfigure(self.window, 0, weight=1)
        
        self.table=tk.Frame(self.window)
        
        self.table.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        
        tk.Grid.rowconfigure(self.table, 7, weight=1)
        tk.Grid.columnconfigure(self.table, 0, weight=1)
        
        for x in range(self.rows):
            for y in range(self.cols):
                btn = tk.Button(self.table,text=" ",command=lambda x=x,y=y: self.clickOn(x, y),)
                btn.grid(column=y, row=x, sticky=tk.N+tk.S+tk.E+tk.W)
                self.buttons[x][y]=btn

        for x in range(self.rows):
            tk.Grid.columnconfigure(self.table, x, weight=1)

        for y in range(self.cols):
            tk.Grid.rowconfigure(self.table, y, weight=1)
            
    def create_menu(self):  
        
        
        #CLOCK
        self.clk.grid(row=self.rows+3,column=0)
        
        
        #BUTTON
        btn2 = tk.Button( text="PLAY",command=lambda:self.setSize(self.size.get()))
        print(self.size.get())
        btn2.grid(row=self.rows+2,column=0)
        btn2.configure(state='normal')
      
        #COMBOBOX
        
        self.size["values"] = ["Small", "Medium", "Big"]
        self.size.grid(row=self.rows+1,column=0) 
 
    def clickOn(self,x,y):
            

        if self.controller.isBomb(x,y)==False:
           
           number=self.controller.countMines(x,y)
           self.buttons[x][y].config(disabledforeground=self.colors[1])
           self.buttons[x][y]["text"] = number
           self.buttons[x][y]['state'] = 'disabled'    
 
 
    def setSize(self,str):

        if str=="Small":
            self.rows=6
            self.cols=6
        elif str=="Medium":
            self.rows=9
            self.cols=9
        else:
            self.rows=12
            self.cols=12
        
        self.buttons.clear()
        self.buttons = [[tk.Button()]*self.rows for i in range(self.cols)]
        self.create_grid()
        self.controller.resize(str)
        self.clk.stop()  
        self.clk.restart()
        
        self.window.update()
        self.table.update()
        
      
    def notify (self,stri,x,y):
        
        if stri=="Loose":
            
            self.buttons[x][y]["text"] = "*"
            self.buttons[x][y].config(background='red', disabledforeground='black')
            self.clk.stop()
       
            
            #photo=tk.PhotoImage(file="bomba1.png")
            #self.buttons[x][y].config(image=photo,width="100",height="100")

        
            windowLooser=tk.Tk()
            windowLooser.title("Loose")
            windowLooser.geometry('200x50')
            label = ttk.Label(windowLooser, text="Sorry, you loose",font=("Helvetica", 12))
            label.pack(side="top", fill="x", pady=10)
            
            for x in range(self.rows):
                for y in range(self.cols):
                   self.buttons[x][y]['state'] = 'disabled' 
            #B1 = tk.Button(windowLooser, text="Restart", command = self.restart())
            #B1.pack()
            windowLooser.mainloop() 
            
        elif stri=="Victory":
            
            windowChamp=tk.Tk()
            windowChamp.title("Victory")
            windowChamp.geometry('200x50')
            label = ttk.Label(windowChamp, text="Congratulations, you have won",font=("Helvetica", 12))
            label.pack(side="top", fill="x", pady=10)
        

    def restart(self):
        
        self.buttons = [[tk.Button()]*self.rows for i in range(self.cols)]
        self.layout=self.create_grid() 
        self.window.update()
        self.table.update()

        
   