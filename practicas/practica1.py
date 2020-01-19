from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

raiz=Tk()
raiz.title("Lily Collins")
raiz.geometry('300x300')
frame=Frame(raiz,  width=1200, height=600)
frame.pack()
frame.config(width="1200", height="650")
frame.config()

#Las variables de control se declaran de forma diferente en función al tipo de dato que almacenan
#Declarar variables de tipo cadena
miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()

def leerdocumento():
    l=messagebox.askretrycancel("Reintentar", "No es posible borrar elementos")
    if l==False:
        raiz.destroy()


#--------------barra de menus en raiz--------------
#Se definen las funciones que dan la accion correspondiente a cada componente de la barra de menu
barramenu=Menu(raiz)
raiz.config(menu=barramenu)
#aparece una especie de elemento por defecto. Podemos    hacer que desaparezca si indicamos el parámetro tearoff=0
archivoMenu=Menu(barramenu, tearoff=0)
barramenu.add_cascade(label="Archivo", menu=archivoMenu)
#cada opcion tiene una lista de opciones el cual se agrega con .add_command(label=" ")
#-----------

archivoMenu.add_command(label="Nuevo")

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir")
    print(fichero)
archivoMenu.add_command(label="Abrir", command=abreFichero)

def guardar():
    fichero=filedialog.asksaveasfilename(title="Guardar")
    print(fichero)
archivoMenu.add_command(label="Guardar", command=guardar)

bssdmenu=Menu(barramenu, tearoff=0)
barramenu.add_cascade(label="BB.DD", menu=bssdmenu)
#-----------
def conexionBBDD():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOICREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            APELLIDO VARCHAR(20),
            PASSWORD VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except:
        messagebox.showwarning("Atencion", "BBDD ya existe")
bssdmenu.add_command(label="Conectar", command=conexionBBDD)

def salirAplicacion():
    va=messagebox.askquestion("Salir","Deseas salir de la aplicacion")
    if va=="yes":
        raiz.destroy()
bssdmenu.add_command(label="Salir", command=salirAplicacion)

crudmenu=Menu(barramenu, tearoff=0)
barramenu.add_cascade(label="CRUD", menu=crudmenu)
crudmenu.add_command(label="Crear")
crudmenu.add_command(label="Leer")
crudmenu.add_command(label="Actualizar")
crudmenu.add_command(label="Borrar")

editMenu=Menu(barramenu, tearoff=0)
barramenu.add_cascade(label="Editar", menu=editMenu)

def limmpiarCampos():
    miID.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    cuadroComentario.delete(1.0, END)
editMenu.add_command(label="Borrar campos", command=limmpiarCampos)

def infoAdicional():
    messagebox.showinfo("Licencia", "Lily es la mas hermosa")
def infoLicencia():
    messagebox.showwarning("Licencia", "No te metas con Lily")
helpmenu=Menu(barramenu, tearoff=0)
barramenu.add_cascade(label="Ayuda", menu=helpmenu)
helpmenu.add_command(label="Acerca de", command=infoAdicional)
helpmenu.add_command(label="Licencia", command= infoLicencia)

#---------------cuadros de Texto en frame---------------

cuadroId=Entry(frame, textvariable=miID)
cuadroId.grid(row=0, column=1, padx=10, pady=10)

cuadronombre=Entry(frame, textvariable=miNombre)
cuadronombre.grid(row=1, column=1, padx=10, pady=10)

cuadroApellido=Entry(frame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroPass=Entry(frame, textvariable=miPass)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)

cuadroComentario=Text(frame, width=16, height=5 )
cuadroComentario.grid(row=4, column=1, padx=10, pady=10)
scrollvert=Scrollbar(frame, command=cuadroComentario)
scrollvert.grid(row=4, column=2, sticky="nsew")
cuadroComentario.config(yscrollcommand=scrollvert.set)


#-------- El widget label utilizado para mostrar textos.-----
# --Suele ser texto estático, de ahí que se llame label o etiqueta de texto.
idlabel=Label(frame, text="Id")
idlabel.grid(row=0, column=0)

nombreLabel=Label(frame, text="Nombre")
nombreLabel.grid(row=1, column=0)

apellidoLabel=Label(frame, text="Apellido")
apellidoLabel.grid(row=2, column=0)

passLabel=Label(frame, text="contraseña")
passLabel.grid(row=3, column=0)

comentarioLabel=Label(frame, text="comentarios")
comentarioLabel.grid(row=4, column=0)

#---------------botones----------
frame2=Frame(raiz)
frame2.pack()

def guardar2():
    fichero=filedialog.asksaveasfile()

botonEnvio=Button(frame2, text="Guardar", command=guardar2)
botonEnvio.pack(side="left")


def crear():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, "
                     "'" + miNombre.get() +
                     "','" + miApellido.get() +
                    "','" + miPass.get() +
                    "','" + cuadroComentario.get("1.0", END) + "')")
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registrado con exito")
botonIniciar=Button(frame2, text="Crear", command=crear)
botonIniciar.pack(side="left")


def leer():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miID.get())
    elUsuario = miCursor.fetchall()
    for usuario in elUsuario:
        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miPass.set(usuario[3])
        cuadroComentario.set(usuario[4])

    miConexion.commit()
botonStop=Button(frame2, text="Leer", command=leer)
botonStop.pack(side="left")

def salirboton():
    valor=messagebox.askokcancel("Salir", "Deseas salir de la aplicaciion?")
    if valor==True:
        raiz.destroy()

botonSalir=Button(frame2, text="Salir", command= salirboton)
botonSalir.pack(side="left")


#

raiz.mainloop()