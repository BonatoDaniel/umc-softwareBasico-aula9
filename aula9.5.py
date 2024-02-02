#Cálculo de preço de produtos importados
#Por Daniels :D

import os
os.system('cls')

print('CÁLCULO DE PREÇO PARA PRODUTOS IMPORTADOS\n------------------------------------')
for cont in range(1, 6):
    print('Produto', cont,'\n------------------------------------')
    s = 0
    pu = float(input('Preço do Produto (R$): '))
    while pu <= 0:
        pu = float(input('VALOR INVÁLIDO\n\nPreço do Produto (R$): '))
    if pu <= 100:
        i = pu * 0.05
    else:
        i = pu * 0.1
    print('\n1 - EUA\n2 - México\n3 - Outros')
    po = int(input('\nPaís de origem: '))
    while po < 1 or po > 3:
        po = int('VALOR INVÁLIDO\n\nPaís de origem: ')
    if po == 2:
        print("\nSEGURO ADICIONADO")
        s = pu / 2
    print('\nT - Terrestre\nF - Fluvial\nA - Aéreo')
    mt = str(input('\nMeio de transporte: ')).upper()
    while mt != 'T' and mt != 'F' and mt != 'A':
        mt = str(input('VALOR INVÁLIDO\n\nMeio de transporte: ')).upper()
    if mt == 'A' and s == 0:
        print("\nSEGURO ADICIONADO")
        s = pu / 2
    pc = str(input('\nCarga perigosa? S/N: ')).upper()
    while pc != 'S' and pc != 'N':
        pc = str(input('VALOR INVÁLIDO\n\nCarga perigosa? S/N: ')).upper()
    if pc == 'S':
        match po:
            case 1:
                vt = 50
            case 2:
                vt = 35
            case 3:
                vt = 24
    else:
        match po:
            case 1:
                vt = 12
            case 2:
                vt = 35
            case 3:
                vt = 60
    pf = pu + i + s + vt
    print(f'''------------------------------------
     Preço unitário: R${pu:.2f}
Valor do Transporte: R${vt:.2f}
            Imposto: R${i:.2f}
             Seguro: R${s:.2f}

        Valor Total: R${pf:.2f}
------------------------------------''')