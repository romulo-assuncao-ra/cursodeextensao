import random
secreto = random.randint(1,100)
vidas = 10
palpite = int(input("Digite seu palpite: "))
while vidas > 0:
    if palpite == secreto:
        print (f"Parabens o numero era {secreto}")
        break
    elif palpite < secreto:
        print (f'O numero secreto é MAIOR.')
    else:
        print (f'O numero secreto é MENOR')
    vidas -= 1
    palpite = int(input("Digite seu palpite: "))
if vidas == 0:
    print (f'O numero secreto era {secreto}')
