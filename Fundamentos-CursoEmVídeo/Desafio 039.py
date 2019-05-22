from datetime import date

print('='*10)
print('DESAFIO 039 - Alistamento')
print('='*10,'\n')

ano=int(input('Qual o seu ano de nascimento? '))
dif=date.today().year - ano-18

if dif ==0:
    print('É hora de se alistar ao serviço militar obrigatório!')
elif dif > 0:
    print(f'Deveria ter se alistado há {dif} ano(s).')
else:
    print(f'Vai se alistar em {-dif} ano(s).')