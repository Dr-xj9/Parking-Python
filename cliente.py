class cliente:
    def __init__(self):
        self.Cliente_id=0
        self.Nombre=""
        self.Telefono=""
        self.Email=""
        self.Usuario_id=0
        self.RFC=""
    
    #primero los getter
    def getCliente_id(self):
        return self.Cliente_id
    def getNombre(self):
        return self.Nombre
    def getTelefono(self):
        return self.Telefono
    def getEmail(self):
        return self.Email     
    def getUsuario_id(self):
        return self.Usuario_id
    def getRFC(self):
        return self.RFC
    
    #Ahora los setter
    def setCliente_id(self,idReferencia):
        self.Cliente_id = idReferencia
    def setNombre(self,NombreReferencia):
        self.Nombre = NombreReferencia
    def setTelefono(self,UserRef):
        self.Telefono = UserRef
    def setEmail(self, EmailRef):
        self.Email = EmailRef    
    def setUsuario_id(self,PassRef):
        self.Usuario_id=PassRef
    def setRFC(self,RFCRef):
        self.RFC = RFCRef