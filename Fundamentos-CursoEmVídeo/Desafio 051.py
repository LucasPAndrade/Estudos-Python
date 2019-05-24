print('='*10)
print('DESAFIO 051 - Progressão aritmética')
print('='*10,'\n')

p=int(input('Primeiro termo: '))
r=int(input('Razão: '))

for i in range(1,11):
    pa=p+(i-1)*r
    print(pa, end=' ')