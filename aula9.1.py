#Aumento populacional de dois países
#Por Daniels :D

import os
os.system("cls")

print("AUMENTO POPULACIONAL DE DOIS PAÍSES")
hp1 = 98000000
hp2 = 200000000
x = 0
while hp1 < hp2:
    hp1 = hp1 * 1.006
    hp2 = hp2 * 1.005
    x += 1
print(f"\nEm {x} anos, o número de habitantes do país 1 ultrapassará o do país 2.\n\nPaís 1: {hp1:.0f}\nPaís 2: {hp2:.0f}")