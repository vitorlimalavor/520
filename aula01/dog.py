#!/usr/bin/python3

class Dog():
    def __init__(self,nome,raca,idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 5

    def latir(self):
        print (self.nome)
        print('auauauauau')
        
    
    def dormir(self):
        self.energia = 5
        print (self.energia)

    def andar(self):
        self.energia -= 1
        print (self.energia)


