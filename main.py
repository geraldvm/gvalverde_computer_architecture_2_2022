
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
    
cv= Canvas(window, width= 1024, height = 800)
cv.place(x=0,y=0)
bg= loadImage("bg2.png")
cv.create_image(0,0, anchor =  "nw", image = bg)  #pos x, pos y, image

cpu_label1=Label(window, bg='white', fg='black', text=ID1).place(x=60,y=75)
cpu_label2=Label(window, bg='white', fg='black', text=ID2).place(x=200,y=75)
cpu_label3=Label(window, bg='white', fg='black', text=ID3).place(x=340,y=75)
cpu_label4=Label(window, bg='white', fg='black', text=ID4).place(x=460,y=75)



cash_cpu1 = Listbox(window, background="white", foreground="black", height=19)
cash_cpu1.place(x=50,y=150)
miss_1 = Listbox(window, background="black", foreground="white", height=5)
miss_1.place(x=50,y=500)

ins_cpu1 = Listbox(window, background="#2596be", foreground="black", height=2)
ins_cpu1.place(x=50,y=100)

cash_cpu2 = Listbox(window, background="white", foreground="black", height=19)
cash_cpu2.place(x=200,y=150)
ins_cpu2 = Listbox(window, background="#2596be", foreground="black", height=2)
ins_cpu2.place(x=200,y=100)
miss_2 = Listbox(window, background="black", foreground="white", height=5)
miss_2.place(x=200,y=500)


cash_cpu3 = Listbox(window, background="white", foreground="black", height=19)
cash_cpu3.place(x=340,y=150)
ins_cpu3 = Listbox(window, background="#2596be", foreground="black", height=2)
ins_cpu3.place(x=340,y=100)
miss_3 = Listbox(window, background="black", foreground="white", height=5)
miss_3.place(x=340,y=500)

cash_cpu4 = Listbox(window, background="white", foreground="black", height=19)
cash_cpu4.place(x=460,y=150)
ins_cpu4 = Listbox(window, background="#2596be", foreground="black", height=2)
ins_cpu4.place(x=460,y=100)
miss_4 = Listbox(window, background="black", foreground="white", height=5)
miss_4.place(x=460,y=500)

mem_label=Label(window, bg='white', fg='black', text="MEMORY").place(x=600,y=75)
mem_list = Listbox(window, background="white", foreground="black", height=19)
mem_list.place(x=600,y=150)

def main():
    
    mt.run()
    while(1):
        #mt.BUS.CACHE_LIST[0].iprint()
        update_cash(cash_cpu1,mt.BUS.CACHE_LIST[0].istring())
        update_cash(cash_cpu2,mt.BUS.CACHE_LIST[1].istring())
        update_cash(cash_cpu3,mt.BUS.CACHE_LIST[2].istring())
        update_cash(cash_cpu4,mt.BUS.CACHE_LIST[3].istring())

        update_mem(mem_list,mt.MEMORY.istring())

        update_miss(miss_1,mt.BUS.WRITE_MISS[0],mt.BUS.READ_MISS[0])
        update_miss(miss_2,mt.BUS.WRITE_MISS[1],mt.BUS.READ_MISS[1])
        update_miss(miss_3,mt.BUS.WRITE_MISS[2],mt.BUS.READ_MISS[2])
        update_miss(miss_4,mt.BUS.WRITE_MISS[3],mt.BUS.READ_MISS[3])

        time.sleep(3)



def update_cash(listbox,cache):
    listbox.delete(0, END)
    listbox.insert(0,'')
    
    for i in range(len(cache)):
        listbox.insert(i+1,cache[i])

def update_mem(listbox,mem):
    listbox.delete(0, END)
    listbox.insert(0,'')
    
    for i in range(len(mem)):
        listbox.insert(i+1,mem[i])

def update_miss(listbox,write,read):
    listbox.delete(0, END)
    listbox.insert(0,'')
    listbox.insert(1,'WRITE MISS: '+str(write))
    listbox.insert(2,'READ MISS: '+str(read))

main_th = threading.Thread(target=main)
main_th.start()        
window.mainloop()