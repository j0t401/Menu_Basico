import mysql.connector

class Data():
    def __init__(self):
        self.cnn=mysql.connector.connect(host='localhost', user='root', password='psw@Sena2024', database='muen_prueba')

    def __str__(self):
        datos = self.consultarUsuario()
        aux = ''
        for fila in datos:
            aux = aux+str(fila)+'\n'
        return aux
    
    def consultarUsuarios(self):
        conex = self.cnn.cursor()
        sql = 'SELECT * FROM data'
        conex.execute(sql)
        datos = conex.fetchall()
        conex.close()
        return datos
    
    def insertarUsuario(self, nomData, emailData):
        conex = self.cnn.cursor()
        sql = f"INSERT INTO data (Usuario, Email) VALUES ('{nomData}', '{emailData}')"
        conex.execute(sql)
        n = conex.rowcount
        self.cnn.commit()
        conex.close()
        return n
    
    def eliminarUsuario(self, id):
        conex = self.cnn.cursor()
        sql = f'DELETE FROM data WHERE iddata={id}'
        conex.execute(sql)
        n = conex.rowcount
        self.cnn.commit()
        conex.close()
        return n
    
    def editarUsuario(self, id, nomData, emailData):
        conex = self.cnn.cursor()
        sql = f'UPDATE data SET Usuario="{nomData}", Email="{emailData}" WHERE iddata={id}'
        conex.execute(sql)
        n = conex.rowcount
        self.cnn.commit()
        conex.close()
        return n