####Klase za CRUD operacije
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from Util.GUIUtils import Centriraj
from Model.Projekat import Projekat


from enum import Enum

#circular dependency


class Operacija(Enum):
    DODAVANJE = 1
    IZMENA = 2







class StudentProzor(tk.Tk):
    def __init__(self, student, operacija):
        tk.Tk.__init__(self)
        
       
        tk.Tk.wm_title(self, "Student UD")
        tk.Tk.geometry(self, '300x150')
        self.resizable(False, False)
        Centriraj(self)
        
        
        
        
        self.student = student
        self.operacija = operacija
        
        #neka vrsta bindinga
        
        
        textIme = StringVar()
        textIme.set(str(self.student.Ime))
        
        textPrezime = StringVar()
        textPrezime.set(self.student.Prezime)
        
        textGodina = StringVar()
        textGodina.set(self.student.GodinaStudija)
        
        
        Input = Frame(self)
        
        self.imeLabel = Label(Input, text = "Ime: ")
        self.prezimeLabel = Label(Input, text = "Prezime: ")
        self.godinaLabel = Label(Input, text = "Godina: ")
        self.imeEntry = Entry(Input, textvariable = textIme)
        self.prezimeEntry = Entry(Input, textvariable = textPrezime )
        self.godinaEntry = Entry(Input, textvariable = textGodina)
        self.potvrdiBTN = Button(Input, text = "Potvrdi", command = self.StudentCU)
      
       
        self.imeLabel.grid(row = 1, sticky = E)#
        self.prezimeLabel.grid(row = 2, sticky = E)
        self.godinaLabel.grid(row = 4, sticky = E)
        
        self.imeEntry.grid(row = 1, column = 1)
        self.prezimeEntry.grid(row = 2, column = 1)
        self.godinaEntry.grid(row = 4, column = 1)
        self.potvrdiBTN.grid(columnspan = 2)
        
        Input.pack()
        
        
        
        
        
        
        
    def StudentCU(self):
        if self.operacija == Operacija.DODAVANJE:
            
            brojac = 0
            for i in Projekat().studenti:
                brojac += 1
            
            self.student.ID = brojac + 1
            self.student.Ime = self.imeEntry.get()
            self.student.Prezime = self.prezimeEntry.get()
            self.student.GodinaStudija = self.godinaEntry.get()
            
            
            Projekat().dodajStudenta(self.student)
            self.withdraw()
            
            
            
            
            
            
            
            
            
        elif self.operacija == Operacija.IZMENA:
            print(self.student)
            
            
        
     
    
        
        