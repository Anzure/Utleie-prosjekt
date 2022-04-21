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

print("Loading all data...")
cursor = database.cursor()
cursor.execute("SELECT * FROM komponenter")
cursor = cursor.fetchall()
components = np.array(cursor)
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
    cursor.execute("SELECT `Låner ID` FROM låner WHERE `E-post` LIKE '" + email + "'")
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
    cursor.execute("SELECT `Komponent ID` FROM komponenter WHERE Navn LIKE '" + name + "'")
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
    cursor.execute("INSERT INTO låner (`Navn`, `Mobilnummer`, `E-post`) VALUES ('" + name + "', '" + phone + "', '" + email + "')")
    database.commit()

def create_or_get_user(name, phone, email):
    user = get_user(email)
    if (user == NULL):
        create_user(name, phone, email)
        user = get_user(email)
    return user

def create_borrow(component_id, user_id):
    cursor = database.cursor()
    cursor.execute("INSERT INTO lån (`Komponenter_Komponent ID`, `Låner_Låner ID`) VALUES ('" + component_id + "', '" + user_id + "')")
    database.commit()

def update_component(component_id, amount):
    cursor = database.cursor()
    cursor.execute("UPDATE komponenter SET `Beholdning` = " + amount + " WHERE `Komponent ID` LIKE " + component_id + "")
    database.commit()

def insert():
    
    if (name_field.get() == "" and
        phone_field.get() == "" and
        email_field.get() == "" and
        component_field.get() == "" and
        deadline_field.get() == ""):
             
        print("empty input")
 
    else:
        
        cursor = database.cursor()
        cursor.execute("SELECT Beholdning FROM komponenter WHERE Navn LIKE '" + component_name.get() + "'")
        cursor = cursor.fetchall()
        amount = int(np.array(cursor)[0])
        print(amount)
        cursor = cursor.clear()

        if (amount <= 0):
            messagebox.showerror("Tomt", "Ikke på lager")

        else:
            print(name_field.get(), phone_field.get(), email_field.get())
            user_id = int(create_or_get_user(name_field.get(), phone_field.get(), email_field.get()))
            component_id = int(get_component(component_name.get()))
            print(user_id, amount, component_id)
            update_component(component_id=str(component_id), amount=str(amount-1))
            create_borrow(component_id=str(component_id), user_id=str(user_id))
            name_field.focus_set()
            clear()


if __name__ == "__main__":
     
    root = tk.Tk()
    root.configure(background='dark green')
    root.title("Registrer utlån")
    root.geometry("500x250")
 
    heading = tk.Label(root, text="Utlånsskjema", bg="dark green")
    name_label = tk.Label(root, text="Navn", bg="dark green")
    phone_label = tk.Label(root, text="Telefonnummer", bg="dark green")
    email_label = tk.Label(root, text="E-postadresse", bg="dark green")
    component_label = tk.Label(root, text="Komponent", bg="dark green")
    deadline_label = tk.Label(root, text="Leveringsfrist", bg="dark green")
    
    heading.grid(row=0, column=1)
    name_label.grid(row=1, column=0)
    phone_label.grid(row=2, column=0)
    email_label.grid(row=3, column=0)
    component_label.grid(row=4, column=0)
    deadline_label.grid(row=5, column=0)
    
    name_field = tk.Entry(root)
    phone_field = tk.Entry(root)
    email_field = tk.Entry(root)
    component_name = tk.StringVar(root)
    component_name.set(component_names[0])
    component_field = tk.OptionMenu(root, component_name, *component_names)
    deadline_field = tk.Entry(root)

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
    
    submit = tk.Button(root, text="Registrer utlån", fg="Black",
                            bg="Grey", command=insert)
    submit.grid(row=6, column=1)
    root.mainloop()