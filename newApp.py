from tkinter import *
import webbrowser

# ***** Definitions *****

def doNothing():
    print("Ok Ok I wont...")

def openSite():
    url = "http://murfitz.com";
    webbrowser.open(url)

def close_window ():
    root.destroy()

def derp():
    print("Button gotta clicky boop")
###
def show_tax(rate):
    b = gross.get()
    n = round(b / rate, 2)
    net.set(format(n, '.2f'))
    t = round(b - n, 2)
    tax.set(format(t, '.2f'))
###



# ***** Box Shape *****

root = Tk()
root.title("Josh Fitz-Gerald's Simple Program")
root.geometry("350x200")
###
gross = tk.DoubleVar()
net = tk.StringVar()
tax = tk.StringVar()
tk.Label(root, text='Input gross').grid(row=2, column=0, columnspan=5)

e = tk.Entry(root, textvariable=gross)
e.grid(row=3, column=1, columnspan=3, sticky='WE', padx=5, pady=5)

###

# ***** Main Menu *****

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="DD1", menu=fileMenu)
fileMenu.add_command(label="unused1", command=doNothing)
fileMenu.add_command(label="unused2", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="unused3", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="DD2", menu=editMenu)
editMenu.add_command(label="exit", command=close_window)


# ***** The Toolbar *****
#Frame Border
toolbar = Frame(root, bg="blue")
#Button 1
webButt = Button(toolbar, text="To WebPage", command=openSite)
webButt.pack(side=LEFT, padx=2, pady=2)

#Button 2
exitButt = Button(toolbar, text="Exit", command=close_window)
exitButt.pack(side=LEFT, padx=2, pady=2)

#Button 3
derpButt = Button(toolbar, text="Derp", command=derp)
derpButt.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)



# ***** Status Bar *****
status = Label(root, text="Preparing to do Nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()

