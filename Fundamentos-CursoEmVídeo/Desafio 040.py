print('='*10)
print('DESAFIO 040 - Nota aluno')
print('='*10,'\n')

nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))
média=(nota1+nota2)/2

if média<5:
    print(f'Média abaixo de 5.0, REPROVADO! Média do aluno: {média:.2f}')
elif média>=7:
    print(f'Média acima de 7.0, APROVADO! Média do aluno: {média:.2f}')
else:
    print(f'Média entre 5.0 e 7.0, RECUPERAÇÃO! Média do aluno: {média:.2f}')