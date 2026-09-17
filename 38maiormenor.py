# Declaração de Variáveis
i: int = 0
num: float = 0.0
maior: float = 0.0
menor: float = 0.0

# Inicio
for i in range(0, 10):
    num = -1.0
    while (num < 0):
        num = float(input("Digite um valor positivo: "))
    
    if (i == 0):
        maior = num
        menor = num
    else:
        if (num > maior):
            maior = num
        if (num < menor):
            menor = num

print("Maior:", maior)
print("Menor:", menor)
#FIM