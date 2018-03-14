

class Korisnik:
        
    BrojKorisnika = 0

    def __init__(self,ID,  ime, prezime, korisnicko, lozinka):
        self.ID = ID
        self.Ime = ime
        self.Prezime = prezime
        self.Korisnicko = korisnicko
        self.Lozinka = lozinka
        Korisnik.BrojKorisnika += 1
        
    @classmethod
    def getBrojKorisnika(cls):
        return cls.BrojKorisnika
        