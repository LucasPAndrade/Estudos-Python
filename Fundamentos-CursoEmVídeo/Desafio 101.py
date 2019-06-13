print('=' * 10)
print('DESAFIO 101 - Voto')
print('=' * 10, '\n')

def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: Voto proibido'
    elif idade < 18 or idade >= 65:
        return f'Com {idade} anos: Voto opcional'
    else:
        return f'Com {idade} anos: Voto obrigatório'

anoN = int(input('Ano de nascimento: '))
print(voto(anoN))