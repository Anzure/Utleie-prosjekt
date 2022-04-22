import tkinter as tk
import sys
import threading





 
root = tk.Tk()
root.configure(background='dark green')
root.title("Meny")
root.geometry("500x250")

heading = tk.Label(root, text="Meny", bg="dark green")
heading.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

def command1():
    exec(open("utleie.py").read())

def command2():
    exec(open("Legginn.py").read())

button1 = tk.Button(root, text="Lån av utstyr", fg="Black", bg="Grey", command=command1)
button2 = tk.Button(root, text="Legge til nytt komponent", fg="Black", bg="Grey", command=command2)
button1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
button2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
 
root.mainloop()