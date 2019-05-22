import random
from time import sleep

print('='*10)
print('DESAFIO 045 - Jokenpô')
print('='*10,'\n')

user=input('Você escolhe Pedra, Papel ou Tesoura? Digite sua escolha!').lower()
jogos=('pedra','papel','tesoura')
pc = random.choice(jogos)

print('Jogo do computador: ...')
sleep(2)
print(str(pc).capitalize())

if user==pc:
    print('Empate!')
elif user=='pedra':
    if pc=='papel':
        print('Computador venceu!')
    else:
        print('Usuário venceu!')
elif user=='papel':
    if pc=='pedra':
        print('Usuário venceu!')
    else:
        print('Computador venceu!')
elif user=='tesoura':
    if pc=='pedra':
        print('Computador venceu!')
    else:
        print('Usuário venceu!')