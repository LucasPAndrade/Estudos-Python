print('=' * 10)
print('DESAFIO 104 - Validação de input')
print('=' * 10, '\n')

def leiaInt(msg):
    n = str(input(msg))
    while not n.isnumeric():
        print('\033[0;31mERRO! Valor digitado não é numérico! Digite um número inteiro!!\033[m')
        n = str(input(msg))
    n = int(n)
    return n

#Programa principal
r = leiaInt('Digite um valor: ')
print(f'Você digitou o valor {r}.')


