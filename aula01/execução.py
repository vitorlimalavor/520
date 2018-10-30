#!/usr/bin/python3

from dog import Dog

dog1 = Dog('bilu','pitbull',1)
dog2 = Dog('rex','poodle',2)
dog1.latir()


print(dog1.nome)
print (dog2.nome)
dog1.dormir()
dog1.andar()