### Dicionarios ###
''''
A dictionary is a collection of unordered, modifiable(mutable)
paired (key: value) data type.
'''

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Camila", "Apellido":"Diles", "Edad":30, 1:"Python"}
my_dict = {
    "Nombre":"Camila", 
    "Apellido":"Diles", 
    "Edad":30, 
    "Lengajes":{"Python", "Swift", "Kotlin"},
    1: 1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"]) #Para ver o valor do nome no dicionario

my_dict["Nombre"] = "Sandra"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Jr Ayacucho" #Adiciono outro elemento no meu dicionario
print(my_dict)

del my_dict["Calle"] #Para deletar um elemento do dicionario
print(my_dict)

print("Apellido" in my_dict)
print("Diles" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list) #Cria um dicionario sem valores
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) #posso pegar um dicionario e usar sem valores
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Camila")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(dict.fromkeys(list(my_new_dict)))
print(tuple(my_new_dict))
print(set(my_new_dict))
