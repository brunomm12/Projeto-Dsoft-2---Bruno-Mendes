import random


def rolar_dados(n):
    rolados = []

    for i in range(n):

        n_randomico = random.randint(1,6)
        rolados.append(n_randomico)

    return rolados
#######################################
def guardar_dado(rol,guard,ind):

    valor = rol[ind]
    guard.append(valor)

    del(rol[ind])

    return [rol, guard]
########################################
def remover_dado(rol,guard,ind):
    valor = guard[ind]
    rol.append(valor)

    del(guard[ind])

    return [rol, guard]
#########################################