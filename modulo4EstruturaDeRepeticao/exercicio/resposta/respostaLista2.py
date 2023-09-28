def ex01():
  qtd = 3 #para fins de teste, vamos colocar apenas 3 ao invés de 30.
  soma = 0
  cont = 0
  
  print(f'Digite {qtd} números inteiros:')
  
  while cont < qtd:
      num = int(input())
      soma += num  # soma = soma + num
      cont += 1  # cont = cont + 1
  
  print (f'Soma = {soma}')

def ex02():
  flag = 999
  soma = 0
  cont = 0
  
  print(f'Digite vários números (para encerrar, digite {flag})')
  num = int(input())
  
  while num != flag:
      soma = soma + num
      cont = cont + 1
      num = int(input())
  
  media = soma / cont
  
  print(f'Média = {media:.1f}')

def ex03():
  flag = 0

  print(f'Digite vários números (para encerrar, digite {flag})')
  num = int(input())

  maior = num
  menor = num
  
  while num != flag:
  
      if num > maior:
          maior = num
  
      if num < menor:
          menor = num
  
      num = int(input())
  
  print(f'Maior = {maior}')
  print(f'Menor = {menor}')

def ex04():
  flag = 0
  print(f'Informe os dados dos alunos. Para encerrar, digite a matrícula {flag}.')
  mat = int(input('\nMatrícula: '))
  while mat != flag:
      nome = input('Nome: ')
      nota1 = float(input('1ª Nota: '))
      nota2 = float(input('2ª Nota: '))
      media = (nota1 + nota2) / 2
      if media >= 7.0:
          sit = 'Aprovado'
      else:
          sit = 'Reprovado'
      print(f'\nMatrícula: {mat}')
      print(f'Nome: {nome}')
      print(f'Média: {media:.1f}')
      print(f'Situação: {sit}')
      mat = int(input('\nMatrícula: '))
  print('Fim do programa.')

def ex05():
  resp = 'S'
  while resp == 'S':
      n = int(input('Digite um número inteiro: '))
      if n % 2 == 0:
          result = 'par'
      else:
          result = 'ímpar'
      print(f'{n} é {result}')
      resp = input('Deseja continuar (S/N)? ').upper()
      print()
  print('Fim do programa')

def ex06():
  chico = 150
  ze = 110
  cont = 0
  while ze <= chico:
      cont = cont + 1
      chico = chico + 2
      ze = ze + 3
  print(cont)

def ex07():
  flag = 0
  soma_geral = 0
  cont_geral = 0
  cont_faixa = 0
  menor_idade = 1000
  print('Digite a idade das pessoas visitantes do show.')
  print('Obs: para encerrar, digite a idade 0')
  idade = int(input('Idade: '))
  while idade != flag:
      soma_geral += idade
      cont_geral += 1
      if idade >= 18 and idade <= 21:
          cont_faixa += 1
      if idade < menor_idade:
          menor_idade = idade
      idade = int(input('Idade: '))
  media_geral = soma_geral / cont_geral
  perc_faixa = cont_faixa / cont_geral * 100
  print(f'\nMédia de idade do público: {media_geral:.0f} anos')
  print(f'Porcentagem de pessoas com idade entre 18 e 21 anos: {perc_faixa:.1f}%')
  print(f'Idade do visitante mais jovem: {menor_idade} anos')


def ex08():
  controle = True
  valor_por_quantidade_h = 0
  quantidade_h = 0
  valor_por_quantidade_c = 0
  quantidade_c = 0
  valor_por_quantidade_b = 0
  quantidade_b = 0
  valor_por_quantidade_f = 0
  quantidade_f = 0
  print('''
=====[ codigo / produto / valor ]=====
|                                    |
|    H. Hamburger.........R$:5,00    |
|    C. Cheese Burger.....R$:6,00    |
|    B. Cheese Bacon......R$:7,00    |
|    F. Cheese Frango.....R$:4,00    |
|                                    |
======================================
  ''')
  while controle:
    codigo = input('codigo do produto:  ').lower()
    if codigo in 'hcbfx':
      if codigo == 'x':
        controle = False

      if codigo == 'h':
        Hamburger = 5.00
        quantidade_h = int(input('quantidade: '))
        valor_por_quantidade_h = Hamburger * quantidade_h

      if codigo == 'c':
        CheeseBurger = 6.00
        quantidade_c = int(input('quantidade: '))
        valor_por_quantidade_c = CheeseBurger * quantidade_c

      if codigo == 'b':
        CheeseBacon = 7.00
        quantidade_b = int(input('quantidade: '))
        valor_por_quantidade_b = CheeseBacon * quantidade_b

      if codigo == 'f':
        CheeseFrango = 4.00
        quantidade_f = int(input('quantidade: '))
        valor_por_quantidade_f = CheeseFrango * quantidade_f
    else:
      print('Favor escolha opção valida')
  else:
    total_pagamento = valor_por_quantidade_h + valor_por_quantidade_c + valor_por_quantidade_b + valor_por_quantidade_f

    print('\n\n=========[ Unid / Prd / Vlr ]=========\n')
    print(
        f'     {quantidade_h}  Hamburger.........R$:{valor_por_quantidade_h}    '
    )
    print(
        f'     {quantidade_c}  Cheese Burger.....R$:{valor_por_quantidade_c}      '
    )
    print(
        f'     {quantidade_b}  Cheese Bacon......R$:{valor_por_quantidade_b}      '
    )
    print(
        f'     {quantidade_f}  Cheese Frango.....R$:{valor_por_quantidade_f}    '
    )
    print(f'        Total.............R$:{total_pagamento}    \n')
    print('=====================================')