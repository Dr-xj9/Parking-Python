import mysql.connector
import vehiculos as vh
import conexion as con

#class base de datos vehiculos
class dbVehiculo:
    def save(self,vehiculo):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        
        self.sql="insert into vehiculos(matricula, modelo, marca, color, cliente_id) values(%s,%s,%s,%s,%s)"
        self.datos=(vehiculo.getMatricula(),
                    vehiculo.getModelo(),
                    vehiculo.getMarca(),
                    vehiculo.getColor(),
                    vehiculo.getCliente_id())
        
        self.cursor1.execute(self.sql,self.datos)
        self.conn.commit()
        self.conn.close()
    
    def search(self, vehiculos):
        aux=None
        try:
            self.con=con.conexion()
            self.conn=self.con.open()
            self.cursor1=self.conn.cursor()
            self.sql="select * from vehiculos where matricula=%s"
            self.cursor1.execute(self.sql, (vehiculos.getMatricula(),))
            row=self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            if(row[0] is not None):
                aux = vh.vehiculo()
                aux.setMatricula(row[0])
                aux.setModelo(row[1])
                aux.setMarca(row[2])
                aux.setColor(row[3])
                aux.setCliente_id(row[4])
        except:
                print("Saluditos")
        return aux
        
    def edit(self, vehiculos):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="update vehiculos set modelo=%s, marca=%s, color=%s where matricula=%s"
        self.datos=(vehiculos.getModelo(),
                    vehiculos.getMarca(),
                    vehiculos.getColor(),
                    vehiculos.getMatricula())
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()
        
    def remove(self, vehiculos):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="delete from vehiculos where matricula=%s"
        self.cursor1.execute(self.sql, (vehiculos.getMatricula(),))
        self.conn.commit()
        self.conn.close()
             
    def close(self):
        self.conn.close()