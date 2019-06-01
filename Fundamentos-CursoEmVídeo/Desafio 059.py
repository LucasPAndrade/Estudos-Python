print('='*10)
print('DESAFIO 059 - Operações')
print('='*10,'\n')

n1=float(input('Digite o primeiro valor: '))
n2=float(input('Digite o segundo valor: '))

sair = 0
while sair == 0:
    print('--- MENU ---\nSelecione uma das opções abaixo:')
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair do programa')
    opção=int(input('Opção: '))
    if opção == 1:
        print(f'Soma de {n1} com {n2} é {n1+n2}.')
    elif opção == 2:
        print(f'Multiplicação de {n1} com {n2} é {n1*n2}.')
    elif opção == 3:
        if n1 == n2:
            print('Números são iguais.')
        elif n1>n2:
            print(f'{n1} é o maior número.')
        else:
            print(f'{n2} é o maior número.')
    elif opção == 4:
        n1 = float(input('Digite novamente o primeiro valor: '))
        n2 = float(input('Digite novamente o segundo valor: '))
    elif opção == 5:
        sair = 1
        print('saindo do programa... Até logo!')
    else:
        print('Comando não identificado. Por favor tente novamente.')
    print('\n','=' * 30,'\n')