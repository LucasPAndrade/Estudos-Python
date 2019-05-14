print('===== DESAFIO 011 =====')

a=float(input('Qual a altura da parede, em metros? '))
l=float(input(('Qual a largura da parede, em metros? ')))

área=a*l
lt=área/2

print(f'Para pintar sua parede de {área}m² de área você precisará de {lt:.0f} litros de tinta.')