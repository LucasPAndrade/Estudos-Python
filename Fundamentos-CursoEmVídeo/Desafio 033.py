print('===== DESAFIO 033 =====\n')

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

#Verificando número menor
menor=n1 #para resumir linhas de código, assumo que o menor inicialmente é alguma das variáveis
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3

#Verificar número maior
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3

print(f'Maior número:{maior}\nMenor número: {menor}')