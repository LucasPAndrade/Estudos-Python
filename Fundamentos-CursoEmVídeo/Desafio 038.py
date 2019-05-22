print('='*10)
print('DESAFIO 038 - Comparação entre números')
print('='*10,'\n')

n1=float(input('Digite primeiro valor: '))
n2=float(input('Digite segundo valor:'))

if n1>n2:
    print(f'Primeiro valor ({n1}) é maior que o segundo valor ({n2}).')
elif n2>n1:
    print(f'Segundo valor ({n2}) é maior que o primeiro valor ({n1}).')
else:
    print(f'Ambos valores são iguais ({n1}, {n2}).')