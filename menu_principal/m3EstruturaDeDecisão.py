def m3():
  print('''
  ===========================================
  ||  1. Slide Estrutura de Decisão        ||
  ||  2. Exercico Estrutura de Decisão     ||
  ||  3. Exercico Complementar             ||
  ||  4. Pratica Exercicio 1               ||
  ||  5. Pratica Exercicio 2               ||
  ||  0. Retornar menu anterior            ||
  ===========================================
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