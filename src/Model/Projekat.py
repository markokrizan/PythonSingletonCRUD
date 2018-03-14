from Util.PickleUnpickle import UnPickle



#SINGLETON KLASA

class Projekat(object):
    _instance = None
    #prvo proveri da li je vec kreirana instanca
    def __new__(self):
        if not self._instance:
           self._instance = super(Projekat, self).__new__(self) 
           self.studenti = UnPickle('studenti.bin') 
           self.korisnici = UnPickle('korisnici.bin')
        return self._instance


       


'''

#SINGLETON BLUEPRINT

#inherit from object base clase
class MySingleton(object):
    _instance = None
    #prvo proveri da li je vec kreirana instanca
    def __new__(self):
        if not self._instance:
           self._instance = super(MySingleton, self).__new__(self) 
           self.y = 10
        return self._instance

x = MySingleton()
print(x.y)
x.y = 20

z = MySingleton()
print(z.y)

#10
#20

'''