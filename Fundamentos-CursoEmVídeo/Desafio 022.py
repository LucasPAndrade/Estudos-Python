print('===== DESAFIO 022 =====\n')
nome=input('Digite o seu nome completo: ')
nome=nome.capitalize()

print(nome.upper())
print(nome.lower())
print('Número de caracteres:',len(nome))
print('Número de caracteres (sem espaço):',len(nome.replace(' ',''))) #ou len(nome)-nome.count(' ')
print('Número de caracteres do primeiro nome:',len(nome.split()[0]))