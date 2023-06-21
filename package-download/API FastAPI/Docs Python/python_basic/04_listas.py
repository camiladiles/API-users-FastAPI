### Listas ###
'''
List []: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple (): is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
'''

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 64, 17, 21, 12, 23, 30, 30]
print(my_list)
print(len(my_list))

my_other_list = [30, 166, "Camila", "Diles"] #pode guardar diferentes tipos de dados
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-3])
#print(my_other_list[-6]) (não existe esse elemento na lista)
print(my_other_list.count("Diles")) #count retonra o numero de ocorrencias de um valor
print(my_list.count(30))

print(my_other_list.index("Diles")) #index mostra o indece do valor desejado

#desempaquetando lista:
age, height, name, surname = my_other_list #adicionei os elementos da minha lista
print(height)

#desempaquetando lista de forma complicada, não tem necessidade de usar assim.
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)
#print(my_list * my_other_list) #SintaxError

#append adiciona um valor no final da lista
my_other_list.append("CamilaDiles") 
print(my_other_list)

#insert precisa escolher a posição e o elemento que quer adicionar.
my_other_list.insert(1, "verde") 
print(my_other_list)

my_other_list[1] = "azul"
print(my_other_list)

#remove para remover um UNICO valor conhecido (se tem repetição, so retira um deles)
my_other_list.remove("azul")
print(my_other_list)

my_list.remove(30) 
print(my_list)

#remove o ultimo valor da lista 
print(my_list.pop()) 
print(my_list)

my_pop_element = my_list.pop(2) 
print(my_pop_element) 
print(my_list)

#elimina um elemento #e se colocar a posição, elemina na posição escolhida
del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse() #invertendo a lista de tras para frente
print(my_new_list)

my_new_list.sort() #ordena a lista, como no tem nada () vai de menor a maior
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list)