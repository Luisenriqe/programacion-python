#Luis Enrique Jimenez Zavala.
#23/11/2016.
#Problema 2.
interes_anual = 0.04
saldo_inicial = input("deposito")
new_saldo=0
for i in range(4):
     saldo = saldo_inicial * 1.04
     new_saldo = new_saldo + saldo
print new_saldo
