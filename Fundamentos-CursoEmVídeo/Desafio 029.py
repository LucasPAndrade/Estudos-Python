print('===== DESAFIO 029 =====\n')

v=int(input('Qual a velocidade do carro, em km/h? '))
if v>80:
    print(f'Velocidade permitida é 80 km/h e a velocidade informada foi {v} km/h!')
    print(f'Multa a ser aplicada = R$ {(v-80)*7:.2f} (R$ 7.00 por cada km excedido).')
else:
    print('Velocidade informada está de acordo com o permitido.')