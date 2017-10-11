class Perro(object):
    def __init__(self, edad,nombre, peso,raza,color):
        self.edad=edad
        self.nombre=nombre
        self.peso=peso
        self.raza=raza
        self.color=color

    def ladrar(self):
        print('Wuaa wuau!!!')

    def correr(self):
        print (self.nombre + ' Esta corriendo')

    def buscando(self):
        print('Estoy buscando un objeto perdido')




perro1=Perro(4,'Chicharo','5kg','Labrador','Hueso')

print('Edad:',perro1.edad)
print('Raza:',perro1.raza)

perro1.ladrar()
perro1.correr()