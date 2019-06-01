print('=' * 10)
print('DESAFIO 084 - Programa de nome e peso')
print('=' * 10, '\n')

pessoas = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Continuar? [S/N]')).lower()
    while r not in 'nNsS':
        r = str(input('Opção inválida... Digite S para continuar ou N para sair: ')).lower()

    if r == 'n': break

print(f'{len(pessoas)} pessoas cadastradas.')

maiorp = menorp = 0
listamaior = list()
listamenor = list()

for i,p in enumerate(pessoas):
    if i == 0:
        maiorp = menorp = p[1]
    elif p[1] >= maiorp:
        listamaior.append(p[0])
        maiorp = p[1]
    elif p[1] <= menorp:
        listamenor.append(p[0])
        menorp = p[1]

print(f'Maior peso foi de {maiorp}. Peso de {listamaior}.')
print(f'Menor peso foi de {menorp}. Peso de {listamenor}.')

#Solução CV
pessoas = list()
temp = list()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai: mai = temp[1]
        if temp[1] < men: men = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    r = str(input('Continuar? [S/N]'))
    if r in 'nN':
        break

print('-=' * 30)
print(f'O maior peso foi de {mai}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]} ',end='')
print()
print(f'O menor peso foi de {men}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]} ',end='')