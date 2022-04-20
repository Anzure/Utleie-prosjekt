import mysql.connector
import tkinter as tk

print("Connecting to database...")
database = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="*********",
    database="***********",
)
print("Connected to database.")

mycursor = database.cursor()

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Komponenter (KomponentID int, Navn VARCHAR(45), Beholdning int, PRIMARY KEY(KomponentID))"
)
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Lån (idLån int, komponentID int, LånerID int, PRIMARY KEY(idLån))"
)
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Leier (LånerID int, Navn varchar(45), Utlånsdato date, leveringsfrist date, Epost varchar(45), TLF int, PRIMARY KEY(LånerID))"
)

print("Execution complete")
