### Tuplas ###
''''
A tuple is a collection of different data types which is ordered and unchangeable
(immutable). Tuples are written with round brackets, (). Once a tuple is created,
we cannot change its values. We cannot use add, insert, remove methods in a tuple
because it is not modifiable (mutable).
'''

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (30, 166, "Camila", "Diles", "Camila")
my_other_tuple = (31, 32, 33)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Camila")) #para contar quantos elementos "Camila" tem na tupla
print(my_tuple.index("Diles")) #mostra o indece do valor desejado

#my_tuple[1] = 170 (SintaxError - porque uma tupla não pode alterar seus elementos)
#print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple 
print(my_sum_tuple)

print(my_sum_tuple[3:6])

#Transformando a tupla em uma lista:
my_tuple = list(my_tuple)
print(type(my_tuple))

#agora pode adicionar e retirar elementos
my_tuple[4] = "CDiles"
my_tuple.insert(1, "Vermelho")
#Transformando agora a lista e tuple:
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple #SintaxError - não se pode remover os elementos das tuplas
#print(my_tuple)