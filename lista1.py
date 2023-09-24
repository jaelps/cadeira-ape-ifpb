def ex01():
  #item 1 ok
  print('Questão')
  print('Faça um programa que exiba na tela do computador a mensagem (Bem-vindo ao mundo da programação\n')
  print('Resposta:\n')
  print('seja bem vindo ao mundo da programação\n\n')
  
def ex02():
  #item 2 ok
  print('Questão')
  print('Escreva um programa que leia um número interiro e exiba o dobro dele')

  print('Resposta:\n')
  n = int(input('digite um numero: '))
  dobro = n * 2
  print(f'o dobro do numero é {dobro} \n\n')

def ex03():
  print('Questão')
  print('Faça um programa que leia números reais, calcule e exiba a soma deles')
  
  print('Resposta:\n')
  n1 = float(input('digite o primeiro numero:  '))
  n2 = float(input('digite o segundo numero:  '))
  soma = n1 + n2
  print(f'A soma de {n1} + {n2}, é igual a {soma}\n\n')

def ex04():
  print('Questão')
  print('Escreva um programa para calcular a área de triângulo, dados os valores de base e altura [área= (base*altura/2')

  print('Resposta:\n')
  base = float(input('A base é: '))
  altura = float(input('Altura é: '))
  
  area = (base * altura) / 2
  
  print(f'A area do trinagulo é {area:.2f}')

def ex05():
  print('Questão')
  primeiroNome = input('favor informar primeiro nome:  ')
  sobreNome = input('Favor informar sobre nome: ')
  
  print(f'{sobreNome}, {primeiroNome} \n\n')

def ex06():
  print('Questão')
  valorDolarReal = float('favor informar o valor da coração dolar atual:  ')
  carteiraDolar = float(input('favor informar valor de sua carteira em dolar(US$): '))

  conversor = carteiraDolar * valorDolarReal
  
  print(f'você possui US$:{carteiraDolar} em sua carteira, convertido em real {conversor:.2f}\n\n')

def ex07():
  print('Questão')
  kgRefeicao = 25
  pesoPrato = float(input('favor informar o peso em kg do prato:  '))
  
  valorASerPago = float(pesoPrato * kgRefeicao)
  
  print(f'O peso do prato do clinete é {pesoPrato}, o kg do prato é {kgRefeicao} o valor a ser pago é {valorASerPago:.2f}\n\n')

def ex08():
  print('Questão')
  aluno = input('falor informar nome do aluno: ')
  primeiraNota = float(input('favor informar primeira nota: '))
  segundaNota = float(input('favor informar segunda nota: '))
  terceiraNota = float(input('favor informar segunda nota: '))
  
  media = (primeiraNota + segundaNota + terceiraNota) / 3
  
  print(f'o aluno{aluno} possui as notas, media de {media}')