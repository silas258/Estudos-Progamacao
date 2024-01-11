# Variáveis - servem para armazenar dados e nomes específicos
# Números
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5  # float
# valores boleanos
esta_aberto = True
# String
nome_do_curso = "Lógica de Programação"

#Quando eu faço o script acima, estou imprimindo o valor da variável na tela
#para executar o script inserido no arquivo aula1.py eu preciso executar o comando python aula1.py no shell

#Outros tipos de variáveis básicas
# Números - serve para armazenar números inteiros ou decimais
# Valores boleanos - serve para verificar se algo é verdadeiro ou falso
# Strings - serve para variáveis que utilizam palavras

# Como variáveis seriam usadas em um programa real?
#Problema 1 - Valor por hora
#Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.
''' - utilizando aspas simples para descrever um pseudocódigo dessa maneira essas linhas não seram interpretadas pelo interpretador de código
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print valor_hora
'''
salario_mensal = input('Qual é o seu salário mensal? ')
horas_trabalhadas_por_mes = input('Quantas horas trabalha por mês?  ')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print(valor_hora)
