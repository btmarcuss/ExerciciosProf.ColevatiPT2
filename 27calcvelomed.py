#Declaração de Variáveis
nvoltas: int = 0
extcirc: int = 0
duracao: int = 0
distancia: int = 0
vmedia: int = 0

#Inicio
nvoltas = int(input("Digite o numero de voltas dadas:"))
extcirc = int(input("Digite quantos metros o circuito possui:"))
duracao = int(input("Digite quantos minutos durou:"))
distancia = (nvoltas * extcirc)
vmedia = ((distancia / duracao) / 16.667)
print (f"A velocidade média é {vmedia:.2f} Km/H.")