from tkinter import *
import tkinter as tk 
#kao css za tkinter
from tkinter import ttk

from Util.GUIUtils import Centriraj
from Model.Projekat import Projekat

from GUI.CRUDProzori import StudentProzor
from Model.Student import Student
from GUI.CRUDProzori import Operacija



#nasledi tkinter frejm
class Glavni(tk.Tk):
    
    #glavni izvori podataka 
    studenti = []
    
    
    

    def __init__(self):
       tk.Tk.__init__(self)
       
       
       #za ikonu prozora, moras koristiti .ico 
       #tk.Tk.iconbitmap(self, default = "putanja")
       #naslov
       tk.Tk.wm_title(self, "Glavni Prozor")
       tk.Tk.geometry(self, '1024x768')
       
       #not resizable po x i y osi
       self.resizable(False, False)
       
       
       
       
       #menu bar
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
        
        
    
       

       container = tk.Frame(self, width = 1024, height = 768)
       
       
       #self.geometry('500x500')
       
       Centriraj(self)
       
       #IDEJA JE DA IMAS JEDAN ROOT PROZOR I FREJMOVE KOJI SE SMENJUJU, STO JE SASVIM SOLIDNO
        
       #da se rasiri po celom prozoru 
       container.pack(side = "top", fill = "both", expand = True) 
       #ovo je recnik svih frejmova koji ce se menjati u prozoru
       self.frames = {}
       
       #napuni sve strane u recnik
       for i in (StartPage, PageOne, PageTwo):
           frame = i(container, self)
           self.frames[i] = frame
           
           #rasiri prvu celiju i rasiri po svim stranama
           frame.grid(row = 0, column = 0, sticky = "nsew")
       
       
       #samo ovako kazes sta hoces da prikaze i on to uzme
       #iz recnika i prikaze
       #na pocetku prikazuje pocetnu stranu
       self.show_frame(StartPage)
       
      
     
    def show_frame(self, cont):  
        #uzmi ga iz kolekcije 
        frame = self.frames[cont]
        #raise it to the front, built in funcion
        frame.tkraise()



        
#definises klase ekrana 
class StartPage(tk.Frame):
    
    
    
    listbox = None
    
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width = 1024, height = 768)
        
        
        
        
        ################## MAJKA MARA #########################################
        tk.Frame.grid(self, column = 0, row = 0, sticky = 'nsew')
        
        parent.columnconfigure(0, weight = 1)
        parent.rowconfigure(0, weight = 1)
        ########################################################################
        
        
        #toolbar
        toolbar = Frame(self, bg  = "grey")
        
        
        #ne mozes u command da pruzas parametar, zato mora ovako hakic:
        #samo jednom ce moci da pruzi parametar bez ovoga
        
        
        prvaBTN = Button(toolbar, text = "Prva", command = lambda: controller.show_frame(PageOne))
        prvaBTN.pack(side = LEFT, padx=2, pady=2)
        
        prvaBTN = Button(toolbar, text = "Druga", command = lambda: controller.show_frame(PageTwo))
        prvaBTN.pack(side = LEFT, padx=2, pady=2)
        
        
        
        toolbar.pack(side=TOP, fill=X)
        
        
        
        
        
        
        #page welcome
        label = ttk.Label(self, text = "- - Pocetna strana - - ")
        label.pack(pady=10, padx=10)
        
        
        n = ttk.Notebook(self)
        f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
        f2 = ttk.Frame(n)   # second page
        n.add(f1, text='One')
        n.add(f2, text='Two')
        
        
        
        
        
        #lista sa studentima
        
        '''
        self.listbox = Listbox(self)
        self.listbox.pack(fill=X)
        '''
        
        StartPage.listbox = Listbox(self)
        StartPage.listbox.pack(fill = X)
        
        
        
        #ugaci na kraj iz bilo koje kolekcije
        
        self.Osvezi()
        #CRUD dugmad
        
        CRUDBar = Frame(self)
        
        
        dodajBTN = Button(CRUDBar, text = "Dodaj", command = self.dodajStudenta)
        dodajBTN.pack(side = LEFT, padx=1, pady=1)
        
        izmeniBTN = Button(CRUDBar, text = "Izmeni", command = self.izmeniStudenta)
        izmeniBTN.pack(side = LEFT, padx=1, pady=1)
        
        obrisiBTN = Button(CRUDBar, text = "Obrisi")
        obrisiBTN.pack(side = LEFT, padx=1, pady=1)
        
        CRUDBar.pack(side=TOP, fill=X)
        
        
        
        
        
        #status bar
        status = Label(self, text = "Status...", bd = 1, relief = SUNKEN, anchor = W)
        status.pack(side = BOTTOM, fill = X)
        
        
    def dodajStudenta(self):
        student = Student()
        studentProzor = StudentProzor(student, Operacija.DODAVANJE)
        
    def izmeniStudenta(self):
        #samo string uzima ne i objekat
        #jebeno ne moze, tako da smisljaj neki odvratni hak ili bataljuj list box
        student = StartPage.listbox.get(ACTIVE)
        
        studentProzor = StudentProzor(student, Operacija.IZMENA)
        
    @classmethod    
    def Osvezi(cls):
        for i in Projekat().studenti:
            if(i.Obrisan != True):
                cls.listbox.insert(END, i)
    @classmethod
    def dodajNaKraj(cls, student):
        cls.listbox.insert(END, student)
                 
        
        
        
        
    
        
