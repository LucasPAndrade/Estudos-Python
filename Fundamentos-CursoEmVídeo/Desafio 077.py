print('=' * 10)
print('DESAFIO 077 - Vogais em palavras')
print('=' * 10, '\n')

lista = 'flavio','juca','garrafa', 'girassol', 'porto'

for palavra in lista:
    print(f'Na palavra {palavra.upper()} temos as seguintes vogais: ',end='')
    if 'a' in palavra: print('a',end=' ')
    if 'e' in palavra: print('e', end=' ')
    if 'i' in palavra: print('i', end=' ')
    if 'o' in palavra: print('o', end=' ')
    if 'u' in palavra: print('u', end=' ')
    print('')

#Solução CV
for p in lista:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')