def ex01():
  n = int(input('Digite um número inteiro: '))

  if n % 2 == 0:
    result = 'par'
  else:
    result = 'ímpar'
  
  print(f'{n} é {result}')

def ex02():
  print('Digite dois números inteiros:')
  a = int(input())
  b = int(input())
  
  print('Números em ordem crescente: ',end='')
  if a < b:
      print(a,b)
  else:
      print(b,a)

def ex03():
  print('Digite 3 número inteiros:')
  a = int(input())
  b = int(input())
  c = int(input())
  
  if a > b and a > c:
    maior = a
  elif b > c:
    maior = b
  else:
    maior = c
  
  print(f'O maior é {maior}')

def ex04():
  nome = input('Nome: ')
  sexo = input('Sexo(M/F): ')
  if sexo == 'M' or sexo == 'm':
      print(f'Olá, Sr. {nome}!')
  else:
      print(f'Olá, Sra. {nome}!')


def ex05():
  salmin = 1320.00
  perc = 5/100
  
  totvend = float(input('Valor total das vendas: R$ '))
  
  salario = totvend * perc
  
  if salario < salmin:
    salario = salmin
  
  print(f'\nSalário: R$ {salario:.2f}')

def ex06():
  nome = input('Nome: ')
  conc = input('Conceito: ').upper()
  
  if conc == 'A':
      rec = 'Fortemente recomendado'
  elif conc == 'B' or conc == 'C':
      rec = 'Recomendado'
  else:
      rec = 'Não recomendado'
  
  print(f'O estudante {nome} foi {rec}')

def ex07():
  peso = float(input('Peso(kg): '))
  alt = float(input('Altura(m): '))
  
  imc = peso / (alt**2)
  
  if imc < 18.5:
    grau = 'Baixo peso'
  elif imc < 25:
    grau = 'Normal'
  elif imc < 30:
    grau = 'Sobrepeso'
  else:
    grau = 'Obesidade'
  
  print(f'Grau de Obesidade: {grau}')

def ex08():
  n1 = int(input('1º operando: '))
  n2 = int(input('2º operando: '))
  op = input('Operador: ')
  if op == '+':
      res = n1 + n2
  elif op == '-':
      res = n1 - n2
  elif op == 'x' or op == '*':
      res = n1 * n2
  elif op == '/':
      res = n1 / n2
  elif op == '%':
      res = n1 % n2
  else:
      res = 'Operador desconhecido'
  print('Resultado:',res)