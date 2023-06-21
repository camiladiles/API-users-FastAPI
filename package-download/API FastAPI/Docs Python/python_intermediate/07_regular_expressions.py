### Regular Expressions ###

import re

my_string = "Esta es la lección 7: Lección llamada Expressiones Regulares"
my_other_string = "Esta es no es la lección 6: Manejo de Ficheros"

###########
#match - busca se tem algo em comum desde o principio da cadena de texto

match = re.match("Esta es la lección", my_string, re.I)
print(match) #aparece que tem
start, end = match.span() 
print(my_string[start:end])

match = re.match("Esta es la lección", my_other_string)
# if not(match == None): #esta es otra forma
#if match != None: #outra forma de comprovar o None
if match is not None:
    print(match) 
    start, end = match.span() 
    print(my_other_string[start:end])

print(re.match("Expressiones Regulares", my_string)) #não aparece porque não inicia assim

###########
#search - busca se tem algo em comum na cadena de texto (lo 1º que encontra)

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span() 
print(my_string[start:end])

###########
#findall - encontra a quantidade de ocoreencias do que esta buscando

findall = re.findall("lección", my_string, re.I)
print(findall)
#start, end = findall.span() 
#print(my_string[start:end])

###########
#split - busca um padrão e divide a partir desse padrão

print(re.split(":", my_string))

###########
#sub -

print(re.sub("Expressiones", "expressiones", my_string))
print(re.sub("Lección", "LECCIÓN", my_string))
print(re.sub("Expressiones Regulares", "RegEx", my_string))
print(re.sub("lección|Lección", "LECCIÓN", my_string))
print(re.sub("[l|L]ección", "LECCIÓN", my_string))

### Regular Expressions Patterns ###
''' As Expressões Regulares não é algo proprio de Python
É um conceito geral que se pode usar em todas as linguagens para gerar busca
ou seja, criamos um padrão de busca de expressões regulares e se pude utilizar 
este mesmo padrão em Java, em Python, em JavaScript, etc '''

# Para aprender y validar expresiones regulares: https://regex101.com


pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expressiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "camiladilesg@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "sandraramirez@gmail" #não é um email porque não concorda com a expressão regular
print(re.findall(pattern, email))

