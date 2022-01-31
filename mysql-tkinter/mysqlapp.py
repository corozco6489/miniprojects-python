from tkinter import Tk , Button , Entry , Label,ttk , PhotoImage , Frame

from pip import main
from conexion import *
import time


class Registro(Frame):
    def __init__(self , master , *args) :
        
        super().__init__(master,*args)
        
        self.fram1 = Frame(master)
        self.fram1.grid(columnspan=2 , column=0 , row=0)
        
        
        self.menu = True
        self.color = True
        
 
      
def main():
    ventana = Tk()
    ventana.title('Registro de datos mysql')
    ventana.config(bg='gray22')
    ventana.geometry('900x500')
    ventana.resizable(0,0)
    app = Registro(ventana)
    app.mainloop()

if __name__ == "__main__":
    main()  