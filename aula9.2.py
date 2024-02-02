#Jogo de Adivinhação
#Por Daniels :D

import os
os.system("cls")

print("JOGO DE ADIVINHAÇÃO")
x = int(input("\nJogador 1, escolha o número que o Jogador 2 deverá descobrir.\nLembrando que o número deverá ser um valor inteiro de 1 a 10: "))
while x < 1 or x > 10:
    x = int(input("\nVALOR INVÁLIDO.\nLembre-se: apenas valores inteiros de 1 a 10: "))
cont = 0
y = 0
os.system('cls')
print("Sua vez, Jogador 2!\nDigite o valor que acha ser a digitada pelo jogador 2.\nLembrand3o sempre, apenas valores inteiros de 1 a 10.")
while y != x:
    cont += 1
    print("\nTentativa", cont)
    y = int(input("Valor: "))
print(f"\nMeus parabéns! Valor encontrado!\nA resposta era {x}!\n\nVocê descobriu o valor digitado em um total de {cont} tentativa(s)!\n")