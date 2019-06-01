print('='*10)
print('DESAFIO 065 - Soma, média, maior e menor de n elementos')
print('='*10,'\n')

n = 0
soma = 0
cont = 0
sair = 'N'
max = 0
min = 0

while sair in 'n N':
    while n != 999:
        n = int(input('Digite um número (999 se quiser sair): '))
        if n != 999:
            cont += 1
            soma += n
            if cont == 1: max = min = n #primeiro laço
            else:
                if n > max: max = n
                if n < min: min = n
    print(f'A média dos valores é {soma / cont}. \nMaior valor: {max}.\nMenor valor: {min}.')
    sair = str(input('Deseja realmente sair do programa (S / N): '))
    n = 0
print('FIM DO PROGRAMA')