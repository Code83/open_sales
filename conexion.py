import sqlite3

con = sqlite3.connect('ejemplo.db')
cursor = con.cursor()

if con is True:
    print("Conexion correcta")