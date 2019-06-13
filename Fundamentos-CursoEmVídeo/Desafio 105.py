print('=' * 10)
print('DESAFIO 105 - Notas')
print('=' * 10, '\n')

def notas(*n, sit=False):
    """
    Análise de notas e situações de alunos.
    :param n: Uma ou mais notas.
    :param sit: (opcional), indica se deve ou não adicionar situação no retorno.
    :return: dicionário com informações sobre situação da turma.
    """

    média = sum(n)/len(n)
    aluno = {'total' : len(n),
             'maior' : max(n),
             'menor' : min(n),
             'média' : média}

    if sit:
        if média < 6:
            aluno['situação'] = 'Ruim'
        elif 6 <= média < 8:
            aluno['situação'] = 'Média'
        else:
            aluno['situação'] = 'Boa'
    return aluno

resp = notas(9,8,3,9,6, sit=True)
print(resp)