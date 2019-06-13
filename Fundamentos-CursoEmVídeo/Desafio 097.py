print('=' * 10)
print('DESAFIO 097 - Função escreva')
print('=' * 10, '\n')

def escreva(msg):
    n = len(msg)
    print('~' * (n + 2))
    print(f' {msg}')
    print('~' * (n + 2))

t = str(input('Digite uma mensagem: '))
escreva(t)