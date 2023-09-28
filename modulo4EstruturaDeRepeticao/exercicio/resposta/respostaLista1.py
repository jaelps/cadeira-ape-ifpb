def ex01():
  import math

  print('    X    RAIZ(X)    CUBO(X)')
  
  for x in range(50,301):
      if x % 5 == 0:
          raiz = math.sqrt(x)
          cubo = x ** 3
          print(f'{x:5} {raiz:10.4f} {cubo:10}')

def ex02():
  s = 0

  n = int(input('Entre com um número inteiro: '))
  
  for i in range(1,n+1):
      s = s + i
  
  print(f'Soma = {s}')

def ex03():
  f = 1

  n = int(input('Entre com um número inteiro positivo: '))
  
  for i in range(2,n+1):
      f *= i  # f = f * i
  
  print(f'{n}! = {f}')

def ex04():
  qtd = 5 #vamos testar o programa com poucos números, para agilizar a execução.

  print(f'Digite {qtd} números inteiros:')
  
  for i in range(qtd):
  
      num = int(input())
  
      if i == 0: #testa se é a 1ª iteração do for
          maior = num
      else:
          if num > maior:
              maior = num
  
  print(f'Maior = {maior}')

def ex05():
  contM = 0
  contF = 0
  
  n = int(input('Quantidade de pessoas: '))
  
  for i in range(n):
  
      sexo = input('Sexo(M/F): ').upper()
  
      if sexo == 'M':
          contM = contM + 1
      else:
          contF = contF + 1
  
  percM = contM / n * 100
  percF = contF / n * 100
  
  print()
  print(f'Percentual de homens: {percM:.0f}%')
  print(f'Percentual de muheres: {percF:.0f}%')

def ex06():
  n = int(input('Informe o valor de N: '))
  x = int(input('Informe o valor de X: '))
  y = int(input('Informe o valor de Y: '))
  
  print('\nOs múltiplos de',n,'entre',x,'e',y,'são:')
  
  if x > y:
      aux = x
      x = y
      y = aux
  
  for i in range(x,y+1):
      if i % n == 0:
          print(i,end=' ')

def ex07():
  n = int(input('Digite um número inteiro: '))

  cont = 0
  
  for i in range(2,n):
      if n % i == 0:
          cont = cont + 1
  
  if cont == 0 and n != 1:
      print('primo')
  else:
      print('não é primo')

def ex08():
  import math

  maior = 0
  
  n = int(input('Digite um número inteiro: '))
  
  for i in range(1,n+1):
      raiz = math.sqrt(i)
      if raiz == int(raiz) and i > maior:
          maior = i
  
  print('Maior quadrado perfeito:',maior)