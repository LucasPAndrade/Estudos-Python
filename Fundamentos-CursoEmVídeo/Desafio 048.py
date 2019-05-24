print('='*10)
print('DESAFIO 048 - Soma ímpares múltiplos 3 entre 1 e 500')
print('='*10,'\n')

soma=0
for i in range(1,501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
print(f'Soma = {soma}')


#Solução Curso em Vídeo

soma=0
cont=0
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma de todos os {cont} valores solicitados é {soma}.')