print('Bem vindo a Lanchonete de Sheila Hui Yi Chiu RU:4412400')
print('*~~~~~~~~~~~~~~ Cardápio ~~~~~~~~~~~~~~~~~*')  # Descrição dos códigos,produtos e valores oferecidos.
print('|Código|        Descrição         |Valor $|')
print('|  100   |    Cachorro-Quente     |  9,00 |')
print('|  101   |  Cachorro-Quente Duplo | 11,00 |')
print('|  102   |       X - Egg          | 12,00 |')
print('|  103   |       X - Salada       | 13,00 |')
print('|  104   |       X - Bacon        | 14,00 |')
print('|  105   |       X - Tudo         | 17,00 |')
print('|  200   |   Refrigerante Lata    |  5,00 |')
print('|  201   |      Chá Gelado        |  4,00 |')

acumulador = 0  #Acumulador dos valores dos pedidos.

while True: #Início do laço
    codigo = input('Digite o código desejado:')
    if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201':  #Dei uma quebra de linha pra não ficar muito extenso.
        print('Código inválido!')  #Comando caso digite um código inválido
        continue  #Comando para perguntar novamente o usuário o código do pedido

    if codigo == '100':
        valor = 9  #Criei uma variável para printar na tela no momento do pedido
        print('Você pediu um Cachorro-Quente no valor de {:.2f}.'.format(valor))
        acumulador += 9

    elif codigo == '101':
        pedido = 11
        print('Você pediu um Cachorro-Quente Duplo no valor de {:.2f}.'.format(pedido))
        acumulador += 11

    elif codigo == '102':
        pedido = 12
        print('Você pediu um X-Egg no valor de {:.2f}.'.format(pedido))
        acumulador += 12

    elif codigo == '103':
        pedido = 13
        print('Você pediu um X-Salada no valor de {:.2f}.'.format(pedido))
        acumulador += 13

    elif codigo == '104':
        pedido = 14
        print('Você pediu um X-Bacon no valor de {:.2f}.'.format(pedido))
        acumulador += 14

    elif codigo == '105':
        pedido = 17
        print('Você pediu um X-Tudo no valor de {:.2f}.'.format(pedido))
        acumulador += 17

    elif codigo == '200':
        pedido = 5
        print('Você pediu um Refrigerante Lata no valor de {:.2f}.'.format(pedido))
        acumulador += 5

    elif codigo == '201':
        pedido = 4
        print('Você pediu um Refrigerante Lata no valor de {:.2f}.'.format(pedido))
        acumulador += 4

    pedir_mais = input('Deseja pedir mais alguma coisa?:\n 1 - Sim \n 0 - Não\n>>')  #Variável para perguntar ao usuário se vai pedir mais
    if pedir_mais == '1':
        continue

    else:
        print('O valor total a ser pago é:R${:.2f}'.format(acumulador))
        break  #Fim do laço e do programa
