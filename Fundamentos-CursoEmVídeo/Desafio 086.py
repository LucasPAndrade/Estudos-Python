print('=' * 10)
print('DESAFIO 086 - Matriz')
print('=' * 10, '\n')

#Solução1
print('SOLUÇÃO 1')
i = l = c = il = ic = 0
num = []
for i in range(0,9):
    num.append(int(input(f'Digite um valor para [{l},{c}]: ')))
    il += 1
    ic += 1
    c += 1
    if il % 3 == 0: l += 1
    if ic % 3 == 0: c = 0

print(num)
p = 1
for n in num:
    print(f'[{n:^5}]',end='')
    if p % 3 == 0:
        print()
    p += 1

print('FIM SOLUÇÃO 1')
print('-'*50)


#Solução 2
print('SOLUÇÃO 2')

i = l = c = 0
num = [[],[],[]]
for i in range(1,10):
    num[l].append(int(input(f'Digite um valor para [{l},{c}]: ')))
    if i % 3 == 0:
        l += 1
        c = 0
    c += 1

i = l = c = 0
for l in num:
    for c in l:
        print(f'[{c:^5}]',end='')
    print()

print('FIM SOLUÇÃO 2')
print('-'*50)


#Solução CV
print('Solução CV')

matriz =[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor em [{l},{c}]: '))

for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()