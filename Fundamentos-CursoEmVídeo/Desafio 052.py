print('='*10)
print('DESAFIO 052 - Números primos')
print('='*10,'\n')

n=int(input('Digite um número: '))
cont=0
for i in range(1, n+1):
    if n % i ==0:
        print('\033[33m',end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(f'{i}',end=' ')
print(f'\n\033[mNúmero {n} foi divisível {cont} vezes.')
if cont==2:
    print('Número é primo.')
else:
    print('Número NÃO é primo.')