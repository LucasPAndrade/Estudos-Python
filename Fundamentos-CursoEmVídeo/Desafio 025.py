print('===== DESAFIO 025 =====\n')

nome=input('Digite o seu nome completo: ').lower()
check=0
check=nome.find('silva')

print('Nome contém Silva') if check > 0 else print('Nome não contém Silva')

#SOLUÇÃO CURSO EM VÍDEO
print('Seu nome tem Silva? {}'.format('silva' in nome))