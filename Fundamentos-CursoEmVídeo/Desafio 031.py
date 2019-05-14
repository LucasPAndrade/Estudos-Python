print('===== DESAFIO 031 =====\n')

distância=int(input('Digite a distância da viagem em km: '))
if distância <= 200:
    custo=0.5
else:
    custo=0.45

print(f'Custo da viagem = R$ {distância*custo:.2f} (R$ {custo:.2f} por km).')