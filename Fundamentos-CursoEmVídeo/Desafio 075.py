print('=' * 10)
print('DESAFIO 075 - Números')
print('=' * 10, '\n')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

num = (n1,n2,n3,n4)

print(f'Número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro 3 foi digitado na posição {num.index(3) + 1}')
else:
    print('O número 3 não foi digitado.')
print('Números pares:')
for n in num:
    if n % 2 == 0: print(n,end=', ')