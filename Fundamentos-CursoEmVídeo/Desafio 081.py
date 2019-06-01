print('=' * 10)
print('DESAFIO 081 - Números...')
print('=' * 10, '\n')

lista = list()
cont = 0

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1

    r = str(input('Deseja continuar? [S/N]'))
    while r not in 'sSnN':
        r = str(input('Deseja continuar? [S/N]'))
    if r in 'nN':
        break

lista.sort(reverse=True)
print(f'{cont} números digitados.')
print(lista)
if 5 in lista:
    print(f'O valor 5 faz parte da lista! Posição {lista.index(5)+1}.')
else:
    print('Valor 5 não faz parte da lista...')