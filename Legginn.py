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
    "CREATE TABLE IF NOT EXISTS Komponenter (KomponentID int auto_increment PRIMARY KEY NOT NULL, Navn VARCHAR(45), Beholdning int)"
)
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Lån (idLån int auto_increment PRIMARY KEY NOT NULL, komponentID int, LånerID int)"
)
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Leier (LånerID int auto_increment PRIMARY KEY NOT NULL, Navn varchar(45), Utlånsdato date, leveringsfrist date, Epost varchar(45), TLF int)"
)

print("Execution complete")


# Tenkt modell for funksjoner som skal hente info fra gui
# def nyKompNavn():
#    NyKomp = navn.get()


nykomp = "INSERT INTO Komponenter (Navn) VALUER (%s)"  # Grunnlag for kommando som skal legge inn nytt komponent. ID har autoinc og ordner seg selv.
