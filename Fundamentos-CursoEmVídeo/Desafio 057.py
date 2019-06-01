print('='*10)
print('DESAFIO 057 - Checagem digitação')
print('='*10,'\n')

sexo=str(input('Digite o sexo da pessoa (M ou F): ')).strip()
while sexo not in 'm M f F':
    sexo=str(input('Inválido, tente novamente! Digite o sexo da pessoa (M ou F): ')).strip()

print('Sexo Masculino' if sexo in 'mM' else 'Sexo Feminino')