print('='*10)
print('DESAFIO 067 - Tabuada (versão 3)')
print('='*10,'\n')

c = 1

while True:
    n = int(input('Quer ver a tabuada de qual número (negativo ou zero para sair)? '))
    if n <= 0: break
    print('-'*30)

    while c <= 10:
        print(f'{n} x {c} = {n*c}')
        c += 1
    print('-' * 30)
print('\nFIM')

#Solução Curso em Vídeo
    #Guanabara usou estrutura FOR ao invés do while na linha 12.