from tkinter import *

root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
miImagen=PhotoImage(file="tenor.gif")
miLabel=Label(miFrame, image=miImagen, text="Eliana es muy hermosa", fg="red", font=("Comic sans MS", 19)).place(x=100, y=200)
#miLabel.pack()

root.mainloop()