print('='*10)
print('DESAFIO 066 - Soma n números')
print('='*10,'\n')

n = s = cont = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999: break
    s += n
    cont += 1
print(f'A soma dos {cont} números digitados é {s}.')