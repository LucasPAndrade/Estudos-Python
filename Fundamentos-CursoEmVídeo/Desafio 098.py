from time import sleep

print('=' * 10)
print('DESAFIO 098 - Função contador')
print('=' * 10, '\n')


def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if f > 0:
        f += 1
    if f < 0:
        f -= 1
    if (i > f and p > 0) or (i < f and p < 0):
        p *= -1
    sleep(1)
    for v in range(i, f, p):
        print(v, end=' ')
        sleep(.25)
    print('FIM!')
    print('=' * 20)


contador(1, 10, 1)
contador(10, 0, -2)
while True:
    início = int(input('Início: '))
    fim = int(input('Fim: '))
    while fim == início:
        fim = int(input('Fim não pode ser igual ao início. Digite outro valor para o fim: '))
    passo = int(input('Passo: '))
    while passo == 0:
        passo = 1
        print('Passo não pode ser igual a 0, por isso vamos considerar passo igual a 1.')
    contador(início, fim, passo)

    r = str(input('Continuar? [S/N]'))
    if r in 'nN':
        break
print('----- FIM PROGRAMA -----')
