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
      print('em processo para abertura de  pdf ')#em processo
    elif op == 0:
      print('Retornado ao menu principal')
      break
    else:
      print('erro')