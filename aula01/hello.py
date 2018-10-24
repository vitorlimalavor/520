#!/usr/bin/python3
# isto é um comentario
print("hello world")
idade = input('Digite sua idade: ')

if idade.isnumeric(): 
   if ( int(idade) >= 18):
      print('maior de idade pode entrar')
   else:
      acomp = input('Acompanhado dos pais(s/n)')
      if acomp.lower() == 's':
          print ('Menor de idade mas acompanhado pelos pais pode entrar' ) 
      else:
       print ('Menor de idade sem acompanhamentos dos pais não pode entrar ')
else:
    print("Não é possivel converter")    