### Loops ###
''''
Life is full of routines. In programming we also do lots of repetitive tasks.
In order to handle repetitive task programming languages use loops.
Python programming language also provides the following types of two loops:
while loop
for loop
'''

#While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #aqui o else es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continua")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es igual a 15")
        break #quando a execução for igual a 15 se detem a execução
        
    print(my_condition)

print("La ejecución continua")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Camila", "Apellido":"Diles", "Edad":30, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break #cuando tiene un break, el else ya no es necesario
    print("Se ejecuta")
else:
    print("finalizo o loop")

for element in list(my_dict.values()):
    print(element)

print("La ejecución continua")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue #sigue para adelante
    print("Se ejecuta")
else:
    print("finalizo o loop")

