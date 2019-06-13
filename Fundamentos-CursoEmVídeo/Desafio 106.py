print('=' * 10)
print('DESAFIO 106 - Mini sistema de ajuda PyHELP')
print('=' * 10, '\n')

from time import sleep

cores = {'padrão': '\033[m',
         'bg_amarelo': '\033[0;30;43m',
         'bg_vermelho': '\033[0;30;41m',
         'bg_azul': '\033[0;30;44m',
         'bg_branco': '\033[7;30m'}


def ajuda(t):
    destaque(f'Acessando o manual do comando \'{r}\'', cores['bg_azul'], True)
    sleep(2)
    print(cores['bg_branco'],end='')
    help(t)
    print(cores['bg_branco'])
    sleep(1)

def destaque(msg='', cor=cores['padrão'], sep=False):
    nsep = len(msg) + 4
    print(cor, end='')
    if sep: print(f'~' * nsep)
    print(f'  {msg}')
    if sep: print(f'~' * nsep)
    print(cores['padrão'], end='')


while True:
    destaque('SISTEMA DE AJUDA PyHELP', cores['bg_amarelo'], True)
    r = str(input('\033[mFunção ou Biblioteca > '))
    if r.lower() == 'fim':
        break
    ajuda(r)

destaque('Até logo!', cores['bg_vermelho'], True)
