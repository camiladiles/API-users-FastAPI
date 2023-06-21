### MongoDB client ###

# Descarga versión community: https://www.mongodb.com/try/download
# Instalación:https://www.mongodb.com/docs/manual/tutorial
# Módulo conexión MongoDB: pip install pymongo
# Ejecución: sudo mongod --dbpath "/path/a/la/base/de/datos/"
# Conexión: mongodb://localhost

from pymongo import MongoClient

# Descomentar el db_client local o remoto correspondiente

#Base de datos local MongoDB
#db_client = MongoClient().local


# Base de datos remota MongoDB Atlas (https://mongodb.com)
db_client = MongoClient(
    "mongodb+srv://cdiles:81538592@cluster0.ulu9hrp.mongodb.net/?retryWrites=true&w=majority").test



# Despliegue API en la nube:
# Deta - https://www.deta.sh/
# Intrucciones - https://fastapi.tiangolo.com/deployment/deta/

#token: W8ZN4cNw_6MHZjtnTaM4o4jFeBEDYrJZmc1UHrnSX
