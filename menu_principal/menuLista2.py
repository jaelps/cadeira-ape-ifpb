from lista2 import ex01,ex02,ex03,ex04,ex05,ex06

def menu_2():
  print('''
  ===================================
  ||  1. Testar 1º item da lista   ||
  ||  2. Testar 2º item da lista   ||
  ||  3. Testar 2º item da lista   ||
  ||  4. Testar 2º item da lista   ||
  ||  5. Testar 2º item da lista   ||
  ||  6. Testar 2º item da lista   ||
  ||  0. Retornar menu anterior    ||
  ===================================
  ''')

  while True:
    op = int(input('Escolha opção da lista: '))

    if op == 1:
      exercicio_1 = ex01()
    elif op == 2:
      exercicio_2 = ex02()
    elif op == 3:
      exercicio_3 = ex03()
    elif op == 4:
      exercicio_4 = ex04()
    elif op == 5:
      exercicio_5 = ex05()
    elif op == 6:
      exercicio_6 = ex06()
    elif op == 0:
      print('Retornado ao menu principal')
      break
    else:
      print('erro')