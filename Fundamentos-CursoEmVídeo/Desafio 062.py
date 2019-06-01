print('='*10)
print('DESAFIO 062 - Progressão aritmética (versão "While" melhorado)')
print('='*10,'\n')

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
q = 10
while q != 0:
    termo = p
    cont = 1
    while cont <= q:
        print(f'{termo} -> ', end='')
        termo += r
        cont += 1
    print('FIM')
    print('')
    q = int(input('Informe a quantidade de termos que deseja mostrar agora (digite 0 para sair do programa): '))
print('FIM PROGRAMA')