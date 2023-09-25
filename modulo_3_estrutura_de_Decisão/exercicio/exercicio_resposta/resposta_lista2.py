def ex01():
  n = input('Digite um número (de 1 a 7): ')

  if n == '1':
      dia = 'domingo'
  elif n == '2':
      dia = 'segunda-feira'
  elif n == '3':
      dia = 'terça-feira'
  elif n == '4':
      dia = 'quarta-feira'
  elif n == '5':
      dia = 'quinta-feira'
  elif n == '6':
      dia = 'sexta-feira'
  else:
      dia = 'sábado'
  
  if dia == '1' or dia == '7':
      tipo = 'final de semana'
  else:
      tipo = 'dia útil'
  
  print(dia)
  print(tipo)

def ex02():
  