from lista1 import ex01,ex02,ex03,ex04,ex05,ex06,ex07,ex08

def m1():
  print('''
  ========================================
  ||  1. Slide Conceitos Fundamentais   ||
  ||  0. Retornar menu anterior         ||
  ========================================
  ''')

  while True:
    op = int(input('Escolha opção da lista: '))

    if op == 1:
      exercicio_1 = ex01()
    elif op == 0:
      print('Retornado ao menu principal')
      break
    else:
      print('erro')