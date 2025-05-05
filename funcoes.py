import random


def rolar_dados(n):
    rolados = []

    for i in range(n):

        n_randomico = random.randint(1,6)
        rolados.append(n_randomico)

    return rolados
