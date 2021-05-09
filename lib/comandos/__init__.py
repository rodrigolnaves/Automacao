import pyautogui as pag


def linha():
    print('linha dentro de comandos')


def pegaPosicaoDoMouse():
    pos = str(pag.position()).replace("Point(x=", "").replace("y=", "").replace(")", "").split(', ')
    return pos


def executarScript(lista):
    x = 0
    pag.PAUSE = 2
    while x < len(lista):
        if lista[x][0] == 1:
            pag.press(lista[x][1])
            x += 1
        elif lista[x][0] == 2:
            pag.write(lista[x][1])
            x += 1
    pag.alert('FIM')
