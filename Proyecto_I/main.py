
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
TIMER=5
mt = Multiprocessor(ID1,ID2,ID3,ID4,TIMER)

#***************Cargar Imagenes***********************
#Entrada: Nombre de la imagen
#Restricciones: el nombre de la imagen debe ser formato str
#Salida: Genera la imagen
def loadImage(filename):
    path = os.path.join('images',filename)
    imagen = PhotoImage(file=path)
    return imagen
#***************button function***********************
def hello():
    print("Hello world!")
    
def set_run():
    mt.cpu_02.RUN_STATE='RUN'
    mt.cpu_01.RUN_STATE='RUN'
    mt.cpu_03.RUN_STATE='RUN'
    mt.cpu_04.RUN_STATE='RUN'

def set_step():
    mt.cpu_02.RUN_STATE='STEP'
    mt.cpu_01.RUN_STATE='STEP'
    mt.cpu_03.RUN_STATE='STEP'
    mt.cpu_04.RUN_STATE='STEP'

def set_pause():
    mt.cpu_02.RUN_STATE='PAUSE'
    mt.cpu_01.RUN_STATE='PAUSE'
    mt.cpu_03.RUN_STATE='PAUSE'
    mt.cpu_04.RUN_STATE='PAUSE'

def set_auto():
    mt.cpu_02.EXECUTION_MODE='AUTO'
    mt.cpu_01.EXECUTION_MODE='AUTO'
    mt.cpu_03.EXECUTION_MODE='AUTO'
    mt.cpu_04.EXECUTION_MODE='AUTO'

def set_manual():
    mt.cpu_02.EXECUTION_MODE='MAN'
    mt.cpu_01.EXECUTION_MODE='MAN'
    mt.cpu_03.EXECUTION_MODE='MAN'
    mt.cpu_04.EXECUTION_MODE='MAN'
    get_inst()

def set_stop():
    mt.cpu_02.EXECUTION_MODE='STOP'
    mt.cpu_01.EXECUTION_MODE='STOP'
    mt.cpu_03.EXECUTION_MODE='STOP'
    mt.cpu_04.EXECUTION_MODE='STOP'


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



#cpu labels
cpu_label1=Label(window, bg='white', fg='black', text=ID1).place(x=100,y=20)
cpu_label2=Label(window, bg='white', fg='black', text=ID2).place(x=320,y=20)
cpu_label3=Label(window, bg='white', fg='black', text=ID3).place(x=100,y=310)
cpu_label4=Label(window, bg='white', fg='black', text=ID4).place(x=320,y=310)

#cache1
ins_cpu1 = Listbox(window, background="#2596be", foreground="black", height=2)
ins_cpu1.place(x=60,y=50)
cash_cpu1 = Listbox(window, background="white", foreground="black", height=7, width=30)
cash_cpu1.place(x=30,y=100)
miss_1 = Listbox(window, background="black", foreground="white", height=3)
miss_1.place(x=60,y=230)

#cache2
ins_cpu2 = Listbox(window, background="#2596be", foreground="black", height=2)
ins_cpu2.place(x=280,y=50)
cash_cpu2 = Listbox(window, background="white", foreground="black", height=7, width=30)
cash_cpu2.place(x=250,y=100)
miss_2 = Listbox(window, background="black", foreground="white", height=3)
miss_2.place(x=280,y=230)

#cache3
ins_cpu3 = Listbox(window, background="#2596be", foreground="black", height=2)
ins_cpu3.place(x=60,y=340)
cash_cpu3 = Listbox(window, background="white", foreground="black", height=7, width=30)
cash_cpu3.place(x=30,y=390)
miss_3 = Listbox(window, background="black", foreground="white", height=3)
miss_3.place(x=60,y=520)

#cache4
ins_cpu4 = Listbox(window, background="#2596be", foreground="black", height=2)
ins_cpu4.place(x=280,y=340)
cash_cpu4 = Listbox(window, background="white", foreground="black", height=7, width=30)
cash_cpu4.place(x=250,y=390)
miss_4 = Listbox(window, background="black", foreground="white", height=3)
miss_4.place(x=280,y=520)

#memory
mem_label=Label(window, bg='white', fg='black', text="MEMORY").place(x=530,y=20)
mem_list = Listbox(window, background="white", foreground="black", height=10, width=40)
mem_list.place(x=500,y=80)


auto_btn = loadImage('auto_btn.png')
manual_btn = loadImage('manual_btn.png')
pause_btn = loadImage('pause_btn.png')
run_btn = loadImage('run_btn.png')
next_btn = loadImage('nxt_btn.png')

automode_button = Button(window, command=set_auto, borderwidth=0, image=auto_btn, bg='black').place(x=800,y=25)
manualmode_button = Button(window, command=set_manual, borderwidth=0, image=manual_btn, bg='black').place(x=800,y=85)
pause_button = Button(window, command=set_pause, borderwidth=0, image=pause_btn, bg='black').place(x=800,y=200)
run_button = Button(window, command=set_run, borderwidth=0, image=run_btn, bg='black').place(x=800,y=300)       
next_button = Button(window, command=set_step, borderwidth=0,image=next_btn, bg='black').place(x=800,y=400)
stop_button = Button(window, command=set_stop, text='STOP',borderwidth=0, bg='red').place(x=800,y=550)

inst_1 = Entry(window, width=20)
inst_1.place(x=530,y=400)
inst_2 = Entry(window, width=20)
inst_2.place(x=530,y=420)
inst_3 = Entry(window, width=20)
inst_3.place(x=530,y=440)
inst_4 = Entry(window, width=20)
inst_4.place(x=530,y=460)

def get_inst():
    mt.cpu_01.INPUT_INS= inst_1.get().split()
    mt.cpu_02.INPUT_INS= inst_2.get().split()
    mt.cpu_03.INPUT_INS= inst_3.get().split()
    mt.cpu_04.INPUT_INS= inst_4.get().split()



def main():
    
    mt.run()
    while(1):
        update_cash(cash_cpu1,mt.BUS.CACHE_LIST[0].istring())
        update_cash(cash_cpu2,mt.BUS.CACHE_LIST[1].istring())
        update_cash(cash_cpu3,mt.BUS.CACHE_LIST[2].istring())
        update_cash(cash_cpu4,mt.BUS.CACHE_LIST[3].istring())

        update_mem(mem_list,mt.MEMORY.istring())

        update_miss(miss_1,mt.BUS.WRITE_MISS[0],mt.BUS.READ_MISS[0])
        update_miss(miss_2,mt.BUS.WRITE_MISS[1],mt.BUS.READ_MISS[1])
        update_miss(miss_3,mt.BUS.WRITE_MISS[2],mt.BUS.READ_MISS[2])
        update_miss(miss_4,mt.BUS.WRITE_MISS[3],mt.BUS.READ_MISS[3])

        update_inst(ins_cpu1,mt.cpu_01.INSTRUCTION.istring())
        update_inst(ins_cpu2,mt.cpu_02.INSTRUCTION.istring())
        update_inst(ins_cpu3,mt.cpu_03.INSTRUCTION.istring())
        update_inst(ins_cpu4,mt.cpu_04.INSTRUCTION.istring())
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

def update_inst(listbox,instruction):
    listbox.delete(0, END)
    listbox.insert(0,'')
    listbox.insert(0,instruction)


main_th = threading.Thread(target=main)
main_th.start()        
window.mainloop()