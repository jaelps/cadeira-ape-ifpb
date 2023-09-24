def ex01():
  sal = 1000.0
  comissao = 200.0
  percentual = 0.05

  nomeVendedor = input('Nome do vendedor:  ')
  quantidadeCarros = int(input('Numero de carros: '))
  valorTotalVendas = float(input('numero de vendas totais:  '))

  calSalario = sal + (comissao * quantidadeCarros) + (percentual * valorTotalVendas)

  print(f'Ola {nomeVendedor} seu salario é {calSalario}')


def ex02():
  nota1 = float(input('favor informar primeira nota: '))
  nota2 = float(input('digite infomrar segunda nota: '))

  media = (nota1 * 6 + nota2 * 4) / 10  #media com peso de nota

  print(f'A media da nota é {media} ')


def ex03():
  x = int(input('digite o valor x: '))
  y = int(input('digite o valor y:  '))
  
  print(f'valor de x é {x} e o valor de y é {y}')
  
  x,y=y,x
  
  print(f'valor de x é {x} e o valor de y é {y}')

def ex04():
  inicioK = int(input('valor de kilometro rodados inicio:  '))
  fimK = int(input('valor kilometro no medidor atual:   '))
  altonomiaG= int(input('quantidade de combustivel gasto: '))
  preco_Litro = float(input('qual o preço do combustivel por litro?  '))
  capacidade = int(input('capacidade do tanque:  '))
  
  k_rodado = inicioK-fimK
  km_l = k_rodado/altonomiaG
  altonomiaT = km_l * capacidade
  
  custo_T = altonomiaG*preco_Litro
  print(f'seu carro tem altonomia de {custo_T}km')

def ex05():
  segundos = int(input('informe o tempo em segundo: '))
  cHoras = segundos // 3600
  cMinutos = segundos // 60
  segundos %= 60
  
  print(f'tempo total {cHoras} horas, {cMinutos} minutos, {segundos} segundos')

def ex06():
  banco = 'Weblands'
  
  print(f'Bem vindo ao banco {banco}\n')
  print('favor informar o valor do saque')
  valor_saque = int(input('Valor em Bit(B$): '))
  print(f'Para B${valor_saque} é necessario')
  
  cedulas = [50, 10, 5, 1]
  qtd_cedulas = [0, 0, 0, 0]
  
  qtd_cedulas[0] = valor_saque // cedulas[0]
  valor_saque %= cedulas[0]
  
  qtd_cedulas[1] = valor_saque // cedulas[1]
  valor_saque %= cedulas[1]
  
  qtd_cedulas[2] = valor_saque // cedulas[2]
  valor_saque %= cedulas[2]
  
  qtd_cedulas[3] = valor_saque // cedulas[3]
  
  print(
      f'- {qtd_cedulas[0]} notas de B$:50\n- {qtd_cedulas[1]} notas de B$:10\n- {qtd_cedulas[2]} notas de B$:5\n- {qtd_cedulas[3]} notas de B$:1'
  )
