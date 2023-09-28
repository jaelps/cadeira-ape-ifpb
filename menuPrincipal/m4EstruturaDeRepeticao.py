from modulo4EstruturaDeRepeticao.exercicio.menuListaExercicio.menuLista1 import m_rA

from modulo4EstruturaDeRepeticao.exercicio.menuListaExercicio.menuLista2 import m_rB


def m4():
  print('''
  =======================[ Modulo 4 ]========================
  ||                                                       ||
  ||    1. Slide Estrutura de Repetição                    ||
  ||    2. Exercico Estrutura de Repetição ( for )         ||
  ||    3. Exercico Estrutura de Repetição ( while )       ||
  ||    4. Resposta Lista de Exercicio ( for )             ||
  ||    5. Resposta Lista de Exercicio ( while )           ||
  ||    0. Retornar menu anterior                          ||
  ||                                                       ||
  ===========================================================
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
      md = m_rA()
      return md
    elif op == 5:
      md = m_rB()
      return md
    elif op == 0:
      print('Retornado ao menu principal')
      break
    else:
      print('erro')
