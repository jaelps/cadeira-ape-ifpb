from modulo3EstruturaDeDecisao.exercicio.resposta.respostaLista2 import ex01, ex02, ex03, ex04, ex05, ex06


def m_rB():
  print('''
  ==========[ Resposta Lista 2]===========
  ||                                    ||
  ||    1. Exercicio 1                  ||
  ||    2. Exercicio 2                  ||
  ||    3. Exercicio 3                  ||
  ||    4. Exercicio 4                  ||
  ||    5. Exercicio 5                  ||
  ||    6. Exercicio 6                  ||
  ||    0. Retornar menu anterior       ||
  ||                                    ||
  ========================================
  ''')

  while True:
    op = int(input('Escolha opção da lista: '))

    if op == 1:
      modulo = ex01()
    elif op == 2:
      modulo = ex02()
    elif op == 3:
      modulo = ex03()
    elif op == 4:
      modulo = ex04()
    elif op == 5:
      modulo = ex05()
    elif op == 6:
      modulo = ex06()
    elif op == 0:
      print('Retornado ao menu principal')
      break
    else:
      print('erro')
