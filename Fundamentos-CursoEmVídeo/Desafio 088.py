from time import sleep
from random import randint

print('=' * 10)
print('DESAFIO 088 - Jogos Mega Sena')
print('=' * 10, '\n')

'''
j = int(input('Quantos jogos devo sortear? '))
jogo = []
p = 0

for i in range(0,j):
    for c in range(0,6):
        if c == 0:
            p = randint(1,60)
            jogo.append(p)
        else:
            while p in jogo:
                p = randint(1,60)
                jogo.append(p)
    jogo.sort()
    print(f'Jogo {i+1}: {jogo}')
    jogo.clear()
    sleep(1)
'''

#Solução CV
print('Solução CV')
print()
print('-'*30)
print(f'{"JOGO MEGA SENA":^30}')
print('-'*30)

lista = []
jogos = []
totjogos = 1
quant = int(input('Quantos jogos você quer que eu sorteie? '))

while totjogos <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totjogos += 1

for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)