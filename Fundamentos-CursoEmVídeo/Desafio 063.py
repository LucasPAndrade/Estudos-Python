print('='*10)
print('DESAFIO 063 - Sequência de Fibonacci')
print('='*10,'\n')

n=int(input('Digite quantos números da Sequência de Fibonacci você deseja ver: '))
while n < 3:
    n=int(input('Número deve ser maior que 3. Digite novamente: '))

lista=[1,1]
i = 2
while i <= n-1:
    lista.append(lista[i-2]+lista[i-1])
    i += 1
print(lista)


#Solução Curso em Vídeo
n = int(input('Digite quantos números da Sequência de Fibonacci você deseja ver: '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~'*30)