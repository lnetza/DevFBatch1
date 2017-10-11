'''
#Comentario
'''
class Animal(object):
    def __init__(self, patas, edad):
        self.patas=patas
        self.edad=edad

    def caminar(self):
        print 'estoy caminando'

class Perro(Animal):
    def __init__(self,patas,edad, raza,color,tamano,hijos):
