### Exceptions Handling ###
'''Manejo de errores'''

numberOne = 5
numberTwo = 1
numberTwo = "1"

#try except
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

#try except else finally
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: 
    #se ejecuta si se produce un except
    print("Se ha producido un error")
else: #es opcional
    #se ejecuta si no se produce un except
    print("La ejecución se ha producido correctamente")
finally: #es opcional
    #se ejecuta siempre
    print("La ejecución continúa")

#Exepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError: 
    #se ejecuta si se produce un except
    print("Se ha producido un TypeError")
except ValueError: 
    #se ejecuta si se produce un except
    print("Se ha producido un ValueError")

#Captura de la información de la exepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error: 
    print(error)
except Exception as exception: 
    print(exception)