print('='*10)
print('DESAFIO 043 - Analisando IMC')
print('='*10,'\n')

peso=float(input('Qual o seu peso, em kg? '))
altura=float(input('Qual a sua altura, em metros? '))
imc=peso/(altura**2)

print(f'IMC = {imc:.2f}')
if imc <18.5:
    print('Você está abaixo do peso.')
elif imc <25:
    print('Peso ideal.')
#elif 18.5 <= imc < 25:
#    print('Peso ideal.')
elif imc <30:
    print('Sobrepeso.')
elif imc <40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')