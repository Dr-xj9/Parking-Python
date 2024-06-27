class servicio:
    def __init__(self):
        self.FolioServicio=0
        self.Matricula=""
        self.FechaEntrada=""
        self.FechaSalida=""
        self.FolioPrecio=0
        self.TipoServicio=""
        self.HoraEntrada=""
        self.HoraSalida=""
    
    #primero los getter
    def getHoraEntrada(self):
        return self.HoraEntrada
    def getHoraSalida(self):
        return self.HoraSalida
    def getFolioServicio(self):
        return self.FolioServicio
    def getMatricula(self):
        return self.Matricula
    def getFechaEntrada(self):
        return self.FechaEntrada
    def getFechaSalida(self):
        return self.FechaSalida     
    def getFolioPrecio(self):
        return self.FolioPrecio
    def getTipoServicio(self):
        return self.TipoServicio
    
    #Ahora los setter
    def setHoraEntrada(self, r):
        self.HoraEntrada = r
    def setHoraSalida(self, r):
        self.HoraSalida = r
    def setFolioServicio(self,idReferencia):
        self.FolioServicio = idReferencia
    def setMatricula(self,MatriculaReferencia):
        self.Matricula = MatriculaReferencia
    def setFechaEntrada(self,UserRef):
        self.FechaEntrada = UserRef
    def setFechaSalida(self, FechaSalidaRef):
        self.FechaSalida = FechaSalidaRef    
    def setFolioPrecio(self,PassRef):
        self.FolioPrecio=PassRef
    def setTipoServicio(self,TipoServicioRef):
        self.TipoServicio = TipoServicioRef