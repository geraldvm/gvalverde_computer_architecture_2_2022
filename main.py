
from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
#import tkMessageBox
import tkinter
import os
import sys
import time
import threading

from Multiprocessor import Multiprocessor

#Multiprocessor Setup
ID1="CPU@01"
ID2="CPU@02"
ID3="CPU@03"
ID4="CPU@04"
TIMER=0
mt = Multiprocessor(ID1,ID2,ID3,ID4,TIMER)



#***************Cargar Imagenes***********************
#Entrada: Nombre de la imagen
#Restricciones: el nombre de la imagen debe ser formato str
#Salida: Genera la imagen
def loadImage(filename):
    path = os.path.join('images',filename)
    imagen = PhotoImage(file=path)
    return imagen


#***********Ventana Principal*************************
#configuracion de ventana principal
window = Tk()
window.title("Memory map")
window.minsize(1024,600)
window.resizable(width=NO, height=NO)
window.configure(background="black")



windowWidth = window.winfo_reqwidth() #sizes
windowHeight = window.winfo_reqheight()    
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)    
window.geometry("+{}+{}".format(positionRight, positionDown))
    
cv= Canvas(window, width= 1024, height = 600)
cv.place(x=0,y=0)
bg= loadImage("bg2.png")
cv.create_image(0,0, anchor =  "nw", image = bg)  #pos x, pos y, image

cpu_label1=Label(window, bg='white', fg='black', text=ID1).place(x=60,y=75)
cpu_label2=Label(window, bg='white', fg='black', text=ID2).place(x=200,y=75)
cpu_label3=Label(window, bg='white', fg='black', text=ID3).place(x=340,y=75)
cpu_label4=Label(window, bg='white', fg='black', text=ID4).place(x=460,y=75)
cash_cpu1 = Listbox(window, background="white", foreground="black", height=19)
cash_cpu1.place(x=50,y=150)
ins_cpu1 = Listbox(window, background="#2596be", foreground="black", height=2).place(x=50,y=100)

def main():
    
    mt.run()
    while(1):
        #mt.BUS.CACHE_LIST[0].iprint()
        update_cash(cash_cpu1,mt.BUS.CACHE_LIST[0].istring())
        time.sleep(3)



def update_cash(listbox,cache):
    listbox.delete(0, END)
    listbox.insert(0,'')
    
    for i in range(len(cache)):
        listbox.insert(i+1,cache[i])

main_th = threading.Thread(target=main)
main_th.start()        
window.mainloop()