print('='*10)
print('DESAFIO 055 - Maior e menor peso')
print('='*10,'\n')

max=0
min=0
for i in range(0,5):
    peso=float(input('Qual o seu peso? '))
    if i == 0: #primeiro laço
        max=peso
        min=peso
    else:
        if peso>max:
            max=peso
        if peso<min: #sem a checagem de primeiro laço da linha 9, esse linha aqui ficaria "if min==0 or peso<min:"
            min=peso

print(f'Maior peso: {max}kg.\nMenor peso: {min}kg.')