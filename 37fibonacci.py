#Declaração de Variáveis
n1: int = 0
i: int = 0
ac1: int = 0
ac2: int = 0
fibo: int = 0

#Inicio
n1 = int(input("Digite o valor"))
ac1 = 0
ac2 = 1
for i in range (0, (n1 + 1)):
    if (i == 0):
        ac1 = i
        print (ac1)
    else:
        fibo = ac1 + ac2
        print (fibo)
        ac2 = ac1
        ac1 = fibo
        