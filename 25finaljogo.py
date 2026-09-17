#Declaração de Variáveis
hinicio: float = 0.0
hfinal: float = 0.0
tempojogo: float = 0.0

#Inicio
hinicio = float(input("Digite o horario de inicio:"))
if hinicio > 24:
    print ("Horario inválido.")
else:
    hfinal = float(input("Digite o horario final:"))
    if hfinal > 24:
        print ("Horario inválido.")
    else:
        if (hfinal < hinicio):
            hfinal = hfinal + 24.00
            tempojogo = hfinal - hinicio
            print (f"O jogo durou: {tempojogo:.2f}")
        else:
            tempojogo = hfinal - hinicio
            print (f"O jogo durou: {tempojogo:.2f}")