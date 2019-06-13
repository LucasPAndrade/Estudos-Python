print('=' * 10)
print('DESAFIO 099 - Função maior')
print('=' * 10, '\n')


def maior(* valores):
    mai = 0
    for v in valores:
        if v > mai:
            mai = v
    print(f'{len(valores)} números informados ao todo {valores}.\nMaior número é {mai}.')

maior(1,6,2,0,5,1,4)