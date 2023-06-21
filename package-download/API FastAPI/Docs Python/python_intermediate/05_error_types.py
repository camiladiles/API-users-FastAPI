### Error Types ###

########################
# SyntaxError

#print"Hola Comunidad!" 
''' SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)? '''

print("Hola Comunidad!")

########################
# NameError

#print(language)
''' NameError: name 'language' is not defined '''

language = "Spanish" #1º defini a variavel e já ão da erro.
print(language)

########################
# IndexError

my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])

#print(my_list[5]) 
''' IndexError: list index out of range '''

########################
# ModuleNotFoundError

#import maths
''' ModuleNotFoundError: No module named 'maths' '''

import math

########################
# AttributeError

#print(math.PI)
''' AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'? '''

print(math.pi)

########################
# KeyError

my_dict = {"Nombre":"Brais", "Apellido":"Moure", "Edad":35, 1:"Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"])
''' KeyError: 'Apelido' '''
print(my_dict["Apellido"])

########################
# TypyError

#print(my_list["0"])
''' TypeError: list indices must be integers or slices, not str '''
print(my_list[0])

########################
# ImportError

#from math import pii
''' ImportError: cannot import name 'pii' from 'math' '''
from math import pi 
print(pi)

########################
# ValueError

my_int = int("10")
print(type(my_int + 10))

# my_int = int("10 Años")
# print(type(my_int))
''' ValueError: invalid literal for int() with base 10: '10 Años' '''

########################
# ZeroDivisionError

print(4/2)
# print(4/0)
''' ZeroDivisionError: division by zero '''
