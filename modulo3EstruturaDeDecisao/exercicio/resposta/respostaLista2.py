def ex01():
  dia = ''
  tipo = ''
  n = int(input('Digite um número (de 1 a 7): '))

  if n == 1:
    dia = 'domingo'
    tipo = 'final de semana'
  if n == 2:
    dia = 'segunda-feira'
    tipo = 'dia útil'
  if n == 3:
    dia = 'terça-feira'
    tipo = 'dia útil'
  if n == 4:
    dia = 'quarta-feira'
    tipo = 'dia útil'
  if n == 5:
    dia = 'quinta-feira'
    tipo = 'dia útil'
  if n == 6:
    dia = 'sexta-feira'
    tipo = 'dia útil'
  if n == 7:
    dia = 'sábado'
    tipo = 'final de semana'

  print(dia)
  print(tipo)


def ex02():
  c = input('Digite um caracter: ').upper()

  if c >= 'A' and c <= 'Z':
    if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
      #if c in ('A','E','I','O','U'):
      tipo = 'vogal'
    else:
      tipo = 'consoante'
  else:
    if c >= '0' and c <= '9':
      tipo = 'número'
    else:
      tipo = 'caracter especial'

  print(tipo)


def ex03():
  ano = int(input('Ano: '))

  if ((ano % 4 == 0) and (not ano % 100 == 0)) or (ano % 400 == 0):
    print('Bissexto')
  else:
    print('Não bissexto')


def ex04():

  inicio = int(input('Hora inicial: '))
  final = int(input('Hora final: '))

  if inicio < final:
    tempo = final - inicio
  else:
    tempo = 24 - inicio + final

  print('Duração:', tempo, 'horas')


def ex05():
  import math

  print('Entre com os coeficientes da equação de 2º grau:')
  a = float(input('a: '))
  b = float(input('b: '))
  c = float(input('c: '))

  delta = (b**2) - (4 * a * c)

  if delta < 0:
    print('Não há raízes')
  else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'As raízes são: {x1:.1f} e {x2:.1f}')


def ex06():
  print('1ª Etapa')
  n1 = float(input('Nota 1: '))
  n2 = float(input('Nota 2: '))
  media = (n1 + n2) / 2
  print(f'Média: {media:.1f}')

  if media >= 7.0:
    print('Apto para a 2ª Etapa')
    n3 = float(input('Nota 3: '))
    if n3 >= 8.0:
      print('Aprovado no concurso')
    else:
      print('Reprovado no concurso')
  else:
    print('Eliminado na 1ª Etapa')
