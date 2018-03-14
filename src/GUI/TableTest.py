
'''

try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *


class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        #self.CreateUI()
        
        self.tv = Treeview(self)
        self.tv['columns'] = ('starttime', 'endtime', 'status')
        self.tv.heading("#0", text='Sources', anchor='w')
        self.tv.column("#0", anchor="w")
        self.tv.heading('starttime', text='Start Time')
        self.tv.column('starttime', anchor='center', width=100)
        self.tv.heading('endtime', text='End Time')
        self.tv.column('endtime', anchor='center', width=100)
        self.tv.heading('status', text='Status')
        self.tv.column('status', anchor='center', width=100)
        self.tv.grid(sticky = (N,S,W,E))
        self.treeview = self.tv
        self.treeview.bind('<ButtonRelease-1>', App.selectItem)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        
        
        
        self.LoadTable()
        
        
        
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    
        

    def LoadTable(self):
        self.treeview.insert('', 'end', text="First", values=('10:00',
                             '10:10', 'Ok'))
    @staticmethod    
    def selectItem(a):
        drvo = App.tv
        current = drvo.focus()
        print(drvo.item(current))

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
    




#mozes kao recnik da prihvatis red, sto i nije tako lose
'''

from tkinter import *
from tkinter import ttk
from Model.Projekat import Projekat

def selectItem(a):
    
   
    '''
    selected_item = tree.selection()[0] ## get selected item
    #tree.delete(selected_item)
    #print(selected_item)
    print(tree.item(selected_item)['values'])
    '''
    

def btnCommand():
    selected_item = tree.selection()[0] ## get selected item
    #tree.delete(selected_item)
    #print(selected_item)
    print(tree.item(selected_item)['values'])
    print(tree.item(selected_item)['text'])
    
root = Tk()
tree = ttk.Treeview(root, columns=("size", "modified"))
tree["columns"] = ( "Ime", "Prezime", "GodStud")

tree.column("Ime", width=65)
tree.column("Prezime", width=40)
tree.column("GodStud", width=100)

tree.heading("Ime", text="Ime")
tree.heading("Prezime", text="Prezime")
tree.heading("GodStud", text="GodStud")
tree.bind('<Button-1>', selectItem)

button_del = Button(root, text="Dugme", command=btnCommand)
button_del.grid()

brojac = 0
for i in Projekat().studenti:
    #tree.insert("", "end",text = "Name",values = ("Date","Time","Loc"))
    tree.insert("", 'end' ,text = i.ID, values = (i.Ime, i.Prezime, i.GodinaStudija))
    
    #print(i)

tree.grid()
root.mainloop()




