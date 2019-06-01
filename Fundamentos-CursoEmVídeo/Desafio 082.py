print('=' * 10)
print('DESAFIO 082 - Números...')
print('=' * 10, '\n')

lista = pares = ímpares = []
pares = []
ímpares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? [S/N]'))
    while r not in 'sSnN':
        r = str(input('Deseja continuar? [S/N]'))
    if r in 'nN':
        break

lista.sort()

for p in lista:
    if p % 2 == 0:
        pares.append(p)
    else:
        ímpares.append(p)

print(f'Lista completa: {lista}')
print(f'Lista pares: {pares}')
print(f'Lista ímpares: {ímpares}')