#Importamos la librería para trabajar con sqlite
import sqlite3
#creamos la base de datos y creamos la conexión con el cursor
con = sqlite3.connect('ejemplo.db')
cursor = con.cursor()
#creamos una tabla stocks con las columnas típicas
cursor.execute ('''create table stocks 
                               (date text, trans text, symbol text, qty real, price real)''')