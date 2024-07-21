import conexion as x  

x.cursor.execute ("DELETE FROM stocks")

x.con.commit()
x.con.close()
print("Insert correcto, bd cerrada")