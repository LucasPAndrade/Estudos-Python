print('=' * 10)
print('DESAFIO 096 - Função área')
print('=' * 10, '\n')


def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.1f} x {comp:.1f} é de {a:.1f}m².')


l = float(input('Largura do terreno, em metros: '))
c = float(input('Comprimento do terreno, em metros: '))
área(l, c)
