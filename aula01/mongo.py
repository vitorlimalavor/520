#!/usr/bin/python3
from pprint import pprint
from pymongo import MongoClient
try:
    con = MongoClient()
    db = con['projeto']
except Exception as e:
    print('Erro:{}'.format(e))
usuarios = []
for usuario in db.usuarios.find():
    usuarios.append(usuario)

#pprint(usuarios)
usuarios = [x for x in db.usuarios.find()]

db.usuarios.remove({'_id':1.0})
db.usuarios.update({"_id": 3},{"$set":{"sobrenome":"Lavor"}})
#db.usuarios.insert()

print(usuarios)