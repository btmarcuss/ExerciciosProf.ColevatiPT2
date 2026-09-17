#Declaração de Variáveis
n1: int = 0
n2: int = 0
i: int = 0
soma: int = 0
maior: int = 0
menor: int = 0

#Inicio
n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o segundo valor:"))
soma = 0
if (n1 > n2):
    maior = n1
    menor = n2
    print (f"O maior é: {n1}.")
else:
    if (n2 > n1):
        maior = n2
        menor = n1
        print (f"O maior é {n2}.")
    else:
        maior = n1
        menor = n2
        print ("Os valores são iguais.")
for i in range (menor, (maior + 1)):
    if (i % 2 > 0):
        soma = soma + i
print (f"A soma dos impares é {soma}.")
