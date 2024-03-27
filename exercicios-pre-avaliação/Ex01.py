# Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número

import random

numero = random.randint(1,100)

print(numero)

while True:
    palpite = int(input("Insira seu palpite do número: "))
    if palpite == numero:
        print("Parabéns,você acertou!")
        break
    if palpite > numero:
        print("Tente novamente, o seu palpite está muito alto!")
    else:
        print("Tente novamente, o seu palpite esta muito baixo!")

