print('=' * 10)
print('DESAFIO 069 - Cadastro de pessoas')
print('=' * 10, '\n')

maior18 = homem = mulher20 = 0
n = 1
while True:
    print(F'\nCADASTRO PESSOA {n}')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite sexo (M / F): '))
    while sexo not in 'mMfF':
        sexo = str(input('Opção inválida. Digite o sexo (M ou F): '))

    if idade > 18:
        maior18 += 1
    if sexo in 'mM':
        homem += 1
    if idade < 20 and sexo in 'fF':
        mulher20 += 1
    n += 1

    continuar = str(input('Deseja cadastrar mais uma pessoa? S / N: '))
    while continuar not in 'sSnN':
        continuar = str(input('Opção inválida. Digite S para continuar cadastro ou N para encerrar programa: '))
    if continuar in 'nN': break

print(f'{n} pessoas cadastradas.')
print(f'{maior18} pessoas com idade acima de 18 anos.')
print(f'{homem} pessoas são do sexo masculino.')
print(f'{mulher20} mulheres tem menos de 20 anos.')
print('FIM PROGRAMA')
