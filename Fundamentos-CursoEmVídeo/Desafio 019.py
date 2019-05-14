import random
print('===== DESAFIO 019 =====\n')

n1=input('Nome do primeiro aluno: ')
n2=input('Nome do segundo aluno: ')
n3=input('Nome do terceiro aluno: ')
n4=input('Nome do quarto aluno: ')

print(f'ALUNO SORTEADO: {random.choices((n1,n2,n3,n4))}!')


#resolução
lista=[n1,n2,n3,n4]
print(f'ALUNO SORTEADO: {random.choice(lista)}!')
