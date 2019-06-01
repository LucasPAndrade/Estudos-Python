print('=' * 10)
print('DESAFIO 085 - Lista única com pares e ímpares')
print('=' * 10, '\n')

lista = [[],[]]

i = 0
for i in range(0,7):
    n = int(input(f'Digite o {i+1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print(lista)
lista[0].sort()
lista[1].sort()
print(f'Números pares: {lista[0]}')
print(f'Números ímpares: {lista[1]}')