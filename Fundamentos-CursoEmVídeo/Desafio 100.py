print('=' * 10)
print('DESAFIO 100 - Função Sorteia')
print('=' * 10, '\n')

from random import randint
from time import sleep

lista = list()

def sorteia():
    print(f'- Números sorteados foram...', end='')
    for i in range(0,5):
        lista.append(randint(0,10))
        sleep(.5)
        print(lista[i], end=' ')
    print('PRONTO!')

def somaPar():
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'- Soma dos números pares é igual a {soma}.')

sorteia()
somaPar()