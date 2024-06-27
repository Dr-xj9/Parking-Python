import mysql.connector
import conexion as con
import reporte as re
import servicio as s

class dbReporte:
    def crear(self):
        aux=None
        reportes = []
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="SELECT YEAR(fecha_entrada) as año, MONTH(fecha_entrada) as mes,COUNT(fecha_entrada) as entradas, COUNT(fecha_salida) as salidas FROM servicios GROUP BY YEAR(fecha_entrada), MONTH(fecha_entrada) ORDER BY año, mes;"
        self.cursor1.execute(self.sql)
        rows = self.cursor1.fetchall()
        self.conn.commit()
        self.conn.close()
        for row in rows:
            aux = re.reporte()
            aux.set_anio(row[0])
            aux.set_mes(row[1])
            aux.set_entradas(row[2])
            aux.set_salidas(row[3])
            reportes.append(aux)
        return reportes
    
    def crearSemana(self):
        aux=None
        reportes = []
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="SELECT YEAR(fecha_entrada) AS anio, WEEK(fecha_entrada) AS semana,COUNT(*) AS servicios FROM servicios GROUP BY YEAR(fecha_entrada), WEEK(fecha_entrada) ORDER BY anio, semana;"
        self.cursor1.execute(self.sql)
        rows = self.cursor1.fetchall()
        self.conn.commit()
        self.conn.close()
        for row in rows:
            aux = re.semana()
            aux.set_anio(row[0])
            aux.set_semana(row[1])
            aux.set_servicio(row[2])
            reportes.append(aux)
        return reportes
    
class dbPrecio:
    def save(self, precio):
      try:
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="insert into precios(tipo, precio) values(%s,%s)"
        self.datos=(precio.getTipo(),
                    precio.getPrecio())
        self.cursor1.execute(self.sql,self.datos)
        
        self.conn.commit()
        self.conn.close()
      except:
        print("Error")
    
    def getMaxId(self):
        id=1
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "select max(folio_precio) as id from precios"
        self.cursor1.execute(self.sql)
        row=self.cursor1.fetchone()
        self.conn.commit()
        self.conn.close()
        return row[0]

class dbServicio:
    def search(self, servicio):
        aux=None
        try:
            self.con=con.conexion()
            self.conn=self.con.open()
            self.cursor1=self.conn.cursor()
            self.sql="select * from servicios where folio_servicio=%s"
            self.cursor1.execute(self.sql, (servicio.getFolioServicio(),))  # Pasar los parámetros como una tupla
            row=self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            if(row[0] is not None):
                aux = s.servicio()
                aux.setFolioServicio(row[0])
                aux.setMatricula(row[1])
                aux.setFechaEntrada(row[2])
                aux.setHoraEntrada(row[3])
                aux.setFechaSalida(row[4])
                aux.setHoraSalida(row[5])
                aux.setFolioPrecio(row[6])
                aux.setTipoServicio(row[7])
                print("Encontrado")
        except Exception as e:
            print(f"Error: {e}")
        return aux
        
    def save(self, servicio):
      try:
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="insert into servicios(matricula, fecha_entrada,hora_entrada,fecha_salida,hora_salida,folio_precio,tipo_servicio) values(%s,%s,%s,%s,%s,%s,%s)"
        self.datos=(servicio.getMatricula(),
                    servicio.getFechaEntrada(),
                    servicio.getHoraEntrada(),
                    servicio.getFechaSalida(),
                    servicio.getHoraSalida(),
                    servicio.getFolioPrecio(),
                    servicio.getTipoServicio())
        self.cursor1.execute(self.sql,self.datos)
        self.conn.commit()
        self.conn.close()
      except:
        print("Error")
    
    def getMaxId(self):
        id=1
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "select max(folio_servicio) as id from servicios"
        self.cursor1.execute(self.sql)
        row=self.cursor1.fetchone()
        self.conn.commit()
        self.conn.close()
        return row[0]
        
class dbCobros:
    def save(self, cobro):
      try:
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="insert into cobros(folio_servicio,matricula,hora_estancia,usuario_id) values(%s,%s,%s,%s)"
        self.datos=(cobro.getFolioServicio(),
                    cobro.getMatricula(),
                    cobro.getHoraEstancia(),
                    cobro.getUsuario_id())
        self.cursor1.execute(self.sql,self.datos)
        self.conn.commit()
        self.conn.close()
      except:
        print("Error Cobros")
    
    def getMaxId(self):
        id=1
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1 = self.conn.cursor()
        self.sql = "select max(folio_cobro) as id from cobros"
        self.cursor1.execute(self.sql)
        row=self.cursor1.fetchone()
        self.conn.commit()
        self.conn.close()
        return row[0]
    