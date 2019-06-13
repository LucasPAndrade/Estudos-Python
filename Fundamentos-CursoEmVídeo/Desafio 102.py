print('=' * 10)
print('DESAFIO 102 - Fatorial v.3')
print('=' * 10, '\n')


def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    :param n: Número a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo.
    :return: Valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


nf = int(input('Digite um valor: '))
r = str(input('Visualizar cálculo? [S/N]'))
if r in 'sS':
    ver = True
else:
    ver = False

print(fatorial(nf, ver))
help(fatorial)
