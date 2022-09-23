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
bg= loadImage("Inicio.png")
cv.create_image(0,0, anchor =  "nw", image = bg)  #pos x, pos y, image

#BOTONES MAIN WINDOW
#userBtn = loadImage("user_btn.png") #modo de uso user
#adminBtn = loadImage("admin_btn.png") #modo de uso admin
botonUser = Button(window, command=hello,'''image=userBtn,''' borderwidth=0, bg='black', fg='white').place(x=200,y=450)
botonAdmin = Button(window, command=hello, '''image=adminBtn, borderwidth=0,''' bg='black', fg='white').place(x=650,y=450)
       

window.mainloop()