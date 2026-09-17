#Declaração de Variáveis
a: int = 0
b: int = 0
c: float = 0

#inicio
a = int(input("Digite o primeiro valor:"))
c = 0
for b in range (1, (a +1)):
    c = c +(1/b)
    print (c)