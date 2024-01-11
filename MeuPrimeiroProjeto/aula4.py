# Coleções (Listas) -

#preco_1 = 20
#preco_2 = 50
#preco_3 = 200
# Listas
#precos = [20, 50, 200]
#          0, 1, 2   = forma de acessar os itens da lista
#para acessar as listas é feita por um conceito chamado de índice. O índice é basicamente o endereço dessa informação dentro da lista.
#índice sempre inicia do número 0
#print(precos[0])
#print(
#    precos.index(200)
#)  #Em casos de dúvida sobre qual é o índice de algo, você tem uma função no python que ajuda a descobrir

#Listas
#diversidades = [15, 'Jhonatan', True]
#print(diversidades[0])
#print(diversidades[1])
#print(diversidades[2])

# Laços em iteráveis
#for preco in precos:
#  print(preco)
'''
#Exemplo 5 - Some os valores (exemplo com coleções)
Dados uma coleção de dados "idades" [15,46,75,34,23] imprima na tela a soma deste valores)

idades = [15,46,75,34,23]
total = 0
loop idade em idades
  total = total + idade
print total
'''

idades = [15, 46, 75, 34, 23]  #Coleção do tipo lista
total = 0
for idade in idades:  #laços de repetição
  total = total + idade
print(total)
#Explicação: A cada momento que o laço de repetição é executado, entra na lista de idades extrair um valor para a variavel temporaria idade e soma esse valor com o valor da variavel total.
