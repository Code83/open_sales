import sqlite3

con = sqlite3.connect('ejemplo.db')
cursor = con.cursor()
print("Conexion correcta")