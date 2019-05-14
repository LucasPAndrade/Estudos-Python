import random
from time import sleep
print('===== DESAFIO 028 =====\n')

palpite=int(input('Qual número, de 0 a 5, o computador escolheu? Digite: '))
n=random.randint(0,5)
print('PROCESSANDO...')
sleep(3)
print(f'Você acertou!!! Nº {n}' if palpite==n else f'Você errou... o nº correto era {n}')