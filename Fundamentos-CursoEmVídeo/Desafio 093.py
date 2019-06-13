print('=' * 10)
print('DESAFIO 093 - Performance Jogador de Futebol')
print('=' * 10, '\n')

jogador = dict()
aproveitamento = list()
partidas = c = total = gol = 0

jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou?'))
for c in range(0,partidas):
    gol = int(input(f'Quantos gols fez na partida {c+1}? '))
    aproveitamento.append(gol)
    total += gol
jogador['Gols'] = aproveitamento
jogador['Total'] = total

print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, v in enumerate(aproveitamento):
    print(f'     => Na partida {i+1} fez {v} gol(s).')
print(f'Total de {total} gol(s).')