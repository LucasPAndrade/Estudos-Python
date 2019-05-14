print('===== DESAFIO 034 =====\n')

salário=float(input('Digite o seu salário para cálculo do aumento: '))

aumento=.10
if salário <= 1250:
    aumento=.15

print(f'Para o salário informado (R$ {salário:.2f}), o aumento é de {aumento*100:.0f}%, ou seja, o novo salário é de R$ {salário*(1+aumento):.2f} (aumento de R$ {salário*aumento:.2f}).')