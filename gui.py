from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import os
import sys

#Variables *******************************************
instr0 = 'READ 000'
cpu = '01'
id0 = 'cpu01'
id1 = 'cpu02'
id2 = 'cpu03'
id3 = 'cpu04'

#memory -----------------------------------------------
add0=0
add1=1
add2=2
add3=3
add4=4
add5=5
add6=6
add7=7

data0=0
data1=1
data2=2
data3=3
data4=4
data5=5
data6=6
data7=7

#cache 0 -------------------------------------------------------
tag00=0
tag01=1
tag02=2
tag03=3

data00=0
data01=1
data02=2
data03=3

st00=0
st01=1
st02=2
st03=3

#cache 1 -------------------------------------------------------
tag10=0
tag11=1
tag12=2
tag13=3

data10=0
data11=1
data12=2
data13=3

st10=0
st11=1
st12=2
st13=3

#cache 2 -------------------------------------------------------
tag20=0
tag21=1
tag22=2
tag23=3

data20=0
data21=1
data22=2
data23=3

st20=0
st21=1
st22=2
st23=3

#cache 3 -------------------------------------------------------
tag30=0
tag31=1
tag32=2
tag33=3

data30=0
data31=1
data32=2
data33=3

st30=0
st31=1
st32=2
st33=3

#***************button function***********************
def hello():
    print("Hello world!")

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
bg= loadImage("bg.png")
cv.create_image(0,0, anchor =  "nw", image = bg)  #pos x, pos y, image

#Buttons
auto_btn = loadImage('auto_btn.png')
manual_btn = loadImage('manual_btn.png')
pause_btn = loadImage('pause_btn.png')
run_btn = loadImage('run_btn.png')
next_btn = loadImage('nxt_btn.png')

automode_button = Button(window, command=hello, borderwidth=0, image=auto_btn, bg='black').place(x=150,y=25)
manualmode_button = Button(window, command=hello, borderwidth=0, image=manual_btn, bg='black').place(x=150,y=85)
pause_button = Button(window, command=hello, borderwidth=0, image=pause_btn, bg='black').place(x=20,y=85)
run_button = Button(window, command=hello, borderwidth=0, image=run_btn, bg='black').place(x=20,y=25)       
next_button = Button(window, command=hello, borderwidth=0,image=next_btn, bg='black').place(x=85,y=145)

#Labels
instr0_label=Label(window, bg='white', fg='black', text=(instr0)).place(x=130,y=258)
cpu_label=Label(window, bg='white', fg='black', text=cpu).place(x=60,y=322)
id0_label=Label(window, bg='white', fg='black', text=id0).place(x=590,y=40)
id1_label=Label(window, bg='white', fg='black', text=id1).place(x=830,y=40)
id2_label=Label(window, bg='white', fg='black', text=id2).place(x=590,y=330)
id3_label=Label(window, bg='white', fg='black', text=id3).place(x=830,y=330)

#memory labels---------------------------------------------------------
add0_label=Label(window, bg='white', fg='black', text=add0).place(x=350,y=160)
add1_label=Label(window, bg='white', fg='black', text=add1).place(x=350,y=210)
add2_label=Label(window, bg='white', fg='black', text=add2).place(x=350,y=260)
add3_label=Label(window, bg='white', fg='black', text=add3).place(x=350,y=310)
add4_label=Label(window, bg='white', fg='black', text=add4).place(x=350,y=360)
add5_label=Label(window, bg='white', fg='black', text=add5).place(x=350,y=410)
add6_label=Label(window, bg='white', fg='black', text=add6).place(x=350,y=460)
add7_label=Label(window, bg='white', fg='black', text=add7).place(x=350,y=510)

data0_label=Label(window, bg='white', fg='black', text=data0).place(x=450,y=160)
data1_label=Label(window, bg='white', fg='black', text=data1).place(x=450,y=210)
data2_label=Label(window, bg='white', fg='black', text=data2).place(x=450,y=260)
data3_label=Label(window, bg='white', fg='black', text=data3).place(x=450,y=310)
data4_label=Label(window, bg='white', fg='black', text=data4).place(x=450,y=360)
data5_label=Label(window, bg='white', fg='black', text=data5).place(x=450,y=410)
data6_label=Label(window, bg='white', fg='black', text=data6).place(x=450,y=460)
data7_label=Label(window, bg='white', fg='black', text=data7).place(x=450,y=510)

