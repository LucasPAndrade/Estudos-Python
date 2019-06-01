print('='*10)
print('DESAFIO 061 - Progressão aritmética (versão "While")')
print('='*10,'\n')

#Solução Curso em Vídeo
p=int(input('Primeiro termo: '))
r=int(input('Razão: '))
termo = p
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += r
    cont += 1
print('FIM')