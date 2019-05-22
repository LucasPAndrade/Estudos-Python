print('='*10)
print('DESAFIO 037 - Conversão/base numérica')
print('='*10)

n=int(input('Digite um número inteiro: '))
print('''\nEscolha uma das bases numéricas para conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção=int(input('\nSua opção: '))

if opção==1:
    print(f'{n} convertido para BINÁRIO é {bin(n)[2:]} ({bin(n)}).')
elif opção==2:
    print(f'{n} convertido para OCTAL é {oct(n)[2:]} ({oct(n)}).')
elif opção==3:
    print(f'{n} convertido para HEXADECIMAL é {hex(n)[2:]} ({hex(n)}).')
else:
    print('Opção inválida, tente novamente.')