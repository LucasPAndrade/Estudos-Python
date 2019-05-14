import math
print('===== DESAFIO 017 =====\n')

opo=float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))

print(f'Hipotenusa = {math.hypot(opo,adj):.5f}.')