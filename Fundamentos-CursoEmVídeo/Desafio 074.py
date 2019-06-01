from random import randint

print('=' * 10)
print('DESAFIO 074 - Tupla com números aleatórios')
print('=' * 10, '\n')

n = 0
cont = 1
num = ()
while cont <= 5:
    n = randint(1,999)
    if cont == 1:
        min = n
        max = n
    elif n > max: max = n
    elif n < min: min = n
    #num = num + n
    cont +=1

print(num)
print(f'Maior número: {max}\nMenor número: {min}')

#Solução CV
numeros = (randint(1,10), randint(1,10),randint(1,10), randint(1, 10),randint(1,10))
print('Valores sorteados foram: ')
for n in numeros:
    print(f'{n}', end=' ')

print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')