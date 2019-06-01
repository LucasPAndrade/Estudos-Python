print('=' * 10)
print('DESAFIO 073 - Classificação de times de futebol do Brasileirão')
print('=' * 10, '\n')

classificação = 'Corinthians', 'Grêmio', 'Vasco', 'Chapecoense', 'Palmeiras', 'Santos', 'São Paulo', 'Portuguesa', 'Flamengo', 'Fluminense'

print(f'Primeiros 5 times: {classificação[:5]}.')
print(f'Últimos 4 times: {classificação[len(classificação)-4:]}.')
print(f'Times em ordem alfabética: {sorted(classificação)}.')
print(f'Chapecoense está na {classificação.index("Chapecoense")+1}ª posição.')