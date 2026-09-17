#Declaração de Variáveis
n: int = 0
f: int = 0
a: int = 0

#Inicio
n = int(input("Digite o primeiro valor:"))
f = 1
for a in range (1,n):
    f = ((a+1) * f)
print (f"O fatorial de {n} é: {f}")