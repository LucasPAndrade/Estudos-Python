from random import randint
from time import sleep

print('='*10)
print('DESAFIO 068 - Par ou Ímpar')
print('='*10,'\n')

check = False
soma = vitória = 0

while True:
    while check == False:
        escolha = str(input('Par ou Ímpar? Digite p ou i: ')).lower()
        if escolha != 'p' and escolha != 'i':
            print('Opção inválida (digite p ou i). Tente novamente...')
        else:
            check = True
    user = int(input('Digite um número: '))
    pc = randint(1,5)
    print('Jogo do computador...', end='')
    sleep(2)
    print(pc)
    soma = user + pc
    if (escolha == 'p' and soma % 2 == 0) or (escolha == 'i' and soma % 2 != 0):
        vitória += 1
        print('Você venceu!')
    else:
        print(f'Após ganhar {vitória} jogo(s), você PERDEU...')
        print('FIM DE JOGO!')
        break
    check = False