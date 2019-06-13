print('=' * 10)
print('DESAFIO 090 - Dicionário Aluno')
print('=' * 10, '\n')

aluno = {}
turma = []

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))
if aluno['Média'] < 6:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'
turma.append(aluno.copy())

for a in turma:
    for k,v in a.items():
        print(f'{k} é igual a {v}')
