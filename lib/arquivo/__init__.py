def linha():
    print('linha dentro de arquivo')


def menu():
    print('Escolha a a opção:')
    print('''    1 - Pressionar uma tecla
    2 - Escrever algo
    3 - Precionar Teclas em conjunto
    4 - Finalizar o Script''')
    op = int(input('Digite a opção escolhida: '))
    return op
