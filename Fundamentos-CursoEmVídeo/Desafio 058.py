from random import randint

print('=' * 10)
print('DESAFIO 058 - Jogo de advinhar')
print('=' * 10, '\n')

print('Tente adivinhar qual número, de 0 a 10, o computador escolheu.')
pc = randint(0, 10)

sair = False
cont = 1

while not sair:
    user = int(input('Digite seu palpite (0 a 10): '))
    cont += 1
    if pc != user:
        print('Você errou. Tente novamente!')
    else:
        sair = True
        print(f'\033[35mVocê acertou!!!\033[m Você fez {cont} palpite(s).')
