print('='*10)
print('DESAFIO 053 - Identificando palíndromos')
print('='*10,'\n')

'''
Exemplos: apos a sopa, a sacada da casa
'''

texto=str(input('Digite um texto para identificar se é palíndromo: ')).strip()
if texto.lower() == texto.lower()[::-1]:
    print('Palíndromo!')
else:
    print('Não é palíndromo.')


#Solução Curso em Vídeo
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('Palíndromo.')
else:
    print('Não palíndromo.')