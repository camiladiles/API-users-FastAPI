### Functions ###
''''
A function is a reusable block of code or programming statements designed
to perform a certain task. To define or declare a function, Python provides 
the def keyword. The following is the syntax for defining a function. 
The function block of code is executed only if the function is called or invoked.
'''

def my_funtion ():
    print("Esto es una función")

my_funtion ()

def sum_two_values (first_mumber, second_number):
    print(first_mumber + second_number)

sum_two_values(5, 7)
sum_two_values(23534, 74325435)
sum_two_values("5", "7")

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(10, 5)

print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(name = "Camila", surname = "Diles")

#função por defeito, vc deixa um valor que pode não ser usado quando a função é chamada
def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Camila", "Diles", "CDG")
print_name_with_default("Camila", "Diles") #como aqui ñ tem alias vai imprimir 'Sin Alias'

def print_texts (*texts):
    for text in texts:
        print(text)

print_texts("Hola")
print_texts("Hellow", "Que tal?")
print_texts("Hola que tal?", "Camila", "ACABOU")

def print_upper_texts (*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Camila", "Diles", "Caroline", "Sandra")

