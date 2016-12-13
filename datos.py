import json               
class Peliculas:  
    data = []
    ##Leer Datos de Peliculas
    def read(self):
        with open('peliculas.json','r') as file:
            data = json.load(file)
            self.data = data['resultado'] 

    def getPeliculas(self): 
        peliculas = []
        for row in self.data:
            peli = row['nombre']
            if peli not in peliculas:
                peliculas.append(peli)
        return peliculas

class Clientes:  
    datos = []

    def read(self):
        with open('clientes.json','r') as file:
            datos = json.load(file)
            self.datos = datos['resultado'] 

    def getClientes(self): 
        clientes = []
        for row in self.datos:
            cliente = row['nombre']
            if cliente not in clientes:
                clientes.append(cliente)
        return clientes
