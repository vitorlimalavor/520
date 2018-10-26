#!/usr/bin/python3
ling = input("qual a melhor linguagem de programacao ?")
ling = ling.strip().lower()

if ling =='python':
    print("Você está no caminho certo")
elif ling == 'html' or ling =='css':
    raise ValueError('isso não é linguagem!!!')
else:
    print('Mude para python')


exit()
try:
    n=(input("Digite um numero"))
    n1= int(n)
    if n1 % 2 == 0:
        print("PAR")
    else:
        print("IMPAR") 
except ValueError:
    res = [ord(x) for x in n]
    res = sum(res)
    if res % 2 ==0:
        print ('par {}'.format(res))
    else:
        print ('impar {}'.format(res))
except Exception:
    print('Tratamento generico')
print ('nao parei a execucao')
