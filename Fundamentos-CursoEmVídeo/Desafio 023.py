print('===== DESAFIO 023 =====\n')

n=int(input('Digite um número inteiro entre 0 e 9999: '))
strN=str(n)
m='-'
c='-'
d='-'
u='-'

if len(strN) == 4:
    m=strN[0]
    c=strN[1]
    d=strN[2]
    u=strN[3]
elif len(strN) == 3:
    c = strN[0]
    d = strN[1]
    u = strN[2]
elif len(strN) == 2:
    d = strN[0]
    u = strN[1]
else:
    u=strN

print(f"""Milhar: {m}
Centena: {c}
Dezena: {d}
Unidade: {u}""")

#SOLUÇÃO MATEMÁTICA CURSO EM VÍDEO
m= n // 1000 % 10
c= n // 100 % 10
d= n // 10 % 10
u= n // 1 % 10

print(f"""\n\nMilhar: {m}
Centena: {c}
Dezena: {d}
Unidade: {u}""")
