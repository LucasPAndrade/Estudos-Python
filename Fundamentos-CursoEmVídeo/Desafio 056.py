print('='*10)
print('DESAFIO 056 - Perguntas sobre dados de 4 pessoas')
print('='*10,'\n')

somaidade=0
maxidade=0 #idade do homem mais velho
contm=0 #número de mulheres com menos de 20 anos

for i in range(0,4):
    print(f'--- {i+1}ª PESSOA ---')
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('Sexo (F ou M): ')).lower()

    somaidade += idade

    if sexo=='m' and idade>maxidade:
        nomehomemvelho=nome
        idadehomemvelho=idade
    if sexo=='f' and idade <20:
        contm+=1

print(f'Média de idade do grupo = {somaidade/4:.0f} anos.')
print(f'Homem mais velho = {nomehomemvelho} ({idadehomemvelho} anos).')
print(f'{contm} mulheres com menos de 20 anos.')