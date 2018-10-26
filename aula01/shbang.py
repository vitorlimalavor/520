#!/usr/bin/python3
shbang="#!/usr/bin/python3"
arquivo=input("Digite o nome do arquivo")
try:
    with open(arquivo+'.py','x') as arq:
        arq.write(shbang)
except FileExistsError:
    with open(arquivo+'.py','r') as arq:
        conteudo = arq.readlines()
    
    if conteudo[0] != shbang:
        conteudo.insert(0,shbang)
    
    with open(arquivo+'.py','w') as arq:
        arq.writelines(conteudo)

