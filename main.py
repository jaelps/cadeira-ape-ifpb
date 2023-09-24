from menuLista1 import menu_1
from menuLista2 import menu_2

print('Bem vindo ao S.A.E (SITEMA DE ANALISE DE EXERCICIOS')

while True:
  print('''
=========================================
||  1. Entrar 1ª lista de exercicio    ||
||  2. Entrar 2ª lista de exercicio    ||
||  0. Para finalizar sistema          ||
=========================================
''')
  op = int(input('Escolha a opção desejada:\n'))

  if op == 1:
    importar_menu1 = menu_1()
  elif op == 2:
    importal_menu2 = menu_2()
  elif op == 0:
    print('sistema esta sendo finalizado ...')
    break
print('Tenha um bom dia')
