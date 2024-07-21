import conexion as x  

x.cursor.execute ("INSERT INTO stocks VALUES ('2024-01-05','PRUEBA','RHAT',100,35.14)")

x.con.commit()
x.con.close()
print("Insert correcto")
