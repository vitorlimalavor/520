#!/usr/bin/python3
lista = ['a' , 'b','c']
with open('teste.txt','a') as arq:
    arq.write('estou acrescentando \n')
    arq.writelines(lista)
with open('teste.txt','r') as arq:
    conteudo = arq.read()
print (conteudo)

with open('teste.txt', 'w') as arq:
    arq.writelines(conteudo)
