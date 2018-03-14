from tkinter import *
from Model.Projekat import Projekat
import tkinter.messagebox
from Util.GUIUtils import Centriraj
from GUI.GlavniProzor import GlavniProzor

class Login(tkinter.Tk):
    
    
    
    def __init__(self):
        tkinter.Tk.__init__(self)
        #container = tkinter.Frame(self)
        self.geometry('300x150')
        self.title("Login")
        Centriraj(self)
        
        self.korisnik = None
        
        #ovo jos vidi
        #container.pack(side = 'top', fill = "both", expand = True)
        
        Input = Frame(self)
        
        self.userLabel = Label(Input, text = "Username: ")
        self.passLabel = Label(Input, text = "Password: ")
        self.userEntry = Entry(Input)
        self.passEntry = Entry(Input)
        #mora da gadja metodu klase bukvlano
        self.LoginBTN = Button(Input, text = "Login", command = self.Login)
        #self.LoginBTN.bind("<Button-1>", self.Login)
        
        
        #sticky: N E S W, North, East, South, West - ALIGNEMENT
        self.userLabel.grid(row = 0, sticky = E)#0 column by default
        self.passLabel.grid(row = 1, sticky = E)
        self.userEntry.grid(row = 0, column = 1)
        self.passEntry.grid(row = 1, column = 1)
        self.LoginBTN.grid(columnspan = 2)
        
        Input.pack()
    
    
    def Login(self):
        kor = self.userEntry
        loz = self.passEntry
        
        if(kor.get() == "" or loz.get() == ""):
            tkinter.messagebox.showinfo('Greska', 'Niste uneli sve podatke!') 
        elif(self.CredCheck(kor.get(), loz.get()) == True):
            #ostaje u memoriji samo sakriva
            self.withdraw()  
            glavniProzor = GlavniProzor(self.korisnik)
                   
        else:
            tkinter.messagebox.showinfo('Greska', 'Niste uneli dobre podatke!')
            '''
            #kada su ueni losi podaci ocisti polja:
            kor.set("")
            loz.set("")
            '''
            
    def CredCheck(self, korisnicko, lozinka):
        korisnici = Projekat().korisnici
        for i in korisnici:
            if(i.Korisnicko == korisnicko and i.Lozinka == lozinka):
                self.korisnik = i
                return True
                break
            else:
                return False
            
            
            
   
            
            
            
            