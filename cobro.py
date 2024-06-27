class cobro:
    def __init__(self):
        self.FolioCobro=0
        self.FolioServicio=0
        self.Matricula=""
        self.HoraEstancia=""
        self.Usuario_id=0
    
    #primero los getter
    def getHoraEstancia(self):
        return self.HoraEstancia
    def getFolioServicio(self):
        return self.FolioServicio
    def getMatricula(self):
        return self.Matricula    
    def getFolioCobro(self):
        return self.FolioCobro
    def getUsuario_id(self):
        return self.Usuario_id
    
    #Ahora los setter
    def setHoraEstancia(self, r):
        self.HoraEstancia = r
    def setFolioServicio(self,idReferencia):
        self.FolioServicio = idReferencia
    def setMatricula(self,MatriculaReferencia):
        self.Matricula = MatriculaReferencia
    def setFolioCobro(self,PassRef):
        self.FolioCobro=PassRef
    def setUsuario_id(self,Usuario_idRef):
        self.Usuario_id = Usuario_idRef