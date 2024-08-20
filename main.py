from cinematica import *

#mostra menu na tela
mostrar_menu()

while True:
    op = input('Digite o numero da operação que dejesa fazer: ')

    match op:
        case '1':
            m = float(input('Informe a massa em kg: ')).replace(',', '.')
            h = float(input('Informe a altura em metros: ')).replace(',', '.')
            print(f'Energia potencial: {calcular_ep(m, h):,.2f} J')
            continue
        case '2':
            m = float(input('Informe a massa em kg: ')).replace(',', '.')
            v = float(input('Informe a velocidade m/s: ')).replace(',', '.')
            print(f'Energia potencial: {calcular_ec(m, v):,.2f} J')
            continue
        case '3':
            break
        case _:
            print('Opção inválida!')
            continue
            
print('Progama encerrado!')