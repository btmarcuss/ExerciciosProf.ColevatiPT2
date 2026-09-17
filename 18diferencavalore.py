#Declaração de variaveis
valor1: int = 0
valor2: int = 0
diferenca: int = 0 

#inicio
valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))
if (valor1 > valor2):
    diferenca = (valor1 - valor2)
elif (valor1 == valor2):
    diferenca = (valor1 - valor2)
else:
    diferenca = (valor2 - valor1)
print (f"A diferença dos valores é: {diferenca}")
#FIM
