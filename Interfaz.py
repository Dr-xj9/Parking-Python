from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from datetime import datetime
import csv

#--Paquetes propios
import usuario as user
import dbUsuario
import cliente as c
import dbCliente
import vehiculos as vh
import dbVehiculo
import cobro
import precio
import servicio
import dbClases
import reporte as re

class GUI:
    def __init__(self, root):
        
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var4 = tk.StringVar()
        self.var5 = tk.StringVar()
        self.var6 = tk.StringVar()
        self.var7 = tk.StringVar()
        self.var8 = tk.StringVar()
        self.var9 = tk.StringVar()
        self.root = root
        self.root.title("Login")
        
        #Labels que aparecen antes de la entrada
        tk.Label(root, text="UserName").grid(row=0, column=0, padx=25, pady=20)
        tk.Label(root, text="Password").grid(row=1, column=0, padx=25, pady=20)
        
        #Entrada del usuario se almacenan aqui
        self.entrada_usuario = tk.Entry(root)
        self.entrada_password = tk.Entry(root, show='*')
        
        self.boton_acceder = tk.Button(root, text="Login", command=self.logear)
        self.boton_acceder.grid(row=2, column=0, columnspan=2, pady=20)
        
        self.entrada_usuario.grid(row=0, column=1, padx=25, pady=8)
        self.entrada_password.grid(row=1, column=1, padx=25, pady=8)
        
        
    def logear(self):
        username = self.entrada_usuario.get()
        password = self.entrada_password.get()
        
        usuario = user.usuario()
        usuario.setUserName(username)
        usuario.setPassword(password)
        
        conexionDB = dbUsuario.dbUsuario()
        datos = conexionDB.Autentificar(usuario)
        if(datos is None):
            messagebox.showinfo("Error", "Verifique que los datos sean correctos")
        else:
            self.idUsuarioG = datos.getUsuario_id()
            perfil = datos.getPerfil() #-------- Perfil a verificar 
            self.root.withdraw()
            if(perfil == "administrador"):
                self.menuAdmin()
            if(perfil == "cobrador"):
                self.menuCobrador()
            
    def menuCobrador(self):
        self.nueva_ventana = tk.Toplevel(self.root, width=500)
        self.nueva_ventana.title("Cobrador")
        
        self.opcion_seleccionada = tk.StringVar()

        # Crear y configurar el menú desplegable
        opciones = ["Registrar Cliente", "Servicio", "Reporte", "Salir"]
        tk.OptionMenu(self.nueva_ventana, self.opcion_seleccionada, *opciones).grid(column=0, row=0)

        # Crear un contenedor para el contenido central
        self.centro_frame = tk.Frame(self.nueva_ventana, bg="lightgray", width=500, height=300)
        self.centro_frame.grid(column=1, row = 1)
        
        # Configurar un rastreador de cambios en el menú desplegable
        self.opcion_seleccionada.trace_add("write", self.actualizar)
        
    def menuAdmin(self):
        self.nueva_ventana = tk.Toplevel(self.root, width=500)
        self.nueva_ventana.title("Administrador")
        
        self.opcion_seleccionada = tk.StringVar()

        # Crear y configurar el menú desplegable
        opciones = ["Usuarios", "Clientes", "Vehiculos","Servicios","Salir"]
        tk.OptionMenu(self.nueva_ventana, self.opcion_seleccionada, *opciones).grid(column=0, row=0)

        # Crear un contenedor para el contenido central
        self.centro_frame = tk.Frame(self.nueva_ventana, bg="lightgray", width=500, height=300)
        self.centro_frame.grid(column=1, row = 1)
        
        # Configurar un rastreador de cambios en el menú desplegable
        self.opcion_seleccionada.trace_add("write", self.actualizar)
        
    def actualizar(self, *args):
        opcion = self.opcion_seleccionada.get()
        self.mostrar_contenido(opcion)
        
    def mostrar_contenido(self, opcion):
        # Limpiar el contenido central actual
        for widget in self.centro_frame.winfo_children():
            widget.destroy()
            
        # Mostrar el nuevo contenido según la opción seleccionada
        if opcion == "Usuarios":
            self.menuUsuarios()
        elif opcion == "Salir":
            self.root.destroy()
        elif opcion == "Clientes":
            self.menuClientes()
        elif opcion == "Vehiculos":
            self.menuVehiculo()
        elif opcion == "Servicios":
            self.menuServicios()
            
        #---Opciones del cobrador ---
        elif opcion == "Registrar Cliente":
            self.menuDatosCliente()    
        elif opcion == "Servicio":
            self.cobro()
        elif opcion == "Reporte":
            self.reporte()
    

    #--------MÉTODOS DEL COBRADOR --------------------------
    def menuDatosCliente(self):
    
        tk.Label(self.centro_frame, text="Nombre").grid(row=0, column=0, padx=6, pady=8)
        self.entradaNombre = tk.Entry(self.centro_frame, textvariable=self.var1)
        self.entradaNombre.grid(row=0, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Telefono").grid(row=2, column=0, padx=5, pady=8)
        self.entradaTelefono= tk.Entry(self.centro_frame, textvariable=self.var2)
        self.entradaTelefono.grid(row=2, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="E-Mail").grid(row=3, column=0, padx=5, pady=8)
        self.entradaEmail= tk.Entry(self.centro_frame, textvariable=self.var3)
        self.entradaEmail.grid(row=3, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="RFC").grid(row=4, column=0, padx=5, pady=8)
        self.entradaRFC= tk.Entry(self.centro_frame, textvariable=self.var4)
        self.entradaRFC.grid(row=4, column=1, padx=5, pady=8)
        #Botones
        self.boton_nuevo = tk.Button(self.centro_frame, text="Nuevo", command=self.nuevoCliente_C)
        self.boton_nuevo.grid(row=5, column=0, padx=5, pady=8)
        self.boton_siguiente = tk.Button(self.centro_frame, text="Siguiente", command=self.siguiente)
        self.boton_siguiente.grid(row=5, column=2, padx=5, pady=8)
        
    def nuevoCliente_C(self):
        self.var1.set("")
        self.var2.set("")
        self.var3.set("")
        self.var4.set("")
        
    def siguiente(self):
        self.objCliente_C = c.cliente()
        self.objCliente_C.setNombre(self.entradaNombre.get())
        self.objCliente_C.setTelefono(self.entradaTelefono.get())
        self.objCliente_C.setEmail(self.entradaEmail.get())
        self.objCliente_C.setRFC(self.entradaRFC.get())
        self.objCliente_C.setUsuario_id(self.idUsuarioG)
        
        for widget in self.centro_frame.winfo_children():
           widget.destroy()
        self.menuDatosVehiculo()
    
    def menuDatosVehiculo(self):
        tk.Label(self.centro_frame, text="Matricula").grid(row=0, column=0, padx=5, pady=8)
        self.entradaMatricula = tk.Entry(self.centro_frame, textvariable=self.var5)
        self.entradaMatricula.grid(row=0, column=1, padx=5, pady=8)
                
        tk.Label(self.centro_frame, text="Modelo").grid(row=2, column=0, padx=6, pady=8)
        self.entradaModelo= tk.Entry(self.centro_frame, textvariable=self.var6)
        self.entradaModelo.grid(row=2, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Marca").grid(row=3, column=0, padx=5, pady=8)
        self.entradaMarca= tk.Entry(self.centro_frame, textvariable=self.var7)
        self.entradaMarca.grid(row=3, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Color").grid(row=4, column=0, padx=5, pady=8)
        self.entradaColor= tk.Entry(self.centro_frame, textvariable=self.var8)
        self.entradaColor.grid(row=4, column=1, padx=5, pady=8)
        
        self.boton_nuevo = tk.Button(self.centro_frame, text="Nuevo", command=self.nuevoVe_C)
        self.boton_nuevo.grid(row=6, column=1, padx=5, pady=10)
        self.boton_guardar = tk.Button(self.centro_frame, text="Guardar", command=self.guardarCliente_C)
        self.boton_guardar.grid(row=6, column=2,padx=5, pady=10)
    
    def nuevoVe_C(self):
        self.var5.set("")
        self.var6.set("")
        self.var7.set("")
        self.var8.set("")
    
    def guardarCliente_C(self):
        baseCliente = dbCliente.dbCliente()
        baseCliente.save(self.objCliente_C)
        res = baseCliente.searchByName(self.objCliente_C)        
        
        objVeh = vh.vehiculo()
        
        objVeh.setMatricula(self.entradaMatricula.get())
        self.var9.set(self.entradaMatricula.get()) 
        
        objVeh.setModelo(self.entradaModelo.get())
        objVeh.setMarca(self.entradaMarca.get())
        objVeh.setColor(self.entradaColor.get())
        objVeh.setCliente_id(res.getCliente_id())
        baseVehiculo = dbVehiculo.dbVehiculo()
        baseVehiculo.save(objVeh)
        messagebox.showinfo("Correcto","Datos Almacenados con éxito")
            
    def cobro(self):
        tk.Label(self.centro_frame, text="Matricula").grid(row=3, column=1, padx=5, pady=8)
        self.entradaMatricula = tk.Entry(self.centro_frame, textvariable=self.var9)
        self.entradaMatricula.grid(row=3, column=2, padx=2, pady=8)
        self.entradaMatricula.config(state=tk.DISABLED)
        
        tk.Label(self.centro_frame, text="Hora de entrada").grid(row=4, column=0, padx=5, pady=8)
        self.entradaHoraEntrada = tk.Entry(self.centro_frame, textvariable=self.var1)
        self.entradaHoraEntrada.grid(row=4, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Fecha de Entrada").grid(row=4, column=2, padx=5, pady=8)
        self.entradaFechaEntrada = tk.Entry(self.centro_frame, textvariable=self.var2)
        self.entradaFechaEntrada.grid(row=4, column=3, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Hora de salida").grid(row=5, column=0, pady=8, padx=5)
        self.entradaHoraSalida = tk.Entry(self.centro_frame, textvariable=self.var3)
        self.entradaHoraSalida.grid(row=5,column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Fecha de salida").grid(row=5, column=2, pady=8, padx=5)
        self.entradaFechaSalida = tk.Entry(self.centro_frame, textvariable=self.var4)
        self.entradaFechaSalida.grid(row=5,column=3, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Tipo de servicio").grid(row=6, column=1, padx=5, pady=8)
        self.tipo = tk.StringVar()
        self.combo = ttk.Combobox(self.centro_frame, textvariable=self.tipo)
        self.combo['values'] = ("Frecuente", "De paso")
        self.combo.grid(row=6, column = 2, padx=5, pady=5)
        
        self.boton_cobrar = tk.Button(self.centro_frame, text="Cobrar", command=self.cobrar_C)
        self.boton_cobrar.grid(row=7, column=1,columnspan=2, pady=10)
        self.limpiarCobro()
    
    def limpiarCobro(self):
        self.var1.set("")
        self.var2.set("")
        self.var3.set("")
        self.var4.set("")
        self.tipo.set("")
    
    def cobrar_C(self):
        if(self.tipo.get() == "Frecuente"):
            if(self.entradaHoraEntrada.get() == "" or self.entradaHoraSalida.get() == ""):
                messagebox.showinfo("Error","Verifique las entradas de horas")
            else:
                fechaE=self.entradaFechaEntrada.get()
                fechaS=self.entradaFechaSalida.get()
                if(fechaE == "" or fechaS == "" or self.verificar_formato_fecha(fechaE)==False or self.verificar_formato_fecha(fechaS)==False):                    
                    messagebox.showinfo("Error","Verifique las fechas")
                else:
                    horasTotales=self.diferencia_entre_horas()
                    horasTotales=int(horasTotales)
                    difDias = self.diferenciaFechas()
                    cobrar = 0
                    for y in range(difDias):
                        horasTotales=horasTotales+24
                        
                    for x in range(1, horasTotales+1):
                        if(x>=5):
                            cobrar=cobrar+22
                        else:
                            cobrar=cobrar+26
                            
                    objPrecio = precio.precio()
                    objPrecio.setTipo(self.tipo.get())
                    objPrecio.setPrecio(cobrar)
                    base = dbClases.dbPrecio()
                    base.save(objPrecio)
                    aux = base.getMaxId()
                    
                    objServ = servicio.servicio()
                    objServ.setFolioPrecio(aux)
                    objServ.setMatricula(self.entradaMatricula.get())
                    objServ.setHoraEntrada(self.entradaHoraEntrada.get())
                    objServ.setHoraSalida(self.entradaHoraSalida.get())
                    objServ.setFechaEntrada(self.entradaFechaEntrada.get())
                    objServ.setFechaSalida(self.entradaFechaSalida.get())
                    objServ.setTipoServicio(self.tipo.get())
                    baseServicio = dbClases.dbServicio()
                    baseServicio.save(objServ)
                    aux = baseServicio.getMaxId()
                    
                    objCobros = cobro.cobro()
                    objCobros.setFolioServicio(aux)
                    objCobros.setMatricula(self.entradaMatricula.get())
                    objCobros.setHoraEstancia(horasTotales)
                    objCobros.setUsuario_id(self.idUsuarioG)
                    baseCobros = dbClases.dbCobros()
                    baseCobros.save(objCobros)
                    messagebox.showinfo("Cobrar","Precio a pagar: {}$ \nHoras de estancia: {}hrs".format(cobrar, horasTotales))
                    self.limpiarCobro()
                    
        elif(self.tipo.get() == "De paso"):
            if(self.entradaHoraEntrada.get() == "" or self.entradaHoraSalida.get() == ""):
                messagebox.showinfo("Error","Verifique las entradas de horas")
            else:
                fechaE=self.entradaFechaEntrada.get()
                fechaS=self.entradaFechaSalida.get()
                if(fechaE == "" or fechaS == "" or self.verificar_formato_fecha(fechaE)==False or self.verificar_formato_fecha(fechaS)==False):                    
                    messagebox.showinfo("Error","Verifique las fechas")
                else:
                    horasTotales=self.diferencia_entre_horas()
                    horasTotales=int(horasTotales)
                    difDias = self.diferenciaFechas()
                    cobrar = 0
                    for y in range(difDias):
                        horasTotales=horasTotales+24
                    for x in range(1, horasTotales+1):
                        if(x>=5):
                            cobrar=cobrar+25
                        else:
                            cobrar=cobrar+30
                    objPrecio = precio.precio()
                    objPrecio.setTipo(self.tipo.get())
                    objPrecio.setPrecio(cobrar)
                    base = dbClases.dbPrecio()
                    base.save(objPrecio)
                    aux = base.getMaxId()
                    
                    objServ = servicio.servicio()
                    objServ.setFolioPrecio(aux)
                    objServ.setMatricula(self.entradaMatricula.get())
                    objServ.setHoraEntrada(self.entradaHoraEntrada.get())
                    objServ.setHoraSalida(self.entradaHoraSalida.get())
                    objServ.setFechaEntrada(self.entradaFechaEntrada.get())
                    objServ.setFechaSalida(self.entradaFechaSalida.get())
                    objServ.setTipoServicio(self.tipo.get())
                    baseServicio = dbClases.dbServicio()
                    baseServicio.save(objServ)
                    aux = baseServicio.getMaxId()
                    
                    objCobros = cobro.cobro()
                    objCobros.setFolioServicio(aux)
                    objCobros.setMatricula(self.entradaMatricula.get())
                    objCobros.setHoraEstancia(horasTotales)
                    objCobros.setUsuario_id(self.idUsuarioG)
                    baseCobros = dbClases.dbCobros()
                    baseCobros.save(objCobros)
                    messagebox.showinfo("Cobrar","Precio a pagar: {}$ \nHoras de estancia: {}hrs".format(cobrar, horasTotales))
                    self.limpiarCobro()
        else:
            messagebox.showinfo("Error","Verifique el tipo de servicio")
    
    def verificar_formato_fecha(self,fecha):
        formato_esperado = "%Y/%m/%d"
        try:
            datetime.strptime(fecha, formato_esperado)
            return True
        except ValueError:
            return False
    
    def diferenciaFechas(self):
        formato = "%Y/%m/%d"
        fecha1_obj = datetime.strptime(self.entradaFechaEntrada.get(), formato)
        fecha2_obj = datetime.strptime(self.entradaFechaSalida.get(), formato)
        diferencia = fecha2_obj - fecha1_obj
        return abs(diferencia.days)
    
    def diferencia_entre_horas(self):
        formato = "%H:%M:%S"
        hora1_obj = datetime.strptime(self.entradaHoraEntrada.get(), formato)
        hora2_obj = datetime.strptime(self.entradaHoraSalida.get(), formato)
        diferencia = hora2_obj - hora1_obj
        return abs(diferencia.total_seconds() / 3600)  # Convertir la diferencia en horas

    def reporte(self):
        tk.Label(self.centro_frame, text="Reportes").grid(row=0, column=1, columnspan=2,padx=35, pady=5)
        
        tk.Label(self.centro_frame, text="Nombre del reporte").grid(row=1, column=1,columnspan=2 ,padx=30, pady=10)
        self.entradaReporte = tk.Entry(self.centro_frame, textvariable=self.var1)
        self.entradaReporte.grid(row=2, column=1, columnspan=2, padx=30, pady=20)
        
        boton = tk.Button(self.centro_frame, text="Entradas/Salidas-Vehiculos", width=30, height=1, anchor="center", command=self.entradasPorMes)
        boton.grid(row=3, column=1, padx=30, pady=5)
        boton2 = tk.Button(self.centro_frame, text="Servicios por Semana", width=30, height=1, anchor="center", command=self.servSemana)
        boton2.grid(row=4, column=1, padx=30, pady=10)
    
    def servSemana(self):
        base = dbClases.dbReporte()
        res = base.crearSemana()
        with open(self.entradaReporte.get(), 'w', newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)    
            escritor.writerow(['Año', 'Semana', 'Servicios'])
            for reporte in res:
                escritor.writerow([reporte.get_anio(), reporte.get_semana(), reporte.get_servicio()])
        print(f"Los datos se han guardado en el archivo '{self.entradaReporte.get()}'.")
        self.var1.set("")
        
    def entradasPorMes(self):
        base = dbClases.dbReporte()
        res = base.crear()
        with open(self.entradaReporte.get(), 'w', newline='') as archivo_csv:
            escritor = csv.writer(archivo_csv)    
            escritor.writerow(['Año', 'Mes', 'Entradas', 'Salidas'])
            for reporte in res:
                escritor.writerow([reporte.get_anio(), reporte.get_mes(), reporte.get_entradas(), reporte.get_salidas()])
        print(f"Los datos se han guardado en el archivo '{self.entradaReporte.get()}'.")
        self.var1.set("")
    
    # <------ MÉTODOS DEL ADMINISTRADOR -------------------------> #    
    def menuVehiculo(self):
        self.limpiar()
        tk.Label(self.centro_frame, text="Matricula").grid(row=0, column=0, padx=5)
        
        self.entradaMatricula = tk.Entry(self.centro_frame, textvariable=self.var1)
        self.entradaMatricula.grid(row=0, column=1, padx=5)
        
        self.buscar = tk.Button(self.centro_frame,text="Buscar", command=self.buscarVe_A)
        self.buscar.grid(row=0, column=2, padx=5)
                
        tk.Label(self.centro_frame, text="Modelo").grid(row=2, column=0, padx=6, pady=8)
        self.entradaModelo= tk.Entry(self.centro_frame, textvariable=self.var2)
        self.entradaModelo.grid(row=2, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Marca").grid(row=3, column=0, padx=5, pady=8)
        self.entradaMarca= tk.Entry(self.centro_frame, textvariable=self.var3)
        self.entradaMarca.grid(row=3, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Color").grid(row=4, column=0, padx=5, pady=8)
        self.entradaColor= tk.Entry(self.centro_frame, textvariable=self.var4)
        self.entradaColor.grid(row=4, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Cliente-ID").grid(row=5, column=0, padx=5, pady=8)
        self.entradaClienteID= tk.Entry(self.centro_frame, textvariable=self.var5)
        self.entradaClienteID.grid(row=5, column=1, padx=5, pady=8)
        
        #Botones
        self.boton_guardar = tk.Button(self.centro_frame, text="Guardar", command=self.guardarVe_A)
        self.boton_guardar.grid(row=6, column=1, padx=5, pady=8)
        self.boton_nuevo = tk.Button(self.centro_frame, text="Nuevo", command=self.nuevoVe_A)
        self.boton_nuevo.grid(row=6, column=0, padx=5, pady=8)
        self.boton_eliminar = tk.Button(self.centro_frame, text="Borrar", command=self.borrarVe_A)
        self.boton_eliminar.grid(row=6, column=2, padx=5, pady=8)
        self.boton_editar = tk.Button(self.centro_frame, text="Editar", command=self.editarVe_A)
        self.boton_editar.grid(row=6, column=6, padx=5, pady=8)
        self.boton_cancelar = tk.Button(self.centro_frame, text="Cancelar", command=self.cancelarVe_A)
        self.boton_cancelar.grid(row=6, column=4, padx=5, pady=8)
        
        self.entradaModelo.config(state=tk.DISABLED)
        self.entradaMarca.config(state=tk.DISABLED)
        self.entradaColor.config(state=tk.DISABLED)
        self.entradaClienteID.config(state=tk.DISABLED)
        self.boton_guardar.config(state="disabled")
        self.buscar.config(state="normal")
        self.boton_editar.config(state="disabled")
        self.boton_eliminar.config(state="disabled")
        self.boton_nuevo.config(state="normal")
        
    def nuevoVe_A(self):
        self.entradaMatricula.config(state=tk.NORMAL)
        self.entradaModelo.config(state=tk.NORMAL)
        self.entradaMarca.config(state=tk.NORMAL)
        self.entradaColor.config(state=tk.NORMAL)
        self.entradaClienteID.config(state=tk.NORMAL)
        
        self.boton_guardar.config(state="normal")
        self.buscar.config(state="disabled")
        self.boton_editar.config(state="disabled")
        self.boton_eliminar.config(state="disabled")
        self.limpiar()
    
    def guardarVe_A(self):
        objVeh = vh.vehiculo()
        objVeh.setMatricula(self.entradaMatricula.get())
        objVeh.setModelo(self.entradaModelo.get())
        objVeh.setMarca(self.entradaMarca.get())
        objVeh.setColor(self.entradaColor.get())
        objVeh.setCliente_id(self.entradaClienteID.get())
        base = dbVehiculo.dbVehiculo()
        estado_btEditar=self.boton_editar.cget("state")
        if(estado_btEditar == "disabled"):
            base.save(objVeh)
            messagebox.showinfo("Correcto", "Vehiculo Registrado")
        else:
            base.edit(objVeh)
            messagebox.showinfo("Correcto", "Datos Editados")
            
        self.cancelarVe_A()
            
    def borrarVe_A(self):
        objVeh = vh.vehiculo()
        objVeh.setMatricula(self.entradaMatricula.get())
        base = dbVehiculo.dbVehiculo()
        base.remove(objVeh)
        messagebox.showinfo("Correcto","Vehiculo Eliminado")
        
    def buscarVe_A(self):
        self.boton_nuevo.config(state="normal")
        self.boton_guardar.config(state="disabled")
        self.boton_editar.config(state="normal")
        self.boton_eliminar.config(state="normal")
        self.entradaMatricula.config(state=tk.DISABLED)
        self.entradaModelo.config(state=tk.DISABLED)
        self.entradaMarca.config(state=tk.DISABLED)
        self.entradaColor.config(state=tk.DISABLED)
        self.entradaClienteID.config(state=tk.DISABLED)
        
        objVeh = vh.vehiculo()
        objVeh.setMatricula(self.entradaMatricula.get())
        base = dbVehiculo.dbVehiculo()
        res = base.search(objVeh)
        if res is not None:
            self.var1.set(res.getMatricula())
            self.var2.set(res.getModelo())
            self.var3.set(res.getMarca())
            self.var4.set(res.getColor())
            self.var5.set(res.getCliente_id())
        else:
            messagebox.showinfo("Error","Vehiculo No Encontrado")        
    
    def editarVe_A(self):
        self.entradaMatricula.config(state=tk.NORMAL)
        self.entradaModelo.config(state=tk.NORMAL)
        self.entradaMarca.config(state=tk.NORMAL)
        self.entradaColor.config(state=tk.NORMAL)
        self.entradaClienteID.config(state=tk.NORMAL)
        self.boton_guardar.config(state="normal")
    
    def cancelarVe_A(self):
        self.entradaMatricula.config(state=tk.NORMAL)
        self.entradaModelo.config(state=tk.DISABLED)
        self.entradaMarca.config(state=tk.DISABLED)
        self.entradaColor.config(state=tk.DISABLED)
        self.entradaClienteID.config(state=tk.DISABLED)
        self.boton_nuevo.config(state="normal")
        self.buscar.config(state="normal")
        self.boton_guardar.config(state="disabled")
        self.boton_editar.config(state="disabled")
        self.boton_eliminar.config(state="disabled")
        self.limpiar()
        
    def menuClientes(self):
        self.limpiar()
        tk.Label(self.centro_frame, text="Cliente ID").grid(row=0, column=0, padx=5)
        
        self.entradaBusqueda = tk.Entry(self.centro_frame, textvariable=self.var5)
        self.entradaBusqueda.grid(row=0, column=1, padx=5)
        
        self.boton_buscar_cliente = tk.Button(self.centro_frame,text="Buscar", command=self.buscarCliente_A)
        self.boton_buscar_cliente.grid(row=0, column=2, padx=5)
        
        tk.Label(self.centro_frame, text="Nombre").grid(row=2, column=0, padx=6, pady=8)
        self.entradaNombre = tk.Entry(self.centro_frame, textvariable=self.var1)
        self.entradaNombre.grid(row=2, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Telefono").grid(row=3, column=0, padx=5, pady=8)
        self.entradaTelefono= tk.Entry(self.centro_frame, textvariable=self.var2)
        self.entradaTelefono.grid(row=3, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="E-Mail").grid(row=4, column=0, padx=5, pady=8)
        self.entradaEmail= tk.Entry(self.centro_frame, textvariable=self.var3)
        self.entradaEmail.grid(row=4, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="RFC").grid(row=5, column=0, padx=5, pady=8)
        self.entradaRFC = tk.Entry(self.centro_frame, textvariable=self.var4)
        self.entradaRFC.grid(row=5, column=1, padx=5, pady=8)
        
        #Botones
        self.boton_guardar = tk.Button(self.centro_frame, text="Guardar", command=self.guardarCliente_A)
        self.boton_guardar.grid(row=6, column=1, padx=5, pady=8)
        self.boton_nuevo = tk.Button(self.centro_frame, text="Nuevo", command=self.nuevoCliente_A)
        self.boton_nuevo.grid(row=6, column=0, padx=5, pady=8)
        self.boton_eliminar = tk.Button(self.centro_frame, text="Borrar", command=self.borrarCliente_A)
        self.boton_eliminar.grid(row=6, column=2, padx=5, pady=8)
        self.boton_editar = tk.Button(self.centro_frame, text="Editar", command=self.editarCliente_A)
        self.boton_editar.grid(row=6, column=6, padx=5, pady=8)
        self.boton_cancelar = tk.Button(self.centro_frame, text="Cancelar", command=self.cancelarCliente_A)
        self.boton_cancelar.grid(row=6, column=4, padx=5, pady=8)
        
        self.entradaNombre.config(state=tk.DISABLED)
        self.entradaEmail.config(state=tk.DISABLED)
        self.entradaTelefono.config(state=tk.DISABLED)
        self.entradaRFC.config(state=tk.DISABLED)
        self.boton_nuevo.config(state="normal")
        self.boton_buscar_cliente.config(state="normal")
        self.boton_editar.config(state="disabled")
        self.boton_eliminar.config(state="disabled")
        self.boton_guardar.config(state="disabled")
        
    def nuevoCliente_A(self):
        self.entradaNombre.config(state=tk.NORMAL)
        self.entradaTelefono.config(state=tk.NORMAL)
        self.entradaEmail.config(state=tk.NORMAL)
        self.entradaRFC.config(state=tk.NORMAL)
        self.entradaBusqueda.config(state=tk.DISABLED)
        
        self.boton_guardar.config(state="normal")
        self.boton_buscar_cliente.config(state="disabled")
        self.boton_editar.config(state="disabled")
        self.boton_eliminar.config(state="disabled")
        self.limpiar()
    
    def buscarCliente_A(self):
        objCliente = c.cliente()
        objCliente.setCliente_id(self.entradaBusqueda.get())
        base = dbCliente.dbCliente()
        res = base.search(objCliente)
        if res is not None:
            self.var1.set(res.getNombre())
            self.var2.set(res.getTelefono())
            self.var3.set(res.getEmail())
            self.var4.set(res.getRFC())
            
            self.entradaNombre.config(state=tk.DISABLED)
            self.entradaEmail.config(state=tk.DISABLED)
            self.entradaTelefono.config(state=tk.DISABLED)
            self.entradaRFC.config(state=tk.DISABLED)
            self.boton_nuevo.config(state="normal")
            self.boton_editar.config(state="normal")
            self.boton_eliminar.config(state="normal")
            self.boton_guardar.config(state="disabled")
        else:
            messagebox.showinfo("Error", "Cliente no encontrado :c")
    
    def editarCliente_A(self):
        self.entradaNombre.config(state=tk.NORMAL)
        self.entradaTelefono.config(state=tk.NORMAL)
        self.entradaEmail.config(state=tk.NORMAL)
        self.entradaRFC.config(state=tk.NORMAL)
        self.boton_nuevo.config(state="disabled")
        self.boton_eliminar.config(state="disabled")
        self.boton_guardar.config(state="normal")
    
    def guardarCliente_A(self):
        objCliente = c.cliente()
        objCliente.setCliente_id(self.entradaBusqueda.get())
        objCliente.setNombre(self.entradaNombre.get())
        objCliente.setTelefono(self.entradaTelefono.get())
        objCliente.setEmail(self.entradaEmail.get())
        objCliente.setRFC(self.entradaRFC.get())
        objCliente.setUsuario_id(self.idUsuarioG)
        base = dbCliente.dbCliente()
        estado_btEditar=self.boton_editar.cget("state")
        if(estado_btEditar == "disabled"):
            base.save(objCliente)
            messagebox.showinfo("Exito","Cliente registrado")
        else:
            base.edit(objCliente)
            messagebox.showinfo("Exito","Datos editados")
        self.cancelarCliente_A()
        
    def borrarCliente_A(self):
        objCliente = c.cliente()
        objCliente.setCliente_id(self.entradaBusqueda.get())
        base = dbCliente.dbCliente()
        base.remove(objCliente)
        messagebox.showinfo("Exito","Eliminado con exito")
        self.limpiar()
        
    def cancelarCliente_A(self):
        self.entradaNombre.config(state=tk.DISABLED)
        self.entradaEmail.config(state=tk.DISABLED)
        self.entradaTelefono.config(state=tk.DISABLED)
        self.entradaRFC.config(state=tk.DISABLED)
        self.entradaBusqueda.config(state=tk.NORMAL)
        self.boton_guardar.config(state="disabled")
        self.boton_editar.config(state="disabled")
        self.boton_eliminar.config(state="disabled")
        self.boton_buscar_cliente.config(state="normal")
        self.boton_nuevo.config(state="normal")
        self.limpiar()
     
    def menuUsuarios(self):
        self.limpiar()
        tk.Label(self.centro_frame, text="Usuario ID").grid(row=0, column=0, padx=5)
        
        self.entradaBusqueda = tk.Entry(self.centro_frame)
        self.entradaBusqueda.grid(row=0, column=1, padx=5)
        
        self.boton_buscar = tk.Button(self.centro_frame,text="Buscar", command=self.buscar_A)
        self.boton_buscar.grid(row=0, column=2, padx=5)
                
        tk.Label(self.centro_frame, text="Nombre").grid(row=2, column=0, padx=6, pady=8)
        self.entradaNombre = tk.Entry(self.centro_frame, textvariable=self.var1)
        self.entradaNombre.grid(row=2, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Email").grid(row=3, column=0, padx=5, pady=8)
        self.entradaEmail= tk.Entry(self.centro_frame, textvariable=self.var2)
        self.entradaEmail.grid(row=3, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Username").grid(row=4, column=0, padx=5, pady=8)
        self.entradaUsername= tk.Entry(self.centro_frame, textvariable=self.var3)
        self.entradaUsername.grid(row=4, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Password").grid(row=5, column=0, padx=5, pady=8)
        self.entradaPassword= tk.Entry(self.centro_frame, textvariable=self.var4)
        self.entradaPassword.grid(row=5, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Perfil").grid(row=6, column=0, padx=5, pady=8)
        self.perfil = tk.StringVar()
        self.combo = ttk.Combobox(self.centro_frame, textvariable=self.perfil)
        self.combo['values'] = ("administrador", "cobrador")
        self.combo.grid(row=6, column = 1, padx=5, pady=5)
        
        #Botones
        self.boton_nuevo = tk.Button(self.centro_frame, text="Nuevo", command=self.nuevo_A)
        self.boton_nuevo.grid(row=7, column=0, padx=5, pady=8)
        
        self.boton_guardar = tk.Button(self.centro_frame, text="Guardar", command=self.guardar_A)
        self.boton_guardar.grid(row=7, column=1, padx=5, pady=8)
        
        self.boton_eliminar = tk.Button(self.centro_frame, text="Borrar", command=self.borrar_A)
        self.boton_eliminar.grid(row=7, column=2, padx=5, pady=8)
        
        self.boton_editar = tk.Button(self.centro_frame, text="Editar", command=self.editar_A)
        self.boton_editar.grid(row=7, column=6, padx=5, pady=8)
        
        self.boton_cancelar = tk.Button(self.centro_frame, text="Cancelar", command=self.cancelar_A)
        self.boton_cancelar.grid(row=7, column=4, padx=5, pady=8)
        
        self.entradaNombre.config(state=tk.DISABLED)
        self.entradaEmail.config(state=tk.DISABLED)
        self.entradaUsername.config(state=tk.DISABLED)
        self.entradaPassword.config(state=tk.DISABLED)
        self.combo.config(state=tk.DISABLED)
        self.boton_guardar.config(state="disabled")
        self.boton_editar.config(state="disabled")
        self.boton_eliminar.config(state="disabled")
    
    def cancelar_A(self):
        self.entradaNombre.config(state=tk.DISABLED)
        self.entradaEmail.config(state=tk.DISABLED)
        self.entradaUsername.config(state=tk.DISABLED)
        self.entradaPassword.config(state=tk.DISABLED)
        self.combo.config(state=tk.DISABLED)
        self.entradaBusqueda.config(state=tk.NORMAL)
        self.boton_guardar.config(state="disabled")
        self.boton_editar.config(state="disabled")
        self.boton_buscar.config(state="normal")
        self.boton_nuevo.config(state="normal")
        self.limpiar()
        self.perfil.set("")
        
    def nuevo_A(self):
        self.boton_eliminar.config(state="disabled")
        self.entradaNombre.config(state=tk.NORMAL)
        self.entradaEmail.config(state=tk.NORMAL)
        self.entradaUsername.config(state=tk.NORMAL)
        self.entradaPassword.config(state=tk.NORMAL)
        self.combo.config(state=tk.NORMAL)
        self.entradaBusqueda.config(state=tk.DISABLED)
        self.boton_guardar.config(state="normal")
        self.boton_buscar.config(state="disabled")
        self.boton_editar.config(state="disabled")
        self.perfil.set("")
        self.limpiar()
        
    def limpiar(self):
        self.var1.set("")
        self.var2.set("")
        self.var3.set("")
        self.var4.set("")
        self.var5.set("")
        self.var6.set("")
        
    def guardar_A(self):
        objUsuario = user.usuario()
        objUsuario.setUsuario_id(self.entradaBusqueda.get())
        objUsuario.setNombre(self.entradaNombre.get())
        objUsuario.setEmail(self.entradaEmail.get())
        objUsuario.setUserName(self.entradaUsername.get())
        objUsuario.setPassword(self.entradaPassword.get())
        objUsuario.setPerfil(self.perfil.get())
        
        base = dbUsuario.dbUsuario()
        estado_btEditar=self.boton_editar.cget("state")
        if(estado_btEditar == "disabled"):
            if(base.save(objUsuario)):
                messagebox.showinfo("Exito", "Usuario Registrado")
            else:
                messagebox.showinfo("Error", "Ocurrió un error")
        else:
            base.edit(objUsuario)
            messagebox.showinfo("Exito", "Datos Editados")
        
        self.entradaNombre.config(state=tk.DISABLED)
        self.entradaEmail.config(state=tk.DISABLED)
        self.entradaUsername.config(state=tk.DISABLED)
        self.entradaPassword.config(state=tk.DISABLED)
        self.combo.config(state=tk.DISABLED)
        
        self.entradaBusqueda.config(state=tk.NORMAL)
        self.boton_guardar.config(state="disabled")
        self.boton_editar.config(state="disabled")
        self.boton_buscar.config(state="normal")
        self.boton_nuevo.config(state="normal")
        self.boton_eliminar.config(state="disabled")
        self.limpiar()
        self.perfil.set("")
    
    def borrar_A(self):
        objUsuario = user.usuario()
        objUsuario.setUsuario_id(self.entradaBusqueda.get())
        base = dbUsuario.dbUsuario()
        base.remove(objUsuario)
        messagebox.showinfo("Exito","Usuario Eliminado con exito")
        self.entradaNombre.config(state=tk.DISABLED)
        self.entradaEmail.config(state=tk.DISABLED)
        self.entradaUsername.config(state=tk.DISABLED)
        self.entradaPassword.config(state=tk.DISABLED)
        self.combo.config(state=tk.DISABLED)
        
        self.entradaBusqueda.config(state=tk.NORMAL)
        self.boton_guardar.config(state="disabled")
        self.boton_editar.config(state="disabled")
        self.boton_buscar.config(state="normal")
        self.boton_nuevo.config(state="normal")
        self.boton_eliminar.config(state="disabled")
        self.limpiar()
        self.perfil.set("")
    
    def editar_A(self):
        self.entradaNombre.config(state=tk.NORMAL)
        self.entradaEmail.config(state=tk.NORMAL)
        self.entradaUsername.config(state=tk.NORMAL)
        self.entradaPassword.config(state=tk.NORMAL)
        self.combo.config(state=tk.NORMAL)
        self.entradaBusqueda.config(state=tk.DISABLED)
        self.boton_guardar.config(state="normal")
        self.boton_eliminar.config(state="disabled")
    
    def buscar_A(self):
        self.boton_nuevo.config(state="disabled")
        self.boton_guardar.config(state="disabled")
        self.boton_editar.config(state="normal")
        self.boton_eliminar.config(state="normal")
        
        objUsuario = user.usuario()
        objUsuario.setUsuario_id(self.entradaBusqueda.get())
        base = dbUsuario.dbUsuario()
        resultado = base.search(objUsuario)
        
        if(resultado is not None):
            self.var1.set(resultado.getNombre())
            self.var2.set(resultado.getEmail())
            self.var3.set(resultado.getUserName())
            self.var4.set(resultado.getPassword())
            self.perfil.set(resultado.getPerfil())
        else:
            messagebox.showinfo("Error","Usuario no encontrado")
    
    def menuServicios(self):
        self.limpiar()
        tk.Label(self.centro_frame, text="Folio Servicio:").grid(row=0, column=0, padx=5)
        
        self.entradaBusqueda = tk.Entry(self.centro_frame)
        self.entradaBusqueda.grid(row=0, column=1, padx=5)
        
        self.boton_buscar = tk.Button(self.centro_frame,text="Buscar", command=self.buscarServicio)
        self.boton_buscar.grid(row=0, column=2, padx=5)
                
        tk.Label(self.centro_frame, text="Matricula").grid(row=2, column=0, padx=6, pady=8)
        self.entradaMatricula = tk.Entry(self.centro_frame, textvariable=self.var1)
        self.entradaMatricula.grid(row=2, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Fecha Entrada").grid(row=3, column=0, padx=5, pady=8)
        self.entradaFechaEntrada= tk.Entry(self.centro_frame, textvariable=self.var2)
        self.entradaFechaEntrada.grid(row=3, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Hora Entrada").grid(row=4, column=0, padx=5, pady=8)
        self.entradaHoraEntrada= tk.Entry(self.centro_frame, textvariable=self.var3)
        self.entradaHoraEntrada.grid(row=4, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Fecha Salida").grid(row=5, column=0, padx=5, pady=8)
        self.entradaFechaSalida= tk.Entry(self.centro_frame, textvariable=self.var4)
        self.entradaFechaSalida.grid(row=5, column=1, padx=5, pady=8)
        
        tk.Label(self.centro_frame, text="Hora Salida").grid(row=6, column=0, padx=5, pady=8)
        self.entradaHoraSalida= tk.Entry(self.centro_frame, textvariable=self.var5)
        self.entradaHoraSalida.grid(row=6, column=1, padx=5, pady=8)
        
        #Botones
        self.boton_guardar = tk.Button(self.centro_frame, text="Guardar")
        self.boton_guardar.grid(row=7, column=1, padx=5, pady=8)
        
        self.boton_editar = tk.Button(self.centro_frame, text="Editar")
        self.boton_editar.grid(row=7, column=6, padx=5, pady=8)
        
        self.boton_cancelar = tk.Button(self.centro_frame, text="Cancelar", command=self.limpiar)
        self.boton_cancelar.grid(row=7, column=4, padx=5, pady=8)
        
        self.entradaMatricula.config(state=tk.DISABLED)
        self.entradaFechaEntrada.config(state=tk.DISABLED)
        self.entradaHoraEntrada.config(state=tk.DISABLED)
        self.entradaFechaSalida.config(state=tk.DISABLED)
        self.entradaHoraSalida.config(state=tk.DISABLED)
        
        
    def buscarServicio(self):
        base = dbClases.dbServicio()
        
        objServ = servicio.servicio()
        objServ.setFolioServicio(self.entradaBusqueda.get())
        
        res = base.search(objServ)
        
        if res is None:
            messagebox.showinfo("Error","Servicio Inexistente")
        else:
            self.var1.set(res.getMatricula())
            self.var2.set(res.getFechaEntrada())
            self.var3.set(res.getHoraEntrada())
            self.var4.set(res.getFechaSalida())
            self.var5.set(res.getHoraSalida())
          
if (__name__== "__main__"):
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()