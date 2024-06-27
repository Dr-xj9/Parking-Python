import mysql.connector
import conexion as con
import cliente as ct

class dbCliente:
    def searchByName(self, clientes):
        aux=None
        try:
            self.con=con.conexion()
            self.conn=self.con.open()
            self.cursor1=self.conn.cursor()
            self.sql="select * from clientes where nombre=%s"
            self.cursor1.execute(self.sql, (clientes.getNombre(),))
            row=self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            if(row[0] is not None):
                aux = ct.cliente()
                aux.setCliente_id(row[0])
                aux.setNombre(row[1])
                aux.setTelefono(row[2])
                aux.setEmail(row[3])
                aux.setUsuario_id(row[4])
                aux.setRFC(row[5])
        except:
                print("Saluditos")
        return aux
        
    def nombres(self):
        self.con=con.conexion()
        self.conn=self.con.open()
        
        self.cursor1=self.conn.cursor()
        self.sql="select nombre from clientes"
        self.cursor1.execute(self.sql)
        rows=self.cursor1.fetchall()
        self.conn.commit()
        self.conn.close()
        nombres=list(rows)
        return nombres     
        
    def save(self,clientes):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="insert into clientes (nombre,telefono,email,usuario_id,rfc) values(%s,%s,%s,%s,%s)"
        self.datos=(clientes.getNombre(),
                    clientes.getTelefono(),
                    clientes.getEmail(),
                    clientes.getUsuario_id(),
                    clientes.getRFC())   
        self.cursor1.execute(self.sql,self.datos)
        self.conn.commit()
        self.conn.close()
    
    def search(self, clientes):
        aux=None
        try:
            self.con=con.conexion()
            self.conn=self.con.open()
            self.cursor1=self.conn.cursor()
            self.sql="select * from clientes where cliente_id=%s"
            self.cursor1.execute(self.sql, (clientes.getCliente_id(),))
            row=self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            if(row[0] is not None):
                aux = ct.cliente()
                aux.setCliente_id(row[0])
                aux.setNombre(row[1])
                aux.setTelefono(row[2])
                aux.setEmail(row[3])
                aux.setUsuario_id(row[4])
                aux.setRFC(row[5])
        except:
            print("ERROR")
        return aux
        
    def edit(self, clientes):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="update clientes set nombre=%s, telefono=%s, email=%s, rfc=%s where cliente_id={}".format(clientes.getCliente_id())
        self.datos=(clientes.getNombre(), 
                    clientes.getTelefono(),
                    clientes.getEmail(),
                    clientes.getRFC())
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()
        
    def remove(self, clientes):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="delete from clientes where cliente_id={}".format(clientes.getCliente_id())
        self.cursor1.execute(self.sql)
        self.conn.commit()
        self.conn.close()
             
    def close(self):
        self.conn.close()