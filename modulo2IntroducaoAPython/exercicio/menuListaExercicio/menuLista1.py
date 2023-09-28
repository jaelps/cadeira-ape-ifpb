from modulo2IntroducaoAPython.exercicio.resposta.respostaLista1 import ex01, ex02, ex03, ex04, ex05, ex06, ex07, ex08


def m_rA():
  print('''
  =========[ Resposta Lista 1 ]===========
  ||                                    ||
  ||    1. Exercicio 1                  ||
  ||    2. Exercicio 2                  ||
  ||    3. Exercicio 3                  ||
  ||    4. Exercicio 4                  ||
  ||    5. Exercicio 5                  ||
  ||    6. Exercicio 6                  ||
  ||    7. Exercicio 7                  ||
  ||    8. Exercicio 8                  ||
  ||    0. Retornar menu inicial        ||
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
    elif op == 7:
      modulo = ex07()
    elif op == 8:
      modulo = ex08()
    elif op == 0:
      print('Retornado ao menu principal')
      break
    else:
      print('erro')