class PageOne(tk.Frame):
    def __init__(self, parent, controller):      
        tk.Frame.__init__(self, parent)
        
        
        
       
       
       
       
        #toolbar
        toolbar = Frame(self, bg  = "grey")
        
        
        
        
        pocetnaBTN = Button(toolbar, text = "Pocetna", command = lambda: controller.show_frame(StartPage))
        pocetnaBTN.pack(side = LEFT, padx=2, pady=2)
        
        pocetnaBTN = Button(toolbar, text = "Druga", command = lambda: controller.show_frame(PageTwo))
        pocetnaBTN.pack(side = LEFT, padx=2, pady=2)
        
        
        
        
        toolbar.pack(side=TOP, fill=X)
        
        #page welcome
        label = ttk.Label(self, text = "- - Prva strana - -")
        label.pack(pady=10, padx=10)
        
        #ne mozes u command da pruzas parametar, zato mora ovako hakic:
        #samo jednom ce moci da pruzi parametar bez ovoga
        
        
        #lista sa entitetima
        listbox = Listbox(self)
        listbox.pack(fill=X)
        
        #status bar
        status = Label(self, text = "Status...", bd = 1, relief = SUNKEN, anchor = W)
        status.pack(side = BOTTOM, fill = X)
        
        
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):      
        tk.Frame.__init__(self, parent)
        
        
        
        
        #toolbar
        toolbar = Frame(self, bg  = "grey")
        
        
        
        
        pocetnaBTN = Button(toolbar, text = "Pocetna", command = lambda: controller.show_frame(StartPage))
        pocetnaBTN.pack(side = LEFT, padx=2, pady=2)
        
        pocetnaBTN = Button(toolbar, text = "Prva", command = lambda: controller.show_frame(PageOne))
        pocetnaBTN.pack(side = LEFT, padx=2, pady=2)
        
        
        
        toolbar.pack(side=TOP, fill=X)
        
        #page welcome
        label = ttk.Label(self, text = "- - Druga strana - -")
        label.pack(pady=10, padx=10)
       
        #lista sa entitetima
        listbox = Listbox(self)
        listbox.pack(fill=X)
        
        #status bar
        status = Label(self, text = "Status...", bd = 1, relief = SUNKEN, anchor = W)
        status.pack(side = BOTTOM, fill = X)
       
     
    
    