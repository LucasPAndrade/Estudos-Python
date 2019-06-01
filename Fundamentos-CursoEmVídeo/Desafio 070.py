print('=' * 10)
print('DESAFIO 070 - Nome e preço de produtos')
print('=' * 10, '\n')

soma = maior_1k = preço_barato = 0
n = 1
while True:
    produto = str(input('Nome produto: '))
    preço = float(input('Preço: '))

    soma += preço
    if preço > 1000:
        maior_1k += 1
    if n == 1:
        nomebarato = produto
        preço_barato = preço
    elif preço < preço_barato:
        nomebarato = produto
        preço_barato = preço

    n += 1

    continuar = str(input('Deseja continuar (S / N)? '))
    while continuar not in 'sSnN':
        continuar = str(input('Deseja continuar? Digite S para sim e N para não: '))
    if continuar in 'nN': break

print(f'{n} produto(s) cadastrado(s), valor total = R$ {soma:.2f}.')
print(f'{maior_1k} produto(s) tem valor acima de R$ 1.000,00.')
print(f'{nomebarato} é o produto mais barato (R$ {preço_barato:.2f}).')