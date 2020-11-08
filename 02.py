#coding: utf-8

''' Atividade 2: Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam
ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso
os valores formem um triângulo, calcular e escrever a área deste triângulo. Se
não formam triângulo escrever os valores lidos. (Se a &gt; b + c não formam
triângulo algum, se a é o maior).'''

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

if a < b + c and b < a + c and c < a + b:
    print('Os 3 valores informados FORMAM UM TRIÂNGULO.')
else:
    print('Os valores informados NÃO FORMAM UM TRIÂGULO.')
