### Classes ###
''''
Si tenemos una clase, tudo que esta dentro de esta clase tiene que responder a una logica
Eje: se tenemos la clase persona, tenemos que tener todo relacionado con persona
Classe es un objeto, que serve para definir una entidad que por ejemplo puede ser
una persona
'''

#por convención as classes escrevemos como camecase (Maiuscula na primeira letra)
class MyEmptyPerson:
    pass 

print(MyEmptyPerson)
print(MyEmptyPerson())

#def __init__ (self): es un consutor de classe, não é uma função
class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
       self.full_name = f"{name} {surname} ({alias})" #Propiedade Publica
       self.__name = name #Propriedade Privada

    def get_name (self):
        return self.__name


    def walk (self):
        print(f"{self.full_name} esta caminando")

my_person = Person("Camila", "Diles")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Sandra", "Ramirez", "SRR")
print(my_other_person.full_name)
my_other_person.walk()

my_other_person.full_name = "Caroline Diles (Engorda Maga)"
print(my_other_person.full_name)







