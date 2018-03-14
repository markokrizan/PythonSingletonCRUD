import pickle
import os, os.path


def Pickle(imeFajla, lista): 
    try:
        #binary_file = open((os.path.join(os.getcwd(), 'Data\\') + imeFajla) , 'wb')
        binary_file = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'Data', imeFajla)), 'wb')
        pickle.dump(lista, binary_file)
    except OSError as e:
        print('Greska (' + e.errmsg + ')')
    finally:
        binary_file.close()
    
    
def UnPickle(imeFajla):
    try:
        #binary_file = open((os.path.join(os.getcwd(), 'Data\\') + imeFajla) , 'rb')
        binary_file = open(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'Data', imeFajla)), 'rb')
        lista = pickle.load(binary_file)
        
        return lista
    except OSError as e:
        print('Greska (' + e.errmsg + ')')
    finally:
        binary_file.close()
    
        
        
    
    