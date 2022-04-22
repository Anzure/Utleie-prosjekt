from asyncio.windows_events import NULL
import mysql.connector
import tkinter as tk
import numpy as np
from tkinter import messagebox

print("Connecting to database...")
database = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Hallo123",
    database="utleie"
)
print("Connected to database.")

def load_components():
    print("Loading all data...")
    cursor = database.cursor()
    cursor.execute("SELECT * FROM komponent")
    cursor = cursor.fetchall()
    global components
    components = np.array(cursor)
    global component_names
    component_names = []
    for component in components:
        component_names.append(component[1])
    cursor = cursor.clear()
    print("Loaded all data.")

def focus1(event):
    name_field.focus_set()

def focus2(event):
    phone_field.focus_set()
 
def focus3(event):
    email_field.focus_set()
 
def focus4(event):
    component_field.focus_set()

def focus5(event):
    deadline_field.focus_set()
 
def clear():
     
    name_field.delete(0, tk.END)
    phone_field.delete(0, tk.END)
    email_field.delete(0, tk.END)
    deadline_field.delete(0, tk.END)

def get_user(email):
    cursor = database.cursor()
    cursor.execute("SELECT id FROM bruker WHERE epost LIKE '" + email + "'")
    cursor = cursor.fetchall()
    users = np.array(cursor)
    if (len(users) > 0):
        user_id = int(users[0])
        cursor.clear()
        return user_id
    else:
        return NULL

def get_component(name):
    cursor = database.cursor()
    cursor.execute("SELECT id FROM komponent WHERE navn LIKE '" + name + "'")
    cursor = cursor.fetchall()
    elements = np.array(cursor)
    if (len(elements) > 0):
        component_id = int(elements[0])
        cursor.clear()
        return component_id
    else:
        return NULL

def create_user(name, phone, email):
    cursor = database.cursor()
    cursor.execute("INSERT INTO bruker (navn, telefon, epost) VALUES ('" + name + "', '" + phone + "', '" + email + "')")
    database.commit()

def create_or_get_user(name, phone, email):
    user = get_user(email)
    if (user == NULL):
        create_user(name, phone, email)
        user = get_user(email)
    return user

def create_borrow(component_id, user_id):
    cursor = database.cursor()
    cursor.execute("INSERT INTO leie (komponent_id, bruker_id) VALUES ('" + component_id + "', '" + user_id + "')")
    database.commit()

def update_component(component_id, amount):
    cursor = database.cursor()
    cursor.execute("UPDATE komponent SET beholdning = " + amount + " WHERE id LIKE " + component_id + "")
    database.commit()

def insert_borrow():
    
    if (name_field.get() == "" and
        phone_field.get() == "" and
        email_field.get() == "" and
        component_field.get() == "" and
        deadline_field.get() == ""):

        messagebox.showwarning("Mangler inndata", "Vennligst fyll ut alle felt")
 
    else:
        cursor = database.cursor()
        cursor.execute("SELECT beholdning FROM komponent WHERE navn LIKE '" + component_name.get() + "'")
        cursor = cursor.fetchall()
        amount = int(np.array(cursor)[0])
        cursor = cursor.clear()

        if (amount <= 0):
            messagebox.showerror("Tomt på lager", "Det er ikke flere komponenter på lager")

        else:
            user_id = int(create_or_get_user(name_field.get(), phone_field.get(), email_field.get()))
            component_id = int(get_component(component_name.get()))
            update_component(component_id=str(component_id), amount=str(amount-1))
            create_borrow(component_id=str(component_id), user_id=str(user_id))
            name_field.focus_set()
            clear()
            messagebox.showinfo("Suksess", "Utleie registrert")

def insert_component():
    knavn = in_knavn.get()
    kAnt = in_kAnt.get()

    if knavn == "" or kAnt == "" or kAnt == "0":
        messagebox.showinfo(
            title="Feil", message="Fyll alle felt. Antall må være 1 eller fler")
    else:
        cursor = database.cursor()
        cursor.execute("INSERT INTO komponent (navn, beholdning) VALUES ('" + knavn + "'," + kAnt + ")")
        cursor.execute("commit")
        messagebox.showinfo(title="Info", message="Komponent registrert")


