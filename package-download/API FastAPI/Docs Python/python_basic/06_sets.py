### Sets ###
''''
is a collection of items. is a collection of unordered and un-indexed distinct elements.
In Python set is used to store unique items, and it is possible to find the union,
intersection, difference, symmetric difference, subset, super set and disjoint
set among sets.
'''

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente o tipo aparece 'dict'

my_other_set = {"Camila", "Diles", 30}
print(type(my_other_set)) #Agora aparece que o tipo é um 'set'

print(len(my_other_set))

my_other_set.add("CDG")
print(my_other_set) #um set não é uma estrutura ordenada

my_other_set.add("CDG") #um set não adimite repetições (os elementos não se repetem)
print(my_other_set)

print("Diles" in my_other_set) #Diles esta no set
print("Deles" in my_other_set) #Deles não esta no set

my_other_set.remove("Diles")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

#Transformando um set em uma lista (porém não é recomendavel)
my_set = {"Camila", "Diles", 30}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin","Swift", "Python" }
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set)) #saca a diferenca my_new_set MENOS my_set



