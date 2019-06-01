print('='*10)
print('DESAFIO 064 - Soma de n elementos')
print('='*10,'\n')

n = soma = cont 0

while n != 999:
    n = int(input('Digite um número (999 se quiser sair): '))
    cont += 1
    if n != 999:
        soma += n
print(f'A soma dos {cont-1} números digitados é igual a {soma}.')
