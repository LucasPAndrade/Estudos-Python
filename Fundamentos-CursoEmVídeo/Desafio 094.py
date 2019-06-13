print('=' * 10)
print('DESAFIO 094 - Dados Pessoas')
print('=' * 10, '\n')


pessoa = dict()
grupo = list()
médiaidade = soma = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).title()
    pessoa['Sexo'] = str(input('Sexo [F/M]: ')).upper()[0] #Maiúscula e primeiro caractere caso pessoa digite palavra completa
    while pessoa['Sexo'] not in 'FM':
        pessoa['Sexo'] = str(input('Opção inválida. Digite F para feminino ou M para masculino: ')).upper()[0]
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    grupo.append(pessoa.copy())
    r = str(input('Continuar? [S/N] '))
    if r in 'nN':
        break

print('='*20)
print(f'{"DADOS":^20}')
print('='*20)
print(grupo)

#Número de pessoas cadastradas.
print(f'- {len(grupo)} pessoas cadastradas.')

#Média de idade
médiaidade = soma / len(grupo)
print(f'- Média de idade = {médiaidade:.2f} anos.')

#Lista com mulheres
print('- As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=' ')

#Pessoas acima da média de idade:
print(f'\n- Lista de pessoas com idade acima da média ({médiaidade:.2f} anos):')

for p in grupo:
    if p['Idade'] >= médiaidade:
        for k, v in p.items():
            print(f'{k} = {v}', end=' | ')
        print()