print('=' * 10)
print('DESAFIO 095 - Performance Jogador de Futebol (MELHORADO)')
print('=' * 10, '\n')

grupo = list()
jogador = dict()
aproveitamento = list()
total = gol = 0

#Início Coleta Dados
while True:
    jogador.clear()
    aproveitamento.clear()
    jogador['Nome'] = str(input('Nome do(a) jogador(a): '))
    partidas = int(input('Quantas partidas ele(a) jogou?'))
    for c in range(0,partidas):
        aproveitamento.append(int(input(f' - Quantos gols fez na partida {c+1}? ')))
    jogador['Gols'] = aproveitamento[:]
    jogador['Total'] = sum(aproveitamento)
    grupo.append(jogador.copy())

    r = str(input('Continuar? [S/N] '))
    if r in 'nN':
        break
#fim Coleta Dados

#Início Análise de Dados
print('-=' * 30)
print(f'ID ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
c = 1
'''
for j in grupo:
    #print(f'{i + 1:>3}{j["Nome"]:<20}{j["Gols"]:<22}{j["Total"]:<5}')
    #print(f'{c:>3}{j["Nome"]:<20}{j["Gols"]:<22}{j["Total"]:<5}')
    print(f'{c}     {j["Nome"]:<10}{j["Gols"]}{j["Total"]:>25}')
    c += 1
'''

#Solução CV
for k, v in enumerate(grupo):
    print(f'{k + 1:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
#fim Solução CV
print('-' * 40)

id = 0
while True:
    id = int(input('Deseja ver detalhe de algum jogador? Digite o número do ID [999 para SAIR]: '))
    if id == 999:
        break
    if len(grupo) < id:
        print('Opção inválida, tente novamente!')
    else:
        id -= 1
        print(f'O(A) jogador(a) {grupo[id]["Nome"]} jogou {len(grupo[id]["Gols"])} partidas.')
        for i, v in enumerate(grupo[id]["Gols"]):
            print(f'     => Na partida {i+1} fez {v} gol(s).')
        print(f'Total de {grupo[id]["Total"]} gol(s).')
        print('-' * 40)
#Fim Análise de Dados

print('\n\n<-- VOLTE SEMPRE -->')
