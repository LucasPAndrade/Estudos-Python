print('===== DESAFIO 026 =====\n')

texto=input('Digite um texto qualquer: ').lower()

print(f'Letra "a" aparece {texto.count("a")} vezes.')
print(f'Letra "a" aparece pela primeira vez na posição {texto.find("a")+1}.')
print(f'Letra "a" aparece pela primeira vez na posição {texto.rfind("a")+1}.')