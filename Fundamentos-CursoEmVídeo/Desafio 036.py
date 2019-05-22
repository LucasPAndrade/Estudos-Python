print('='*10)
print('DESAFIO 036 - Aprovar Empréstimo')
print('='*10)

print('Para obter empréstimo bancário para comprar uma casa, informe os dados abaixo:')
valorcasa=float(input('Qual o valor da casa, em reais? '))
salário=float(input('Qual o salário mensal do comprador? '))
tempo=int(input('Em quantos anos o empréstimo será pago? '))
parcela=valorcasa/(tempo*12)

print('Você está apto a solicitar empréstimo!' if parcela<salário*.3 else 'Desculpe, mas a parcela corresponde a mais de 30% do seu salário. Empréstimo negado.')

if parcela<salário*.3:
    print('Você está apto a solicitar empréstimo!')
else:
    print(f'Desculpe, mas a parcela (R$ {parcela:.2f}) corresponde a mais de 30% do seu salário. Empréstimo negado.')