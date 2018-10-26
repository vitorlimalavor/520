#!/usr/bin/python3
matriz = [
    [1,2,3],
    [4,5,6],
    [5,2,1]
]
soma = 0
for c,m in enumerate(matriz):
    soma += m[c] + m[-[(c+1)]
print(soma) 

     
