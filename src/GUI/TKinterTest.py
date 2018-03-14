from tkinter import *
from tkinter import ttk


#blank window, this is the acutal constructor
root = Tk()
root.title('Test prozor')
root.geometry('1024x768')


def randomFunction():
    print("some out")
####################################################################################
'''
#part 1
#all controls are called widgets in tkinter
label = Label(root, text = "Some text")

#just pack it in there dobrojeto
label.pack()
'''

#frame - panel in swing, koristi ga kao kontejner

'''
#part 2
topFrame = Frame(root)
topFrame.pack()#by default on TOP

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "Button 1", fg = "red")
button2 = Button(topFrame, text = "Button 2", fg = "blue")
button3 = Button(bottomFrame, text = "Button 3", fg = "green")
button4 = Button(bottomFrame, text = "Button 4", fg = "purple")


#this actually displays them 
#pack default is on top of each other, stack like
button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = RIGHT)
button4.pack(side = RIGHT)
'''

'''
#part3
one = Label(root, text = "One", bg = "red", fg = "white")
two = Label(root, text = "Two", bg = "green", fg = "white")
three = Label(root, text = "Three", bg = "green", fg = "white")
one.pack()

#fill it as long as the x value of the parrent is, kind of responsive as you resize the container window
two.pack(fill = X)

#the same goes for Y axis
three.pack(side = LEFT, fill = Y)
'''


'''
#part4
#GRID:

one = Label(root, text = "Username: ")
two = Label(root, text = "Password: ")
oneEntry = Entry(root)
twoEntry = Entry(root)
check = Checkbutton(root, text = "Keel me logged in ")

#sticky: N E S W, North, East, South, West - ALIGNEMENT
one.grid(row = 0, sticky = E)#0 column by default
two.grid(row = 1, sticky = E)
oneEntry.grid(row = 0, column = 1)
twoEntry.grid(row = 1, column = 1)
check.grid(columnspan = 2)
'''

#part5
#basic listeners:
'''
def printName():
    print("Hello")

#without pars for command arg
#in python called: Binding a funciton to a widget
button = Button(root, text = "TestListener", command = printName)
button.pack()
'''
#OR

'''
def printName(event):
    print("Hello")


button = Button(root, text = "TestListener")
#first arg name for left mouse button event, jebiga, drugi arg sta se poziva po tom iventu
#ovo je mozda jasniji primer binda iventa
button.bind("<Button-1>", printName)
button.pack()
'''

'''
#part6
#possible to bind multiple functions for multiple events for one widget

def leftClick(event):
    print('Left')

def middleClick(event):
    print('Middle')

def rightClick(event):
    print('Right')

frame = Frame(root, width = 300, height = 250)#sets the size of root window too
#YOU CAN ADD EVENTS ON A FRAME 
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()
'''


'''
#part7
#OOP in TKinter

class GUIKlasa:
    
    
    #master - root(main window), convetion for arg name, ali prosledjujes root dole, da na njemu napravi frejm
    def __init__(self, master):
        #put that frame in the root - main window 
        frame = Frame(master)
        #display:
        frame.pack()
        
        self.printButton = Button(frame, text = "Print", command = self.printMessage)
        self.printButton.pack(side=LEFT)
        
        #brakes the main loop, built in method
        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side=LEFT)
        
        
    def printMessage(self):
        print("Nesto bla bla")



gk = GUIKlasa(root)


'''

'''
#part8 main menu
def someFunction():
    print("some out")

def someOtherFunction():
    print("some other out")
    
m = Menu(root)
root.config(menu=m)

subMenu = Menu(m)
m.add_cascade(label = "File", menu = subMenu)

subMenu.add_command(label = "New...", command = someFunction)
subMenu.add_command(label = "Old...", command = someOtherFunction)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command = someFunction)

editMenu = Menu(m)
m.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Redo...", command = someOtherFunction)
'''


'''
#part 9 toolbar

toolbar = Frame(root, bg = "blue")
insertButton = Button(toolbar, text = "Insert", command = randomFunction)
#padx pady pading x, y, in pixels
insertButton.pack(side = LEFT, padx=2, pady=2)

printButton = Button(toolbar, text = "Print", command = randomFunction)
printButton.pack(side = LEFT, padx=2, pady=2)


toolbar.pack(side=TOP, fill=X)
'''

'''
#part 10 status bar

#bd - border, SUNKEN - sunken in the screen
status = Label(root, text = "Status...", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)
'''



'''
#part 11 message box

import tkinter.messagebox

tkinter.messagebox.showinfo('Window title', 'Some message text')

#store in variable directly
answer = tkinter.messagebox.askquestion('Question 1', 'Yes or no question')

if answer == 'yes':
    print("yes")
else:
    print('no')

'''



'''
#part 12 graphics

canvas = Canvas(root, width = 200, height = 200)
canvas.pack()

#x, y start, x, y end
blackLine = canvas.create_line(0,0, 200, 200)

#canvas.delete(blackLine)
#canvas.delete(ALL)
'''

'''
#part 13 images and icons
photo = PhotoImage(file = "lokacija sa ekstenzijom")
#you need to put it in a label
label = Label(root, image = photo)
label.pack()
'''

#part 14 table kroz krid
# ne postoji interni widget za tabele, lol

'''
height = 5
width = 3
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Label(root, text="Blaasdasd")
        b.grid(row=i, column=j)


'''



#define a grid,  very useful:

rows = 0
while rows < 50:
    root.rowconfigure(rows, weight = 1)
    root.columnconfigure(rows, weight = 1)
    rows += 1


#Notebook - tabs
nb = ttk.Notebook(root)
#ovde ispodesavas fino kako ide, ceo je 50 redova i onda ga smanjis po potrebi da ubacis menije gore ili ispod nesto kako god
nb.grid(row = 1, column = 0, columnspan = 50, rowspan = 49, sticky = 'NESW' )

#frame to tab
page1 = ttk.Frame(nb)
nb.add(page1, text = "Prvi tab")

page2 = ttk.Frame(nb)
nb.add(page2, text = "Drugi tab")

#sada ovako dodajes vidzete direktno na strane label = Label(page1) itd

tree = ttk.Treeview(page1, columns=("size", "modified"))
tree["columns"] = ( "Ime", "Prezime", "GodStud")

tree.column("Ime")
tree.column("Prezime")
tree.column("GodStud")

tree.heading("Ime", text="Ime")
tree.heading("Prezime", text="Prezime")
tree.heading("GodStud", text="GodStud")

tree.grid()





####################################################################################

#needed for it to stay on screen, inifinite loop of render of the window, close button breaks the loop
root.mainloop()

