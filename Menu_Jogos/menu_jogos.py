# MENU DE SELEÇÃO DE QUAL JOGO JOGAR!

import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")
while True:
    try:
        print("(1) Forca (2) Adivinhação")

        jogo = int(input("Qual jogo? "))

        if (jogo == 1):
            print("Jogando forca")
            forca.gerenciamento_do_jogo()
            break
        elif (jogo == 2):
            print("Jogando adivinhação")
            adivinhacao.manager_jogo()
            break
    except ValueError:
        print('Digite somente 1 - para jogar a Forca ou 2 para jogar Adivinhação!')