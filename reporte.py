class semana:
    def __init__(self):
        self.anio = 0
        self.semana = 0
        self.servicios = 0
        
    def set_anio(self, anio):
        self.anio = anio
    
    def get_anio(self):
        return self.anio
    
    def set_semana(self, semana):
        self.semana = semana
    
    def get_semana(self):
        return self.semana
    
    def set_servicio(self, servicios):
        self.servicios= servicios
    
    def get_servicio(self):
        return self.servicios
    
class reporte:
    def __init__(self):
        self.anio = 0
        self.mes = 0
        self.entradas = 0
        self.salidas = 0
        
    def set_anio(self, anio):
        self.anio = anio
    
    def get_anio(self):
        return self.anio
    
    def set_mes(self, mes):
        self.mes = mes
    
    def get_mes(self):
        return self.mes
    
    def set_entradas(self, entradas):
        self.entradas = entradas
    
    def get_entradas(self):
        return self.entradas
    
    def set_salidas(self, salidas):
        self.salidas = salidas
    
    def get_salidas(self):
        return self.salidas
