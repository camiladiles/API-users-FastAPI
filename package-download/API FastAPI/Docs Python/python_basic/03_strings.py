### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + "" + my_other_string)

# \n para saltar uma linha
my_new_line_string = "Este es un string \n con salto de línea"
print(my_new_line_string)

#\t para da um espaço de inicio de frase
my_tab_string = "\tEste es un string con salto de línea"
print(my_tab_string)

#\t e logo \n vai dar o espaço inicial para cada linha de texto
my_scape_string = "\tEste es un string \n con salto de línea"
print(my_scape_string)

# Se adiciono outra \ no codigo ele vai saltar a solicitação pedida
my_scape2_string = "\\tEste es un string \\n con salto de línea"
print(my_scape2_string)

# Formateo con % e com .format

name, surname, age = "Camila", "Diles", 30
print("Mi nombre es {} {} y mi edad es {}" .format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
#forma mas complicada e trabalhosa
print("Mi nombre es " + name + "" + surname + "y mi edade es " + str(age))
#Uma forma ainda mais simples que as anteriores:
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

'''
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision
'''

# Desempequetado de Caracteres

language = "python"
a, b, c, d, e, f = language # unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slice = language[1:3] #vai da 1 a 3 sem contar a 3. (0 é a primeira, 1 é a 2º)
print(language_slice)

language_slice = language[1:] #vai do 1 ate a última
print(language_slice)

language_slice = language[-2] #se coloca negativo vai de tras para frente
print(language_slice)

reversed_language = language[0:6:2] #vai de 0 ate antes do 6 e pula de 2 em 2
print(reversed_language)

# Reverse language

reversed_language = language[::-1]
print(reversed_language)

# Funciones del sistema

print(language.capitalize()) #transforma a primeira letra em maiuscula
print(language.upper()) #transforma tudo em maiuscula
print(language.count("t")) #conta quantas t tem na palavra python
print(language.isnumeric()) #diz si True or False se é ou não número
print("1".isnumeric())
print(language.lower()) #transforma tudo em menuscula
print(language.upper().isupper()) #usando duas funções juntas
print(language.startswith("py")) #perguntando se algo começa com tal coisa