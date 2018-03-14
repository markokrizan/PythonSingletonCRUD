import tkinter as tk 
from tkinter import ttk
from tkinter import *
from Model.Student import *
from Model.Projekat import *
from enum import Enum
from Util.GUIUtils import *
from Controller.CRUDController import *

class Operacija(Enum):
    DODAVANJE = 1
    IZMENA = 2
    

class StudentProzor(tk.Tk):
    def __init__(self, student, operacija, glavni):
        tk.Tk.__init__(self)
        
       
        tk.Tk.wm_title(self, "Student UD")
        tk.Tk.geometry(self, '200x150')
        self.resizable(False, False)
        Centriraj(self)
        
        self.student = student
        self.operacija = operacija
        
        #referenca na glavni da se moze iskoristiti Osvezi
        self.glavni = glavni
        
        rows = 0
        while rows < 10:
            self.rowconfigure(rows, weight = 1)
            self.columnconfigure(rows, weight = 1)
            rows += 1
        
        Input = Frame(self)
        
        self.imeLabel = Label(Input, text = "Ime: ")
        self.prezimeLabel = Label(Input, text = "Prezime: ")
        self.godinaLabel = Label(Input, text = "Godina: ")
        
        self.imeEntry = Entry(Input)
        self.prezimeEntry = Entry(Input)
        self.godinaEntry = Entry(Input)
        
        #napuni vrednostima, ako se prosledi prazan student bice prazno
        self.imeEntry.insert(0, student.Ime)
        self.prezimeEntry.insert(0, student.Prezime)
        self.godinaEntry.insert(0, student.GodinaStudija)
        
        
        self.potvrdiBTN = Button(Input, text = "Potvrdi", command = self.StudentCU)
      
       
        self.imeLabel.grid(row = 1, sticky = E)#
        self.prezimeLabel.grid(row = 2, sticky = E)
        self.godinaLabel.grid(row = 4, sticky = E)
        
        self.imeEntry.grid(row = 1, column = 1)
        self.prezimeEntry.grid(row = 2, column = 1)
        self.godinaEntry.grid(row = 4, column = 1)
        self.potvrdiBTN.grid(columnspan = 2)
        
        Input.grid(row = 2, column = 0, columnspan = 10, rowspan = 10, sticky = 'NESW' )
        
        
    def StudentCU(self):
        if self.operacija == Operacija.DODAVANJE:
            
            brojac = 0
            for i in Projekat().studenti:
                brojac += 1
            
            self.student.ID = brojac + 1
            self.student.Ime = self.imeEntry.get()
            self.student.Prezime = self.prezimeEntry.get()
            self.student.GodinaStudija = self.godinaEntry.get()
            
            DodajStudenta(self.student)
            
            self.glavni.Osvezi()
            
            #vidi ovo sta se desava, mozda destruktor eksplicitno
            self.withdraw()
            
            
        elif self.operacija == Operacija.IZMENA:
            #print(self.student)
            
            self.student.Ime = self.imeEntry.get()
            self.student.Prezime = self.prezimeEntry.get()
            self.student.GodinaStudija = self.godinaEntry.get()
            
            
            IzmeniStudenta(self.student)
            
            self.glavni.Osvezi()
            
            self.withdraw()
            
            
            
            
            
            
            
        