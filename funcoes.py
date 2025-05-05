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
def calcula_pontos_regra_simples (rolados):

    resposta = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for numero in rolados:
        resposta[numero] += numero
    
    return resposta
##########################################
def calcula_pontos_soma (rolados):

    soma = 0

    for num in rolados:
        soma += num
    return soma
########################################