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
def calcula_pontos_sequencia_baixa (rolados):

    lista_o = []

    for num in rolados:
        if num not in lista_o:
            lista_o.append(num)
    
    lista_o = sorted(lista_o)

    if len(lista_o)<4:
        return 0

    for i in range(len(lista_o) - 3):

        cond1 = lista_o[i+1] == lista_o[i] + 1 and lista_o[i+2] == lista_o[i] + 2 and lista_o[i+3] == lista_o[i] + 3
        
        if cond1:
            return 15
    
    return 0
##############################################
def calcula_pontos_sequencia_alta(lista):
    
    lista_o = []

    for num in lista:
        if num not in lista_o:
            lista_o.append(num)

    
    if len(lista_o)<5:
        return 0

    lista_o = sorted(lista_o)

    for i in range(len(lista_o)-1):
        proximo = lista_o[i] + 1
        if lista_o[i+1] != proximo:
            return 0
    return 30
##########################################
def calcula_pontos_full_house(rolados):

    lista_o = sorted(rolados)

    condição1 = lista_o[0] == lista_o[1] and lista_o[2] == lista_o[3] == lista_o[4] and lista_o[0] != lista_o[3]
    condiçao2 = lista_o[3] == lista_o[4] and lista_o[0] == lista_o[1] == lista_o[2] and lista_o[0] != lista_o[3]

    if condição1 or condiçao2:
        soma = 0 
        for n in lista_o:
            soma += n
        return soma
    else:
        return 0 
    ########################################