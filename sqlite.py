#Importamos la librería para trabajar con sqlite
import sqlite3
#creamos la base de datos y creamos la conexión con el cursor
con = sqlite3.connect('ejemplo.db')
cursor = con.cursor()
#creamos una tabla stocks con las columnas típicas
cursor.execute ('''create table stocks 
                               (date text, trans text, symbol text, qty real, price real)''')
#insertamos valores a la tabla stocks
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#hacemos commit para guardar los datos y cerramos la conexión
con.commit()
con.close()

