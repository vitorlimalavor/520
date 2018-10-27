#!/usr/bin/python3

quadrados = []
for x in range(1,11):
    quadrados.append((lambda y :y **2) (x))
print (quadrados)

exit()

convidados = []
nome = input("Digite o nome do convidado para registro (sair para fechar o programa")
def adicionar(nome,idade):
    global convidados
    convidado = {'nome' : nome , 'idade': idade}
    convidados.append(convidado)
    
while True:
    nome = input('Digite um nome ou sair') 
    if nome.strip().lower() == 'sair' :
        break
    idade = int (input('digite a idade ') ) 
    adicionar(nome,idade)
print (convidados)  
    