print('='*10)
print('DESAFIO 042 - Analisando Triângulos')
print('='*10,'\n')

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('As retas informadas podem formar um triângulo.')
    if r1==r2 and r1==r3:
        print('Triângulo equilátero (todos lados iguais).')
    elif r1!=r2 and r1!=r3:
        print('Triângulo escaleno (todos lados diferentes).')
    else:
        print('Triângulo isósceles (dois lados iguais).')

else:
    print('As retas informadas NÃO podem formar um triângulo.')