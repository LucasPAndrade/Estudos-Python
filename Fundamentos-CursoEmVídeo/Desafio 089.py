print('=' * 10)
print('DESAFIO 089 - Sistema Notas de Alunos')
print('=' * 10, '\n')

boletim = []
aluno = []
notas = []
n1 = n2 = i = r = 0
while True:
    aluno.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    notas.append(n1)
    notas.append(n2)
    aluno.append(notas[:])
    notas.clear()
    aluno.append((n1+n2)/2)
    boletim.append(aluno[:])
    aluno.clear()
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'nN':
        break


print('='*30)
print(f'{"BOLETIM":^30}')
print('='*30)
print(f'{"#":<4}{"Aluno":<15}{"Média":>8}')

for i,aluno in enumerate(boletim):
    print(f'{i+1:<4}{aluno[0]:<15}{aluno[2]:>8}')

while True:
    r = int(input('\nDeseja exibir notas de qual aluno (#)? (999 para interromper): '))
    if r == 999:
        break
    r -= 1
    if r <= len(boletim):
        print(f'Nota do aluno {boletim[r][0]}: {boletim[r][1]}.')
print('<-- FIM DO PROGRAMA -->')

#Solução CV
'''
ficha = list()
while True:
    nome = str(input('Digite seu nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1,nota2], media])
    resp = str(input('Continuar? [S/N] '))
    if resp in 'nN':
        break

...

'''