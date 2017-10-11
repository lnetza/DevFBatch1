class Persona(object):
    def __init__(self, nombre, email, age):

       self.nombre=nombre
       self.__email = email
       self.__age = age

    #Actualizar variables en variables privadas, con metodo publico
    def update_email(self, new_email):
        self.__email=new_email

    def email(self):
        return self.__email

    #Metodo privado
    def __show_age(self):
        return self.__email

    def show_age(self):
        return self.__get_age()

    #Metodo privado
    def __get_age(self):
        return self.__age

    """Sobrecarga de metodos"""

    def update_email(self,new_email,algo_mas):
        self.__email=new_email+algo_mas

np=Persona("Netza","l.lopez@gmail.com",24)
print (np.email())