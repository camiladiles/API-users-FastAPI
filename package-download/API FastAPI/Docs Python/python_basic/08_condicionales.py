### Conditionals ###
'''
Manera de estabelecer flujo de nuestro codigo
Se algo vai funcionar ou não

So funciona quando a condição é verdadeira 'True'
'''

my_condition = False

if my_condition: #es lo mismo que 'if my_condition == True:'
    print("Se ejecuta la dondición del if")

my_condition = 5 ** 0

if my_condition == 10: 
    print("Se ejecuta la dondición del segundo if")

if my_condition > 10 and my_condition < 20: 
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual a 20")

print("La ejecución continua")

my_string = "Mi cadena de texto es no vacia"

if my_string:
    print("Mi cadena de texto es no vacia")

if my_string == "Mi cadena de texto es no vaciaaaaaa":
    print("Estas cadenas de textos coinciden")


print("La ejecución continua")


