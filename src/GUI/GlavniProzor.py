import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter import ttk
from Util.GUIUtils import Centriraj
from Model.Projekat import Projekat
from GUI.Forme import *
from Model.Student import *
from Util.GUIUtils import Centriraj
from Controller.CRUDController import *

class GlavniProzor(tk.Tk):
    def __init__(self, korisnik):
        
        
        tk.Tk.__init__(self)
       
        tk.Tk.wm_title(self, "Glavni Prozor")
        tk.Tk.geometry(self, '1024x768')
       
        self.resizable(False, False)
        Centriraj(self)
        
        self.korisnik = korisnik
       
       #definisi grid prozora, dosta korisno
       #50*50
        rows = 0
        while rows < 50:
            self.rowconfigure(rows, weight = 1)
            self.columnconfigure(rows, weight = 1)
            rows += 1
            
            
           
        menu = Menu(self)
        self.config(menu = menu)
        
        subMenu = Menu(menu)
        menu.add_cascade(label = "File", menu = subMenu)
        
        subMenu.add_command(label = "New...")
        subMenu.add_command(label = "Old...")
        subMenu.add_separator()
        subMenu.add_command(label = "Exit")
        
        editMenu = Menu(menu)
        menu.add_cascade(label = "Edit", menu = editMenu)
    
        editMenu.add_command(label = "Redo...") 
           
           
           
       
       
        nb = ttk.Notebook(self)
        nb.grid(row = 1, column = 0, columnspan = 50, rowspan = 49, sticky = 'NESW' )
       
       
        #jedna kartica jedan frejm obican
        page1 = ttk.Frame(nb)
        
        #definisi grid za svaku od kartica
        rowsp1 = 0
        
        while rowsp1 < 50:
            page1.rowconfigure(rowsp1, weight = 1)
            page1.columnconfigure(rowsp1, weight = 1)
            rowsp1 += 1
            
        # ------------------------------------------------------------
        #Komponente pojedinacnih kartica:
        
        #TREEVIEW
        self.tree = ttk.Treeview(page1, columns=("size", "modified"))
        self.tree["columns"] = ( "Ime", "Prezime", "GodStud")
        
        self.tree.column("Ime")
        self.tree.column("Prezime")
        self.tree.column("GodStud")
        
        self.tree.heading("Ime", text="Ime")
        self.tree.heading("Prezime", text="Prezime")
        self.tree.heading("GodStud", text="GodStud")
        
        self.tree.grid(row = 1, column = 0, columnspan = 50, rowspan = 15, sticky = 'NESW' )
        
        self.Osvezi()
        
        #CRUD kontrole:
        CRUDBar = Frame(page1)
        
        
        dodajBTN = Button(CRUDBar, text = "Dodaj", command = self.DodajStudenta)
        dodajBTN.pack(side = LEFT, padx=1, pady=1)
        
        izmeniBTN = Button(CRUDBar, text = "Izmeni", command = self.IzmeniStudenta)
        izmeniBTN.pack(side = LEFT, padx=1, pady=1)
        
        obrisiBTN = Button(CRUDBar, text = "Obrisi", command = self.ObrisiStudenta)
        obrisiBTN.pack(side = LEFT, padx=1, pady=1)
        
        CRUDBar.grid(row = 16, column = 0, columnspan = 50, rowspan = 3, sticky = 'NESW' )
        
        
        
        #-------------------------------------------------------------
                
        nb.add(page1, text = "Studenti")
        
        
        
        
        page2 = ttk.Frame(nb)
        
        rowsp2 = 0
        while rowsp2 < 50:
            page2.rowconfigure(rowsp2, weight = 1)
            page2.columnconfigure(rowsp2, weight = 1)
            rowsp2 += 1
        
        # ------------------------------------------------------------
        
        
        #-------------------------------------------------------------
        
        nb.add(page2, text = "Zaposleni")
        
        status = Label(self, text = "Ulogovani korisnik: " + self.korisnik.Ime, bd = 1, relief = SUNKEN, anchor = W)
        status.grid(row = 50, column = 0, columnspan = 50, rowspan = 48, sticky = 'NESW' )
     
      
    def Osvezi(self):
        #prvo ocisti
        for i in self.tree.get_children():
            self.tree.delete(i)
        #ponovo ucitaj iz kolekcije
        for i in Projekat().studenti:
            if(i.Obrisan != True):
                self.tree.insert("", 'end' ,text = i.ID, values = (i.Ime, i.Prezime, i.GodinaStudija))
    
    def DodajStudenta(self):
        student = Student()
        #prosledi referencu na glavni prozor da se iskoristio Osvezi
        studentProzor = StudentProzor(student, Operacija.DODAVANJE, self)
        
    def IzmeniStudenta(self):
        selektovani = self.tree.selection()[0]
        id = self.tree.item(selektovani)['text']
        ime = self.tree.item(selektovani)['values'][0]
        prezime = self.tree.item(selektovani)['values'][1]
        godina = self.tree.item(selektovani)['values'][2]
        
        student = Student(ID= id, obrisan= False, ime = ime, prezime = prezime, godstud = godina)
        studentProzor = StudentProzor(student, Operacija.IZMENA, self)
        
    def ObrisiStudenta(self):
        selektovani = self.tree.selection()[0]
        id = self.tree.item(selektovani)['text']
        
        odgovor = messagebox.askquestion("Obrisi", "Da li ste sigurni?", icon='warning')
        
        if (odgovor == 'yes'):
           UkloniStudenta(id)
           self.Osvezi() 
        
        
        