print('=' * 10)
print('DESAFIO 091 - Jogo de Dados')
print('=' * 10, '\n')

print('===== Solução CV =====')

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou o valor {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('--- RANKING ---')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

print('FIM DO PROGRAMA')