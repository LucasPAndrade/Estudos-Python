print('='*10)
print('DESAFIO 050 - Soma números pares')
print('='*10,'\n')

soma = 0

for i in range(1,7):
    n=int(input('Digite um número inteiro: '))
    if n % 2 ==0:
        soma+=n
print(f'Soma = {soma}')