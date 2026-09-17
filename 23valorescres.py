#Declaração de Variáveis
v1: int = 0
v2: int = 0
v3: int = 0
v4: int = 0

#Inicio
v1 = int(input("Digite o primeiro valor:"))
v2 = int(input("Digite o segundo valor:"))
if (v1 > v2):
    print ("Digite um valor maior que o primeiro.")
else:
    v3 = int(input("Digite o terceiro valor:"))
    if (v2 > v3):
        print ("Digite um valor maior que o segundo.")
    else:
        v4 = int(input("Digite o quarto valor:"))
        if (v4 == 0):
            print ("Valores Inválidos.")
        elif(v4 < v1):
            print (v4, v1, v2, v3)
        elif (v4 > v1 and v4 < v2):
            print (v1, v4, v2, v3)
        elif (v4 > v2 and v4 < v3):
            print (v1, v2, v4, v3)
        else:
           print (v1, v2, v3, v4)
