### Higher Order Functions ###
''' Funções de Ordem Superior'''

from functools import reduce 

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

#Adicionando a def sum_one dentro do return da nova def
def sum_two_values_and__add_one(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_and__add_one(5, 2))

#adicionando um terceiro valor que no final ao chamar sera o sum_one
def sum_two_values_and__add_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and__add_one(5, 2, sum_one))
print(sum_two_values_and__add_one(5, 2, sum_five))

### Closures ### É uma função que retorna uma função

def sum_ten():
    def add(value):
        return value + 10
    return add
    
add_closure = sum_ten()
print(add_closure(5))

##########

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add
    
add_closure = sum_ten(5)
print(add_closure(5))

print((sum_ten(5))(5))

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 33, 42]

#Map - recorria cada uno de los valores y ejecuta una función

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

#Filter - recorria cada uno de los valores y filtraba valores

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten , numbers)))
print(list(filter(lambda number: number > 10 , numbers)))

#Reduce - operar entre los valores que va recorrendo

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))
''' pega a lista, soma os dos primeiros valores, soma, logo a soma se torna o 1º valor e
 o segundo valor se torna o segundo, ate terminar todos os valors.'''

print("Terminamos")

