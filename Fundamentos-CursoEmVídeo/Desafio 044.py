print('='*10)
print('DESAFIO 044 - Pagamentos')
print('='*10,'\n')

preço=float(input('Qual o preço normal do produto, em reais? '))
print('OPÇÕES DE PAGAMENTO:'
      '\n[1] À vista dinheiro (10% de desconto)'
      '\n[2] À vista cartão (5% de desconto)'
      '\n[3] 2x no cartão (preço normal)'
      '\n[4] 3x ou mais no cartão (20% de juros)')
pgto=int(input('Qual sua opção? '))

fator=1
if pgto == 1:
    fator=0.9
elif pgto == 2:
    fator=0.95
elif pgto == 4:
    fator=1.2

print(f'Novo preço pela condição de pagamento selecionada = R$ {preço*fator:.2f}.')