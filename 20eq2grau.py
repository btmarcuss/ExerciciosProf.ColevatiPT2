#Declaração de variáveis
valor1: int = 0
valor2: int = 0
valor3: int = 0
delta: int = 0
raiz1: float = 0.0
raiz2: float = 0.0

#Inicio
valor1 = int(input("Digite o primeiro valor:"))
valor2 = int(input("Digite o segundo valor:"))
valor3 = int(input("Digite o terceiro valor:"))
if (valor1 == 0):
  print("coeficiente igual a 0")
else:
    delta = ((valor2 **2) - (4 * valor1 * valor3))
    if (delta < 0):
        print ("Não possui raiz real.")
    elif (delta == 0):
        raiz1 = ((valor2 * -1) / (2 * valor1))
        print (f"Possui apenas uma raiz, sendo {raiz1}")
    else:
        raiz1 = (((valor2 * -1) + (delta ** 0.5)) / (2 * valor1))
        raiz2 = (((valor2 * -1) - (delta ** 0.5)) / (2 * valor1))
        print (f"A primeira raiz é: {raiz1}")
        print (f"A segunda raiz é: {raiz2}")
