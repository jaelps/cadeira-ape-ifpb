from modulo_2_Introdução_a_Python.exercicio.menu_lista_exercicio.menu_lista1 import m_r_list1

from modulo_2_Introdução_a_Python.exercicio.menu_lista_exercicio.menu_lista2 import m_r_lista2

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
      print('em processo')
    elif op == 2:
      print('em processo')
    elif op == 3:
      print('em processo')
    elif op == 4:
      print('em processo')
    elif op == 5:
      exercicio_1 = m_r_list1()
      return exercicio_1
    elif op == 6:
      exercicio_2 = m_r_lista2()
      return exercicio_2
    elif op == 0:
      print('Retornado ao menu principal')
      break
    else:
      print('erro')