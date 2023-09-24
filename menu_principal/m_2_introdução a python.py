from lista2 import ex01,ex02,ex03,ex04,ex05,ex06

def m2():
  print('''
  ==========================================
  ||   1. Slide Introdução a Python       ||
  ||   2. Exercicio Introdução a Python   ||
  ||   3. Exercicio Complementar          ||
  ||   4. Pratica exercicio 1             ||
  ||   5. Pratica exercicio 2             ||
  ||   0. Retornar menu anterior          ||
  ==========================================
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