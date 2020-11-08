#coding: utf-8

'''Atividade 5: Escreva uma função que:
a) Receba uma frase como parâmetro.
b) Retorne uma nova frase com cada palavra com as letras invertidas.'''

frase = input('Digite uma frase: ')
print(' Você digitou: {}'.format(frase))
finvertida = ' '.join(palavra[::-1] for palavra in frase.split())
print('Frase invertida: {}'.format(finvertida))