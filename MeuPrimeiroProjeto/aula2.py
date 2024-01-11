# Condicionais - servem para verificar se uma condição é verdadeira ou falsa

# if - serve para verificar se uma condição é verdadeira

# elif - serve para verificar se uma condição é verdadeira e outra é falsa
# utilizada em situações que tem varias avaliações a serem feitas.
# Casos de uso do elif: Todo comando if ele obrigatoriamente será executado pelo seu interpretador(funcionalidade que vai ler o seu código e executar os comandos se necessário), já os elif serão executados caso o if acima deles não sejam executados.

# else - serve para verificar se uma condição é falsa

mensagem_multilinha = '''
Este é um exemplo de uma string
que ocupa várias linhas.
Pode ser muito útil para documentação
ou para representar blocos de texto longos.
'''
'''
Eae jhonatan, bora dar uma saida hoje?
Se eu terminar me trabalho aqui, eu consigo.
'''
#trabalho_terminado = True
#if trabalho_terminado == True:
# print('Opa! Bora dar uma saida. ')
#else:
# print('Não posso sair agora.')
'''
Ei, Você consegue me ajudar a mover essas caixas lá para fora hoje a tarde? Se eu estiver livre, sim. Mas se não der pede a meu irmão para te ajudar'''

#saida = input(
#    "Caso esteja com disponibilidade digite True, caso não  digite False: ")
#estou_livre = saida.lower() == 'true'

#if estou_livre:
#  print('Ok, posso ajudar hoje sim')
#else:
#  print('Peça o meu irmão para te ajudar')
'''
Eu cheguei atrasado na aula, ainda posso entrar? 
Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma suspensão'''

#numero_de_atrasos = 4
#if numero_de_atrasos >= 3:
#  print('Você está suspenso')
#elif numero_de_atrasos == 1:
#  print('Pode entrar, porém caso tome mais 2 faltas, irá ser suspenso')
#elif numero_de_atrasos == 2:
#  print('Pode entrar, porém caso tome mais 1 falta, irá ser suspenso')
#else:
#  print('Pode entrar')

#Encontre o maior entre 2 números
'''
input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor
  print o primeiro valor é maior
else
  print o segundo valor é maior
'''

primeiro_valor = input('Digite o primeiro valor:')
segundo_valor = input('Digite o segundo valor:')

if int(primeiro_valor) > int(segundo_valor):
  print('O primeiro valor é maior!')
else:
  print('O segundo valor é maior')
