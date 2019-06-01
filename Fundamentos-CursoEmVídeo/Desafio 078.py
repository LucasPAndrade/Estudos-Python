print('=' * 10)
print('DESAFIO 078 - Números em lista')
print('=' * 10, '\n')

lista = []
for i in range(0,5):
    lista.append(int(input('Digite um número: ')))

max = min = 0
for p, n in enumerate(lista):
    if n > max: max = n
    if p == 0 or n < min: min = n

p = n = 0

print(f'Maior valor foi {max}, posição ', end='')
for p, n in enumerate(lista):
    if n == max:print(f'{p+1}',end='... ')

print(f'\nMenor valor foi {min}, posição ', end='')
for p, n in enumerate(lista):
    if n == min:print(f'{p+1}',end='... ')