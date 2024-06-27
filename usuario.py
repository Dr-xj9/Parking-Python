class usuario:
    def __init__(self):
        self.Usuario_id=0
        self.Nombre=""
        self.UserName=""
        self.Password=""
        self.Perfil=""
        self.Email=""
    
    #primero los getter
    def getUsuario_id(self):
        return self.Usuario_id
    def getNombre(self):
        return self.Nombre
    def getUserName(self):
        return self.UserName
    def getEmail(self):
        return self.Email     
    def getPassword(self):
        return self.Password
    def getPerfil(self):
        return self.Perfil
    
    #Ahora los setter
    def setUsuario_id(self,idReferencia):
        self.Usuario_id = idReferencia
    def setNombre(self,NombreReferencia):
        self.Nombre = NombreReferencia
    def setUserName(self,UserRef):
        self.UserName = UserRef
    def setEmail(self, EmailRef):
        self.Email = EmailRef    
    def setPassword(self,PassRef):
        self.Password=PassRef
    def setPerfil(self,PerfilRef):
        self.Perfil = PerfilRef