#Controle de Qualidade
#Por Daniels :D

import os
os.system("cls")

print("PROGRAMA DE CONTROLE DE QUALIDADE")
ap = 0
rep = 0
for cont in range(1, 401):
    sit = str(input(f"\nProduto {cont}: ")).upper()
    while sit != "APROVADO" and sit != "REPROVADO":
        sit = str(input(f"\nRESPOSTA INVÁLIDA\nProduto {cont}: ")).upper()
    if sit == "REPROVADO":
        rep += 1
        print("\nPRODUTO", cont, "REPROVADO")
    else:
        ap += 1
print("\n",ap," produtos aprovados\n",rep," produtos reprovados")