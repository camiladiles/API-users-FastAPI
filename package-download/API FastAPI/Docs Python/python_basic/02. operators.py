### Operadores Aritmeticos ###

print(3 + 4) # soma
print(3 - 4) # resta
print(3 * 4) # multiplicação
print(3 / 4) # divisão
print(11 % 2) # modulo: faz a divisão e o resultado é o resto da divisão
print(10 // 3) # faz a divisão e sempre aproxima a um número inteiro, mesmo que seja decimal
print(2 ** 8) # potencia
print( 2 ** 4 + 7 - 2 // 4)

# Se pode operar com textos também como por exemplo aqui:
print("Hola" + "Python" + ". Que tal?")
print("Hola" + str(5))
print("Hola " * 5)

my_int = (2.5 * 2)
# print("Hola " * (my_int)) # Da um ERROR, porque "float * int = float"
print("Hola " * int(my_int)) #como transformei a variavel my_int em int, o resultado foi

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4  == 2) # se puede juntar difernetes operadores

print("Hola" > "Python") #se compara por ordenação alfabetica por ASCII
print("Hola" < "Python") # H vem antem de P
print("aaa" >= "aba") 
print(len("aaa") >= len("aba"))  #aqui conta caracteres
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python" )
print(3 > 4 or "Hola" > "Python" )
print(3 < 4 and "Hola" < "Python" )
print(3 < 4 or ("Hola" < "Python" and 4 == 4))
print(not 3 > 4) #como 3 > 4 é falso, então sua negação é verdadeira.