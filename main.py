from menuPrincipal.m1ConceitoFundamentais import m1

from menuPrincipal.m2IntroducaoAPython import m2

from menuPrincipal.m3EstruturaDeDecisao import m3

from menuPrincipal.m4EstruturaDeRepeticao import m4

print('\n\n\n')
with open('banner_jacupy.txt', 'r') as arquivo:
  conteudo = arquivo.read()
  print(conteudo)

resp = input('Deseja iniciar? (s/n):  ')

if resp == 'n':
  exit()
elif resp == 's':
  controle = True
  while controle:
    print('''
  ===============[ Menu Inicial ]===============
  ||                                          ||
  ||     1. Modulo 1 Conceito Fundamentais    ||
  ||     2. Modulo 2 Introdução a Python      ||
  ||     3. Modulo 3 Estrutura de Decisão     ||
  ||     4. Modulo 4 Estrutura de Repetição   ||
  ||     0. Para finalizar sistema            ||
  ||                                          ||
  ==============================================
  ''')
    op = int(input('Escolha a opção desejada:  '))
  
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

else:
  print('Escola uma opção valida')