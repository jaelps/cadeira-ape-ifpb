def m4():
  print('''
  ====================================================
  ||   1. Slide Estrutura de Repetição              ||
  ||   2. Exercico Estrutura de Repetição (for)     ||
  ||   3. Exercico Estrutura de Repetição (while)   ||
  ||   4. Pratica Exercicio For                     ||
  ||   5. Pratica Exercicio While                   ||
  ||   0. Retornar menu anterior                    ||
  ====================================================
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