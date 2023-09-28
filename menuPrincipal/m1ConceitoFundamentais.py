import webbrowser


def m1():
  print('''
  =============[ Modulo 1 ]===============
  ||                                    ||
  ||  1. Slide Conceitos Fundamentais   ||
  ||  0. Retornar menu anterior         ||
  ||                                    ||
  ========================================
  ''')

  while True:
    op = int(input('Escolha opção da lista: '))

    if op == 1:
      print('\nPara acessar os pdf favor click no link abaixo\n')
      url = 'https://jaelps.github.io/repositorio_aula_ape_ifpb/'

      print(f'Link >>> {url}\n\n')
    elif op == 0:
      print('Retornado ao menu principal')
      break
    else:
      print('erro')
