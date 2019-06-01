print('=' * 10)
print('DESAFIO 083 - Validando expressão matemática')
print('=' * 10, '\n')

abrindo = fechando = 0
texto = str(input('Digite a expressão: '))
for p in texto:
    if p == '(':
        abrindo +=1
    elif p == ')':
        fechando +=1

if abrindo == fechando:
    print('''Expressão correta!
    Quer dizer, pelo menoso número de parênteses abrindo é igual ao número de parênteses fechando...''')
else:
    print('Expresão incorreta!')
