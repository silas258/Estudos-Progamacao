# Exemplo 5 - Fatorial de um número
'''
Crie um programa que recebe um número e imprime o seu fatorial.
# Método 5Q's para montar um algoritmo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
2. O que devo fazer com estes dados?
- Eu devo calcular o fatorial do número que for passado para o meu programa e o exibir na tela
3. Quais são as restrições deste problema?
- O número deve ser um valor positivo
- O número deve ser um valor inteiroo
4. Qual é o resultado esperado?
- O resultado esperado é que o fatorial do número providenciado seja exibido.
5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
input numero
if numero > 0
if numero = inteiro
  fatorial = 1
  loop de 1 a numero
    fatorial = fatorial * numero
  print(fatorial)
'''
#Tranformando pseudocódigo acia em código Python

numero = int(input('Digite um número: '))
if numero > 0:  # Condição
  fatorial = 1  # Variável
  for item in range(1, numero + 1):  # Laço de repetição
    fatorial = fatorial * item  # Expressão
