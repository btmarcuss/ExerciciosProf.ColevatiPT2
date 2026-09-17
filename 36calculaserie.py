#Declaração de Variáveis
n: int = 0
i: int = 0
fat: float = 0.0
soma: float = 0.0

#Inicio
n = int(input("Digite o valor:"))
soma = 1
fat = 1
for i in range (1, n +1):
    fat = fat * i
    soma = soma + (1/fat)
print (f"O resultado é: {soma}")