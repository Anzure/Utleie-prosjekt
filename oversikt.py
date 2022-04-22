from model.component import Component
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
cursor.execute("SELECT * FROM komponent")
cursor = cursor.fetchall()
elements = np.array(cursor)
cursor = cursor.clear()
print("Loaded all data.")

print("Viser oversikt over komponenter...")
components = []
for element in elements:
    id = int(element[0])
    name = str(element[1])
    available = int(element[2])
    cursor = database.cursor()
    cursor.execute("SELECT COUNT(*) FROM leie WHERE komponent_id LIKE " + str(id))
    cursor = cursor.fetchall()
    missing = int(np.array(cursor)[0])
    cursor.clear()
    component = Component(id, name, available, missing)
    components.append(component)


print("%-10s" % f"ID", end="")
print("%-20s" % f"Navn", end="")
print("%-20s" % f"Tilgjengelig", end="")
print("%-20s" % f"Antall i bruk")
for component in components:
    print("%-10s" % f"{component.id}", end="")
    print("%-20s" % f"{component.name}", end="")
    print("%-20s" % f"{component.available}", end="")
    print("%-20s" % f"{component.missing}")
