print('=' * 10)
print('DESAFIO 080 - Lista crescente sem sort')
print('=' * 10, '\n')

#Solução CV
lista = []
for c in range(0,5):
    n = int(input(f'Digite o valor da posição {c+1}: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Primeiro valor adicionado à lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos+1}.')
                break
            pos += 1
print(lista)