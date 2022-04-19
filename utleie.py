import mysql.connector
import tkinter as tk

print("Connecting to database...")
database = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Hallo123",
    database="utleie"
)
print("Connected to database.")

components = ["one", "two", "three"]

def focus1(event):
    course_field.focus_set()

def focus2(event):
    sem_field.focus_set()
 
def focus3(event):
    form_no_field.focus_set()
 
def focus4(event):
    contact_no_field.focus_set()
 
def focus5(event):
    email_id_field.focus_set()
 
def focus6(event):
    address_field.focus_set()
 
def clear():
     
    name_field.delete(0, tk.END)
    course_field.delete(0, tk.END)
    sem_field.delete(0, tk.END)
    form_no_field.delete(0, tk.END)
    contact_no_field.delete(0, tk.END)
    email_id_field.delete(0, tk.END)
    address_field.delete(0, tk.END)
 
def insert():
    
    if (name_field.get() == "" and
        course_field.get() == "" and
        sem_field.get() == "" and
        form_no_field.get() == "" and
        contact_no_field.get() == "" and
        email_id_field.get() == "" and
        address_field.get() == ""):
             
        print("empty input")
 
    else:
        
        name_field.focus_set()
        
        clear()
 

if __name__ == "__main__":
     
    root = tk.Tk()
 
    root.configure(background='dark green')
 
    root.title("Registrer utlån")
 
    root.geometry("500x300")
 
    heading = tk.Label(root, text="Utlånsskjema", bg="dark green")
 
    name = tk.Label(root, text="Navn", bg="dark green")
 
    course = tk.Label(root, text="Telefonnummer", bg="dark green")
 
    sem = tk.Label(root, text="E-postadresse", bg="dark green")
 
    form_no = tk.Label(root, text="Komponent", bg="dark green")
 
    contact_no = tk.Label(root, text="Leveringsfrist", bg="dark green")
 
    email_id = tk.Label(root, text="Plassholder 1", bg="dark green")

    address = tk.Label(root, text="Plassholder 2", bg="dark green")
    
    heading.grid(row=0, column=1)
    name.grid(row=1, column=0)
    course.grid(row=2, column=0)
    sem.grid(row=3, column=0)
    form_no.grid(row=4, column=0)
    contact_no.grid(row=5, column=0)
    email_id.grid(row=6, column=0)
    address.grid(row=7, column=0)
    
    name_field = tk.Entry(root)
    course_field = tk.Entry(root)
    sem_field = tk.Entry(root)

    #form_no_field = tk.Entry(root)
    component = tk.StringVar(root)
    component.set(components[0])
    form_no_field = tk.OptionMenu(root, component, *components)

    contact_no_field = tk.Entry(root)
    email_id_field = tk.Entry(root)
    address_field = tk.Entry(root)

    name_field.bind("<Return>", focus1)

    course_field.bind("<Return>", focus2)
 
    sem_field.bind("<Return>", focus3)
 
    form_no_field.bind("<Return>", focus4)
 
    contact_no_field.bind("<Return>", focus5)
 
    email_id_field.bind("<Return>", focus6)

    name_field.grid(row=1, column=1, ipadx="100")
    course_field.grid(row=2, column=1, ipadx="100")
    sem_field.grid(row=3, column=1, ipadx="100")
    form_no_field.grid(row=4, column=1, ipadx="100")
    contact_no_field.grid(row=5, column=1, ipadx="100")
    email_id_field.grid(row=6, column=1, ipadx="100")
    address_field.grid(row=7, column=1, ipadx="100")
    
    submit = tk.Button(root, text="Registrer utlån", fg="Black",
                            bg="Grey", command=insert)
    submit.grid(row=8, column=1)
 
    root.mainloop()