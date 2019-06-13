print('=' * 10)
print('DESAFIO 092 - Aposentadoria')
print('=' * 10, '\n')

from datetime import date

pessoa = dict()

pessoa['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
pessoa['Idade'] = date.today().year - nascimento
pessoa['CTPS'] = int(input('Nº CTPS: '))
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))

print('-' * 20)
print(f'{"DADOS":^20}')
print('-' * 20)

for k, v in pessoa.items():
    print(f'{k}: {v}')

tempotrabalho = date.today().year - pessoa['Contratação']
if tempotrabalho < 35:
    print(f'Pessoa vai se aposentar em {35 - tempotrabalho} anos, quando tiver {pessoa["Idade"] + 35 - tempotrabalho} anos de idade.')
else:
    print('Já pode se aposentar!')
