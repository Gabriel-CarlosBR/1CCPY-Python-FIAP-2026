# Imagina... um sistema q recolha a escolha de um usuario
#escola_usuario
# se
# 0 --> sair do programa
# 1 --> entrar no programa
# ----- erro!
from queue import PriorityQueue

escolha_usuario = 0

match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("entrar no programa")
    case _:
        print("erro")