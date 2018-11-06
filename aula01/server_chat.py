#!/usr/bin/python3
from pymongo import MongoClient, DESCENDING
import time

try:
    client = MongoClient()
    db = client['chat']
except Exception as e:
    print('Erro:{}'.format(e))
    exit()
def cadastrar(nome,mensagem):
    data = {
        'nome':nome,
        'mensagem': mensagem,
        'hora': time.strftime('%d-%m-%Y %H:%M:%S')
    }
    db.mensagens.insert(data)
def visualizar():
    ultimo =[x for x in db.mensagens.find().sort("_id", DESCENDING)]
    
    while True:
        data = [x for x in db.mensagens.find().sort("_id",DESCENDING)]
        if ultimo !=data:
            ultimo = data
            print("[{}] {} : {} \n".format(
                data[0]['hora'],data[0]['nome'],data[0]['mensagem']
            ))
        time.sleep(2)

