class vehiculo:
    def __init__(self):
        self.Matricula=""
        self.Modelo=""
        self.Marca=""
        self.Color=""
        self.Cliente_id=0
    
    #primero los getter
    def getMatricula(self):
        return self.Matricula
    def getModelo(self):
        return self.Modelo
    def getMarca(self):
        return self.Marca
    def getEmail(self):
        return self.Email     
    def getColor(self):
        return self.Color
    def getCliente_id(self):
        return self.Cliente_id
    
    #Ahora los setter
    def setMatricula(self,m):
        self.Matricula = m
    def setModelo(self,ModeloReferencia):
        self.Modelo = ModeloReferencia
    def setMarca(self,UserRef):
        self.Marca = UserRef 
    def setColor(self,PassRef):
        self.Color=PassRef
    def setCliente_id(self,Cliente_idRef):
        self.Cliente_id = Cliente_idRef