class precio:
    def __init__(self):
        self.FolioPrecio=0
        self.Tipo=""
        self.Precio=0.0
    
    #primero los getter
    def getPrecio(self):
        return self.Precio
    def getFolioPrecio(self):
        return self.FolioPrecio
    def getTipo(self):
        return self.Tipo
    
    #Ahora los setter
    def setPrecio(self, r):
        self.Precio = r
    def setFolioPrecio(self,PassRef):
        self.FolioPrecio=PassRef
    def setTipo(self,TipoRef):
        self.Tipo = TipoRef