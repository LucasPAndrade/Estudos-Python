print('='*5,'DESAFIO 06','='*5)

n=int(input('Digite um número qualquer: '))
print('O número digitado foi {}.\n -- Dobro: {}\n -- Triplo: {}\n -- Raiz quadrada: {:.3f}'.format(n,n*2,n*3,n**(1/2)))

#Simplificação usando f no começo
print(f'O número digitado foi {n}.\n -- Dobro: {n*2}\n -- Triplo: {n*3}\n -- Raiz quadrada: {n**(1/2):.3f}')