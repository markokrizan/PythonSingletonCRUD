from Model.Projekat import Projekat

class Student(object):
    
   
    #brojStudenata = 0
    

    def __init__(self, ID = 0, obrisan = False,  ime = "", prezime = "", godstud = 1):
        self.ID = ID
        self.Obrisan = obrisan
        self.Ime = ime
        self.Prezime = prezime
        self.GodinaStudija = godstud
        #Student.brojStudenata += 1
    
    '''
    @classmethod
    def getBrojStudenata(cls):
        return cls.brojStudenata
    '''
    
    
    
    
    #override ugradjeno to string metodu
    def __str__(self):
        
        #sad ovi koji su untra nemaju id pa izbacije gresku, ubucai blagovremeno
        return  str(self.ID) + ", " + self.Ime + ", " + self.Prezime + ", " + str(self.GodinaStudija)
        
        
        