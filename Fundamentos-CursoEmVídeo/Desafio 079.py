print('=' * 10)
print('DESAFIO 079 - Valores únicos em lista')
print('=' * 10, '\n')

lista = []

while True:
    n=int(input('Digite um valor: '))

    if n in lista:
        print('Valor duplicado, não foi adicionar...')
    else:
        lista.append(n)
        print('Valor adicionado.')

    pergunta = str(input('Quer continuar? [S/N]'))
    while pergunta not in 'sSnN':
        pergunta = str(input('Opção inválida... Quer continuar? [S/N]'))

    if pergunta in 'nN':
        break

lista.sort()
print(f'Você digitou os valores {lista}.')