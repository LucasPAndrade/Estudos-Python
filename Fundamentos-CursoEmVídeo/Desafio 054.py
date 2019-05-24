from datetime import date

print('='*10)
print('DESAFIO 054 - Checar se possui mais de 18 anos')
print('='*10,'\n')

maior=0
menor=0

for i in range(0,7):
    ano=int(input(f'Qual o ano de nascimento da pessoa {i+1}? '))
    idade=date.today().year-ano
    if idade >= 21:
        maior+=1
    else:
        menor+=1

print(f'Maior de 21 anos: {maior}.\nMenor de 21 anos: {menor}.')