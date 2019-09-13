from tkinter import *

root =Tk()

photo =  PhotoImage(file="image.jpg")
label = Label(root, image=photo)
label.pack()

root.mainloop()