def close_rental_window():
    root.deiconify()
    rental.destroy()
    
def open_rental_window():
    load_components()
    contruct_rental()
    root.withdraw()

def close_register_window():
    root.deiconify()
    register.destroy()
    
def open_register_window():
    construct_register()
    root.withdraw()

def contruct_rental():
    global rental
    rental = tk.Toplevel(root)
    rental.configure(background='dark green')
    rental.title("Registrer utlån")
    rental.geometry("500x250")
 
    heading = tk.Label(rental, text="Utlånsskjema", bg="dark green")
    name_label = tk.Label(rental, text="Navn", bg="dark green")
    phone_label = tk.Label(rental, text="Telefonnummer", bg="dark green")
    email_label = tk.Label(rental, text="E-postadresse", bg="dark green")
    component_label = tk.Label(rental, text="Komponent", bg="dark green")
    deadline_label = tk.Label(rental, text="Leveringsfrist", bg="dark green")
    
    heading.grid(row=0, column=1)
    name_label.grid(row=1, column=0)
    phone_label.grid(row=2, column=0)
    email_label.grid(row=3, column=0)
    component_label.grid(row=4, column=0)
    deadline_label.grid(row=5, column=0)
    
    global name_field
    name_field = tk.Entry(rental)
    global phone_field
    phone_field = tk.Entry(rental)
    global email_field
    email_field = tk.Entry(rental)
    global component_name
    component_name = tk.StringVar(rental)
    component_name.set(component_names[0])
    global component_field
    component_field = tk.OptionMenu(rental, component_name, *component_names)
    global deadline_field
    deadline_field = tk.Entry(rental)

    name_field.bind("<Return>", focus1)
    phone_field.bind("<Return>", focus2)
    email_field.bind("<Return>", focus3)
    component_field.bind("<Return>", focus4)
    deadline_field.bind("<Return>", focus5)

    name_field.grid(row=1, column=1, ipadx="100")
    phone_field.grid(row=2, column=1, ipadx="100")
    email_field.grid(row=3, column=1, ipadx="100")
    component_field.grid(row=4, column=1, ipadx="100")
    deadline_field.grid(row=5, column=1, ipadx="100")
    
    submit_borrow = tk.Button(rental, text="Registrer utlån", fg="Black",
                            bg="Grey", command=insert_borrow)
    submit_borrow.grid(row=6, column=1)

    rental.protocol("WM_DELETE_WINDOW", close_rental_window)

def construct_register():
    global register
    register = tk.Toplevel(root)
    register.configure(background="dark green")
    register.geometry("600x300")
    register.title("Registrer ny komponent")

    knavn = tk.Label(register, text="Komponentnavn", font=("bold", 10), bg="dark green")
    knavn.place(x=30, y=50)

    kAnt = tk.Label(register, text="Antall enheter: ", font=("bold", 10), bg="dark green")
    kAnt.place(x=30, y=80)

    global in_knavn
    in_knavn = tk.Entry(register)
    in_knavn.place(x=160, y=50)

    global in_kAnt
    in_kAnt = tk.Entry(register)
    in_kAnt.place(x=160, y=80)

    register_submit = tk.Button(register, text="Registrer", fg="Black",
                    bg="Grey", command=insert_component)
    register_submit.place(x=90, y=200)
    
    register.protocol("WM_DELETE_WINDOW", close_register_window)

if __name__ == "__main__":

    root = tk.Tk()
    root.configure(background='dark green')
    root.title("Meny")
    root.geometry("500x250")

    heading = tk.Label(root, text="Meny", bg="dark green")
    heading.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    button1 = tk.Button(root, text="Lån av utstyr", fg="Black", bg="Grey", command=open_rental_window)
    button2 = tk.Button(root, text="Legge til nytt komponent", fg="Black", bg="Grey", command=open_register_window)
    button1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    button2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    
    root.mainloop()
    
