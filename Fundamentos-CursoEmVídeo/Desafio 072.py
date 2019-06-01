print('=' * 10)
print('DESAFIO 072 - Números por extenso')
print('=' * 10, '\n')

itens = ('um','dois','três', 'quatro', 'cinco', 'seis','sete','oito','nove','dez')
n = 0
check = False
while check == False:
    n=int(input('Digite um número inteiro entre 1 e 10: '))
    if n >= 1 and n <= 10:
        print(itens[n-1])
        check = True