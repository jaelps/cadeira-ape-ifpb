from modulo2IntroducaoAPython.exercicio.menuListaExercicio.menuLista1 import m_rA

from modulo2IntroducaoAPython.exercicio.menuListaExercicio.menuLista2 import m_rB


def m2():
  print('''
  ===============[ Modulo 2 ]===============
  ||                                      ||
  ||   1. Slide Introdução a Python       ||
  ||   2. Exercicio Introdução a Python   ||
  ||   3. Exercicio Complementar          ||
  ||   4. Resposta Lista Exercicio 1      ||
  ||   5. Resposta Lista Exercicio 2      ||
  ||   0. Retornar menu anterior          ||
  ||                                      ||
  ==========================================
  ''')

  while True:
    op = int(input('Escolha opção da lista: '))

    if op == 1:
      print('\nPara acessar os pdf favor click no link abaixo\n')
      url = 'https://jaelps.github.io/repositorio_aula_ape_ifpb/'

      print(f'Link >>> {url}\n\n')
    elif op == 2:
      print('\nPara acessar os pdf favor click no link abaixo\n')
      url = 'https://jaelps.github.io/repositorio_aula_ape_ifpb/'

      print(f'Link >>> {url}\n\n')
    elif op == 3:
      print('\nPara acessar os pdf favor click no link abaixo\n')
      url = 'https://jaelps.github.io/repositorio_aula_ape_ifpb/'

      print(f'Link >>> {url}\n\n')
    elif op == 4:
      exercicio_1 = m_rA()
      return exercicio_1
    elif op == 5:
      exercicio_2 = m_rB()
      return exercicio_2
    elif op == 0:
      print('Retornado ao menu principal')
      break
    else:
      print('erro')
