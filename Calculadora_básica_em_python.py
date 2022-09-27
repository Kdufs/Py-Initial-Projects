#marca

print('''
      --------------------
      |      Kdufs       |
      --------------------
      ''')

#variáveis

n1 = int(input('Escolha um Número\n>>>'))
n2 = int(input('Escolha outro Número\n>>>'))
sinal = input('Escolha um sinal(- + / *)\n>>>')
consulta = 'Houve algum problema ao Executar o código, caso precise de ajuda, mande um email para contatokdufs@gmail.com'

#decisões

if sinal == "-":
    print( n1 - n2)
elif sinal == "+":
    print(n1 + n2)
elif sinal == "/":
    print(n1 / n2)
elif sinal == "*":
    print(n1 * n2)
else:
    print(consulta)