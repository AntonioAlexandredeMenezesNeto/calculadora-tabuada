print('Ola, seja bem vindo.')
mensagem = input('Se desejar fazer um calculo escreva calcular, '
                 'se desejar saber uma tabuada escreva tabuada: ')

separador = mensagem
if separador == 'calcular':
    mensagemdois = str(input('digite um calculo: '))
    calculador = mensagemdois
    resultado = eval(calculador)
    print('o resultado do seu calculo é:', resultado)
elif separador == 'tabuada':
    tabu = int(input('Tabuada de: '))
    nnn = 0
    print('tabuada de {}'.format(tabu))
    while (nnn <= 10):
        print('{0} X {1} = {2}'.format(nnn, tabu, (nnn * tabu)))
        nnn = nnn + 1
else:
    raise ValueError('escreva calcular ou tabuada')