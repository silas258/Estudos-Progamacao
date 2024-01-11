# Laços de Repetição + Listas

# Laços de repetição - servem para executar um comando várias vezes

# Listas - servem para armazenar coleções de dados e poderem ser acessados por um índice

#Exemplos de laçõs de repetição
#for palavra in range(1, 4):
#  print('Carregando')
'''
for item in coleção:
  expressão
'''
# for - serve para executar um comando várias vezes enquanto uma condição for verdadeira
# item - servem para armazenar os itens da coleção
# in - serve para indicar que o item está dentro da coleção
# coleção - serve para armazenar uma coleção de dados

#for item in range(1, 20):
#  print(item)
#for item in range(1, 20, 2):
#  print(item)

#Exemplos de Laçõs de repetição com Listas

#nomes = ['Jhonatan', 'Cristian', 'Roberto', 'Camila']
#for nome in nomes:  #basicamente no item utilizar a nomenclatura no singular em comparação com a coleção que está no plural. Isso não afeta a execução do programa, mas é uma forma de entender melhor o código.
#  print(nome)

#Problema 1 a N - Imprime os valores de 1 a N
'''
input numero_maximo
valor_inicial = 1
loop de valor_inical a numero_maximo
  print valor
'''

valor_maximo = int(input('Digite o valor máximo: '))
valor_inicial = 1
for numero in range(valor_inicial, valor_maximo + 1):
  print(numero)
