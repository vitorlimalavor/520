#!/usr/bin/python3
notas=0
put = int(input("Digite quantidade de notas"))
for i in range(put):
    nota = float(input ("Digite a nota {}:".format(i+1)))
    notas += nota
media = notas / put
if (media >= 7):
    result = "Aprovado"
elif (media > 3):
    result = "Recuperacao"
else:
    result = "Reprovado"

print (media)
print (result)