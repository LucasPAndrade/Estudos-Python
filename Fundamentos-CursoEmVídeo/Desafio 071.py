print('=' * 10)
print('DESAFIO 071 - Simulação Caixa Eletrônico')
print('=' * 10, '\n')

valor = int(input('Qual o valor a ser sacado? R$ '))

vcalc = c = v = d = u = 0

while vcalc < valor:
    if vcalc + 50 > valor: break
    vcalc += 50
    c += 1
while vcalc < valor:
    if vcalc + 20 > valor: break
    vcalc += 20
    v += 1
while vcalc < valor:
    if vcalc + 10 > valor: break
    vcalc += 10
    d += 1
while vcalc < valor:
    if vcalc + 1 > valor: break
    vcalc += 1
    u += 1

print(f'{c} notas de R$ 50')
print(f'{v} notas de R$ 20')
print(f'{d} notas de R$ 10')
print(f'{u} notas de R$ 1')


#Solução CV
    #Pensamento inverso ao meu: pega o total e vai subtraindo as cédulas.

total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd:.2f}.')
        if céd == 50: céd = 20
        elif céd == 20: céd = 10
        elif céd == 10: céd = 1
        totcéd = 0
        if total == 0: break
print('=' * 30)
print('Vole sempre! Programa encerrado.')