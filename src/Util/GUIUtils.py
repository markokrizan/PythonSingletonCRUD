
def Centriraj(prozor):
    prozor.withdraw()
    prozor.update_idletasks()
    x = (prozor.winfo_screenwidth() - prozor.winfo_reqwidth()) / 2
    y = (prozor.winfo_screenheight() - prozor.winfo_reqheight()) / 2
    prozor.geometry("+%d+%d" % (x, y))
    prozor.deiconify() 

