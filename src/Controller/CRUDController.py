from Model.Projekat import *
from Util.PickleUnpickle import *

def DodajStudenta(student):
    Projekat().studenti.append(student)
    Pickle('studenti.bin', Projekat().studenti)
    
    
        
def IzmeniStudenta(student):
    #print(student)
    for i in Projekat().studenti:
        if i.ID == student.ID:
            i.Ime = student.Ime
            i.Prezime = student.Prezime
            i.GodinaStudija = student.GodinaStudija
    Pickle('studenti.bin', Projekat().studenti)
    
def UkloniStudenta(id):
    for i in Projekat().studenti:
        if i.ID == id:
            i.Obrisan = True
    Pickle('studenti.bin', Projekat().studenti)
    
