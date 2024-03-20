# Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número

import random

def gera():
    return random.randint(1,100)

def game():
    resposta = gera()
    tentativa = 0
    print("\nPalpite gerado!")

    chute=0
    while chute is not resposta:
        tentativa +=1
        chute = int (input ("qual seu chute: "))
        if chute > resposta: 
            print("Errou!! É um valor menor que ", chute)
        elif chute < resposta:
            print("Errou! É um valor maio que ", chute)
        else:
            print("parabéns! O número gerado foi ",resposta, \
                  "Acertou em ",tentativa"tentativas!")
            
    while True:
        game()
