#Lanchonete Bom Apetite
#Por Daniels :D

import os

resp2 = 'S'
while resp2 == 'S':
    os.system('cls')
    print('''-----------------------------------------
LANCHONETE BOM APETITE: CARDÁPIO
-----------------------------------------
CÓDIGO    ESPECIFICAÇÃO      PREÇO (R$)
-----------------------------------------
100       CACHORRO QUENTE    2,50
101       BAURU SIMPLES      2,00
102       BAURU COM OVO      3,50
103       HAMBURGUER         5,10
104       CHEESEBURGUER      3,30
105       REFRIGERANTE       2,00
-----------------------------------------''')
    resp1 = 'S'
    vt = 0
    while resp1 == 'S':
        cod = int(input('\nCódigo: '))
        while cod < 100 or cod > 105:
            cod = int(input('CÓDIGO INVÁLIDO\n\nCódigo: '))
        match cod:
            case 100:
                print('CACHORRO QUENTE')
                v = 2.5
            case 101:
                print('BAURU SIMPLES')
                v = 2
            case 102:
                print('BAURU COM OVO')
                v = 3.5
            case 103:
                print('HAMBURGUER')
                v = 5.1
            case 104:
                print('CHEESEBURGUER')
                v = 3.3
            case 105:
                print('REFRIGERANTE')
                v = 2
        qtd = int(input('\nQuantidade: '))
        while qtd <= 0:
            qtd = int(input('VALOR INVÁLIDO\n\nQuantidade: '))
        vt += (v * qtd)
        resp1 = str(input('\nDeseja inserir mais algum produto? S/N: ')).upper()
        while resp1 != 'S' and resp1 != 'N':
            resp1 = str(input('RESPOSTA INVÁLIDA\n\nDeseja inserir mais algum produto? S/N: ')).upper()
    print(f'\nValor total do pedido: R${vt:.2f}')
    resp2 = str(input('Cadastrar novo pedido? S/N: ')).upper()
    while resp2 != 'S' and resp2 != 'N':
        resp2 = str(input('RESPOSTA INVÁLIDA\n\nCadastrar novo pedido? S/N: ')).upper()
print('\n:D')