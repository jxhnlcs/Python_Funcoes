import random
from time import sleep

venceu ="Você ganhou, parabéns!\n"
perdeu="Você perdeu!\nTente de novo"
ponto="Ponto"

def jogo():

    dado1=random.randrange(1,6)
    dado2=random.randrange(1,6)

    soma=dado1+dado2
    print("====")
    sleep(1)
    print("Dado 1: ",dado1)
    sleep(1)
    print("Dado 2: ",dado2)
    sleep(1)
    print("A soma dos dados é: ",soma,)
    sleep(1)
    print("====")

    return soma

print("Bem-vindo a questão mais difícil de Ícaro\nDivirta-se")

while True:
    jogar=input("Rolar dados (Digite n para sair, aperte <enter> para jogar)? ")

    if jogar=="n" or jogar=="N":
        break
    
    else:
        result=jogo()

        if result==7 or result==11:
            sleep(1)
            print(venceu)

        elif result==2 or result==3 or result==12:
            sleep(1)
            print(perdeu)

        else:
            print(ponto)
            while True:
                result2=jogo()

                if result==result2:
                    print(venceu)
                    break

                elif result2==7:
                    print(perdeu)
                    break

                else:
                    print("Você ainda tá no jogo primo!\n")
                    sleep(1)