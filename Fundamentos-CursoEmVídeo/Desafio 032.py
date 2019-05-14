from datetime import date
print('===== DESAFIO 032 =====\n')

ano=int(input('Digite o ano que quer avaliar se é bissexto. Digite 0 para analisar ano atual: '))

if ano==0:
    ano=date.today().year

if ano%4 == 0 and ano%100 !=0 or ano%400 ==0:
    print(f'Ano {ano} é bissexto!')
else:
    print(f'Ano {ano} não é bissexto.')