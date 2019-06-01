print('='*10)
print('DESAFIO 060 - Fatorial')
print('='*10,'\n')

n = int(input('Digite um número inteiro: '))
f = n
while n != 1:
    f = f * (n-1)
    n -= 1
print(f'Fatorial = {f}')
print('FIM')


#Solução Curso em Vídeo
n = int(input('Digite um número inteiro: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)