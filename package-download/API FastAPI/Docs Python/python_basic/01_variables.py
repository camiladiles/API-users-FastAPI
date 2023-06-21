# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable) # imprime el 5, pero lo transformo en string (texto)
print(type(my_int_to_str_variable)) # aqui podemos ver a class que imprimio 'str'

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable) #para colocar texto se coloca entre ""
# para colocar variavel apenas escrevemos ela. A virgula para separar dos prints em um

# Algunas funcione del sistema
print(len(my_int_to_str_variable)) #conta quanto espaço foi usado

# Variables en una sola línea. (Cuidado para não abusar desta sintaxis!)
name, surname, alias, age = "Camila", "Diles", "camiladiles", 30
print("Me llamo:", name, surname,". Mi edad es:", age, ". Y mi alias es:", alias) 

#Imputs: para de rodar o programa e faz pergunta para adicionar alguma resposta
'''
first_name = input('What is your name: ')
age = input('How old are you? ')
print(first_name)
print(age)
'''

#Cambios de tu tipo:
name = 30
age = "Camila" 
print(name)
print(age)

#Forzamos el tipo?
address: str = "Mi dirección"
address = 30
print(type(address))