from modulo3EstruturaDeDecisao.exercicio.menuListaExercicio.menuLista1 import m_rA

from modulo3EstruturaDeDecisao.exercicio.menuListaExercicio.menuLista2 import m_rB

def m3():
  print('''
  ================[ Modulo 3 ]=================
  ||                                         ||
  ||    1. Slide Estrutura de Decisão        ||
  ||    2. Exercico Estrutura de Decisão     ||
  ||    3. Exercico Complementar             ||
  ||    4. Resposta Lista Exercicio 1        ||
  ||    5. Resposta Lista Exercicio 2        ||
  ||    0. Retornar menu anterior            ||
  ||                                         ||
  =============================================
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
      modulo = m_rA()

    elif op == 5:
      modulo = m_rB()
      return modulo
    elif op == 0:
      print('Retornado ao menu principal')
      break
    else:
      print('erro')