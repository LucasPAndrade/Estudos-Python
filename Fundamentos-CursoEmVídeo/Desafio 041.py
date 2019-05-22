from datetime import date

print('='*10)
print('DESAFIO 041 - Categoria por idade')
print('='*10,'\n')

ano=int(input('Digite ano de nascimento do atleta: '))
idade=date.today().year-ano

print(f'Idade: {idade} anos.')
if idade <=9:
    print('Categoria MIRIM, até 9 anos.')
elif idade <=14:
    print('Categoria INFANTIL, até 14 anos.')
elif idade <=19:
    print('Categoria JÚNIOR, até 19 anos.')
elif idade <=20:
    print('Categoria SÊNIOR, até 20 anos.')
else:
    print('Categoria MASTER, acima de 20 anos.')