from tkinter import *  # Carga módulo tk (widgets estándar)

raiz=Tk()    # Define la ventana principal de la aplicación
raiz.title("Primera ventana")  # Asigna un título a la ventana
raiz.resizable(1,1)
raiz.iconbitmap("alejandro-magno4.ico")
raiz.config(bg="black")   # Asigna un color de fondo a la ventana. Si se omite
raiz.config(bd=35)
raiz.config(relief="groove")
raiz.config(cursor="hand2")

miFrame=Frame()
miFrame.pack(fill="y", expand="0")
miFrame.config(bg="red")
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
miFrame.config(relief="groove")
miFrame.config(cursor="pirate")


raiz.mainloop()