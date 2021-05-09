from lib.arquivo import *
from lib.comandos import *

lista_de_comandos = list()
comando = list()
while True:
    op = menu()
    if op == 1:
        comando.append(op)
        comando.append(input('Qual tecla? '))
        lista_de_comandos.append(comando.copy())
        comando.clear()
    elif op == 2:
        comando.append(op)
        comando.append(input('Qual texto? '))
        lista_de_comandos.append(comando.copy())
        comando.clear()
    elif op == 3:
        comando.append(op)
        comando.append(input('Qua o comando de teclado? separe com , as teclas '))
        lista_de_comandos.append(comando.copy())
        comando.clear()
    elif op == 4:
        break

executarScript(lista_de_comandos)