### File Handling ###
''' Manejo de Ficheros '''

import os

##############
# .txt file

txt_file = open("python_intermediate/my_file.txt", "w+") #r+ -> Leer y Escribir

txt_file.write("Mi nombre es Camila\nMi apellido es Diles\n30 Años\nMi lengaje preferida es Python")

print(txt_file.read())
print(txt_file.read(10)) #leer los 10 primeiros caracteres
print(txt_file.readline())
print(txt_file.readline())

print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAún que también me gusta Kotlin")
print(txt_file.readlines())

txt_file.close

#os.remove("python_intermediate/my_file.txt")

with open("python_intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

##############
# .json file

import json 

json_file = open("python_intermediate/my_file.json", "w+")

json_test = {
    "name":"Brais", 
    "surname":"Moure", 
    "age":35, 
    "language":["Python", "Swift", "Kotlin"],
    "website":"https://moure.dev",
    }

json.dump(json_test, json_file, indent = 2)

json_file.close()

with open("python_intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)
    
json_dict = json.load(open("python_intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

##############
# .csv file
import csv

csv_file = open("python_intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "apellido", "age", "language", "website"])
csv_writer.writerow(["Camila", "Diles", 30, "Python", "https://cdiles.com"])
csv_writer.writerow(["Sandra", "Ramirez", 31, "Java", "https://sramirez.com"])


csv_file.close()

with open("python_intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

##############
# .xlsx file
#import xlsl #Devemos instalar o modulo

##############
# .xml file
import xml