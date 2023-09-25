from menu_principal.m1ConceitoFundamentais import m1

from menu_principal.m2IntroduçãoAPython import m2

from menu_principal.m3EstruturaDeDecisão import m3

from menu_principal.m4EstruturaDeRepetição import m4

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
    modulo1 = m1()
  elif op == 2:
    modulo = m2()
  elif op == 3:
    modulo = m3()
  elif op == 4:
    modulo = m4()
  elif op == 0:
    print('sistema esta sendo finalizado ...')
    controle = False
  else: 
    print('Favor escolha uma opção valida')
print('Tenha um bom dia')
