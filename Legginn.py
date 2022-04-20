import mysql.connector
import tkinter as tk
from tkinter import *
import tkinter.messagebox as MessageBox


print("Connecting to database...")
database = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="WifiKoster100KrMB",
    database="utleie",
)
print("Connected to database.")

mycursor = database.cursor()

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Komponenter (KomponentID int auto_increment PRIMARY KEY NOT NULL, Navn VARCHAR(45), Beholdning int)"
)
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Lån (idLån int auto_increment PRIMARY KEY NOT NULL, komponentID int, LånerID int)"
)
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Leier (LånerID int auto_increment PRIMARY KEY NOT NULL, Navn varchar(45), Utlånsdato date, leveringsfrist date, Epost varchar(45), TLF int)"
)

print("Execution complete")


def insert():
    knavn = in_knavn.get()
    kAnt = in_kAnt.get()

    if knavn == "" or kAnt == "":
        MessageBox.showinfo("Fyll alle felt")
    else:
        mycursor.execute("INSERT INTO komponenter(Navn) VALUES ('" + knavn + "')")
        mycursor.execute("commit")

        MessageBox.showinfo("Komponent registrert")
        database.close()


root = Tk()
root.configure(background="dark green")
root.geometry("600x300")
root.title("Registrer ny komponent")

knavn = Label(root, text="Komponentnavn", font=("bold", 10), bg="dark green")
knavn.place(x=30, y=50)

kAnt = Label(root, text="Antall enheter: ", font=("bold", 10), bg="dark green")
kAnt.place(x=30, y=80)

in_knavn = Entry()
in_knavn.place(x=160, y=50)

in_kAnt = Entry()
in_kAnt.place(x=160, y=80)

submit = tk.Button(root, text="Registrer", fg="Black", bg="Grey", command=insert)
submit.place(x=90, y=200)

root.mainloop()
