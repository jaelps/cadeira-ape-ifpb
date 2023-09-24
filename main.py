from menuLista1 import menu_1
from menuLista2 import menu_2

print('Bem vindo ao S.A.E (SITEMA DE ANALISE DE EXERCICIOS')
controle = True
while controle:
  print('''
==============================================
||     1. Modulo 1 Conceito Fundamentais    ||
||     2. Modulo 2 Introdução a Python      ||
||     3. Modulo 3 Estrutura de Decisão     ||
||     4. Modulo 4 Estrutura de Repetição   ||
||     0. Para finalizar sistema            ||
==============================================
''')
  op = int(input('Escolha a opção desejada:\n'))

  if op == 1:
    importar_menu1 = menu_1()
  elif op == 2:
    importal_menu2 = menu_2()
  elif op == 3:
    importal_menu2 = menu_2()
  elif op == 4:
    importal_menu2 = menu_2()
  elif op == 0:
    print('sistema esta sendo finalizado ...')
    controle = False
  else: 
    print('Favor escolha uma opção valida')
print('Tenha um bom dia')
