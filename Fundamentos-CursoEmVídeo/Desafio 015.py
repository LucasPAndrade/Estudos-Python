print('===== DESAFIO 015 =====\n')

km = int(input('Quantos km rodou com o carro? '))
dias = int(input('Quantos dias o carro ficou alugado? '))

valorKm = km*0.15
valorDias = dias*60

print(f'=== ALUGUEL DE CARROS ===n\Carro alugado por {dias} dias, {km}km rodados.\nValor km = R$ {valorKm:.2f}\nValor tempo = R$ {valorDias:.2f}\nValor totoal a pagar = R$ {valorDias+valorKm:.2f}')