#cache 0 labels-------------------------------------------------------
tag00_label=Label(window, bg='white', fg='black', text=tag00).place(x=610,y=120)
tag01_label=Label(window, bg='white', fg='black', text=tag01).place(x=610,y=160)
tag02_label=Label(window, bg='white', fg='black', text=tag02).place(x=610,y=200)
tag03_label=Label(window, bg='white', fg='black', text=tag03).place(x=610,y=240)

data00_label=Label(window, bg='white', fg='black', text=data00).place(x=670,y=120)
data01_label=Label(window, bg='white', fg='black', text=data01).place(x=670,y=160)
data02_label=Label(window, bg='white', fg='black', text=data02).place(x=670,y=200)
data03_label=Label(window, bg='white', fg='black', text=data03).place(x=670,y=240)

st00_label=Label(window, bg='white', fg='black', text=st00).place(x=730,y=120)
st01_label=Label(window, bg='white', fg='black', text=st01).place(x=730,y=160)
st02_label=Label(window, bg='white', fg='black', text=st02).place(x=730,y=200)
st03_label=Label(window, bg='white', fg='black', text=st03).place(x=730,y=240)

#cache 1 labels-------------------------------------------------------
tag10_label=Label(window, bg='white', fg='black', text=tag10).place(x=850,y=120)
tag11_label=Label(window, bg='white', fg='black', text=tag11).place(x=850,y=160)
tag12_label=Label(window, bg='white', fg='black', text=tag12).place(x=850,y=200)
tag13_label=Label(window, bg='white', fg='black', text=tag13).place(x=850,y=240)

data10_label=Label(window, bg='white', fg='black', text=data10).place(x=910,y=120)
data11_label=Label(window, bg='white', fg='black', text=data11).place(x=910,y=160)
data12_label=Label(window, bg='white', fg='black', text=data12).place(x=910,y=200)
data13_label=Label(window, bg='white', fg='black', text=data13).place(x=910,y=240)

st10_label=Label(window, bg='white', fg='black', text=st10).place(x=970,y=120)
st11_label=Label(window, bg='white', fg='black', text=st11).place(x=970,y=160)
st12_label=Label(window, bg='white', fg='black', text=st12).place(x=970,y=200)
st13_label=Label(window, bg='white', fg='black', text=st13).place(x=970,y=240)

#cache 2 labels-------------------------------------------------------
tag20_label=Label(window, bg='white', fg='black', text=tag20).place(x=610,y=415)
tag21_label=Label(window, bg='white', fg='black', text=tag21).place(x=610,y=455)
tag22_label=Label(window, bg='white', fg='black', text=tag22).place(x=610,y=495)
tag23_label=Label(window, bg='white', fg='black', text=tag23).place(x=610,y=535)

data20_label=Label(window, bg='white', fg='black', text=data20).place(x=670,y=415)
data21_label=Label(window, bg='white', fg='black', text=data21).place(x=670,y=455)
data22_label=Label(window, bg='white', fg='black', text=data22).place(x=670,y=495)
data23_label=Label(window, bg='white', fg='black', text=data23).place(x=670,y=535)

st20_label=Label(window, bg='white', fg='black', text=st20).place(x=730,y=415)
st21_label=Label(window, bg='white', fg='black', text=st21).place(x=730,y=455)
st22_label=Label(window, bg='white', fg='black', text=st22).place(x=730,y=495)
st23_label=Label(window, bg='white', fg='black', text=st23).place(x=730,y=535)

#cache 3 labels-------------------------------------------------------
tag30_label=Label(window, bg='white', fg='black', text=tag30).place(x=850,y=415)
tag31_label=Label(window, bg='white', fg='black', text=tag31).place(x=850,y=455)
tag32_label=Label(window, bg='white', fg='black', text=tag32).place(x=850,y=495)
tag33_label=Label(window, bg='white', fg='black', text=tag33).place(x=850,y=535)

data30_label=Label(window, bg='white', fg='black', text=data30).place(x=910,y=415)
data31_label=Label(window, bg='white', fg='black', text=data31).place(x=910,y=455)
data32_label=Label(window, bg='white', fg='black', text=data32).place(x=910,y=495)
data33_label=Label(window, bg='white', fg='black', text=data33).place(x=910,y=535)

st30_label=Label(window, bg='white', fg='black', text=st30).place(x=970,y=415)
st31_label=Label(window, bg='white', fg='black', text=st31).place(x=970,y=455)
st32_label=Label(window, bg='white', fg='black', text=st32).place(x=970,y=495)
st33_label=Label(window, bg='white', fg='black', text=st33).place(x=970,y=535)

#Entries
freq_entry = Entry(window, width = 20).place(x = 130, y = 404)
instr1_entry = Entry(window, width = 20).place(x = 130, y = 486)


window.mainloop()