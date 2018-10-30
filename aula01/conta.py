#!/usr/bin/python3
class Conta():
    def __init__(self,titular,num_conta,saldo=0):
        self.titular = titular
        self.num_conta = num_conta
        self.saldo = saldo 
    
    def depositar(self,valor):
        self.saldo += valor
        return self.saldo    
    
    def sacar (self,valor):
        if self.saldo < valor:
            raise ValueError ("Saldo INsuficiente")
        else:
            return ("Efetuado")
            self.saldo -= valor
            return self.saldo

    def tranf (self,valor,conta):
        try:
            self.sacar(valor)
            conta.depositar(valor)
        except ValueError as e:
            print (e)
            return 'Nao foi possivel realizar a transferencia'
        except Exception:
            return "Conta destino invalida"
        return self.saldo

class Poupanca(Conta):
    def __init__(self,titular,num,saldo):
        super().__init__(titular,num,saldo)
        self.taxa = 0
   
c1 = Conta('daniel',1244343, 2000)
print (c1.saldo)
c2 = Conta('maria',1243434,4000)
print(c1.tranf(50000000,c2))



            
        