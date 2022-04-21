import tkinter as tk
 
root = tk.Tk()
root.configure(background='dark green')
root.title("Meny")
root.geometry("500x250")

heading = tk.Label(root, text="Meny", bg="dark green")
heading.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

button1 = tk.Button(root, text="Lån av utstyr", fg="Black", bg="Grey")
button2 = tk.Button(root, text="Legge til nytt komponent", fg="Black", bg="Grey")
button1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
button2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
 
root.mainloop()