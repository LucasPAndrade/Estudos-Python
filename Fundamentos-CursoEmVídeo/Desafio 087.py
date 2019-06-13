print('=' * 10)
print('DESAFIO 087 - Matriz e análise')
print('=' * 10, '\n')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
n = somapares = somatc = maiorsegl = 0

for l in range(0,3):
    for c in range (0,3):
        n = int(input(f'Digite um valor em [{l},{c}]: '))
        matriz[l][c] = n
        if n % 2 == 0:
            somapares += n
        if c == 2:
            somatc += n
        if l == 1 and n >= maiorsegl:
            maiorsegl = n

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print()
print(f'Soma dos valores pares = {somapares}')
print(f'Soma valores 3ª coluna = {somatc}')
print(f'Maior valor 2ª liha = {maiorsegl}')