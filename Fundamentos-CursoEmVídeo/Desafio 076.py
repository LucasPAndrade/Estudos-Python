print('=' * 10)
print('DESAFIO 076 - Lista de preços')
print('=' * 10, '\n')

lista='Maçã',1.5,'Vassoura',5,'Escova de dente', .9, '1 kg de frango', 8, 'TV', 1300.50

print('-'*50)
print(f'{"LISTA DE PREÇOS":^50}')
print('-'*50)

for n,item in enumerate(lista):
    if n % 2 == 0:
        print(f'{item:.<30} R$ ', end='')
    else:
        print(f'{item:>10.2f}')

print('-'*50)