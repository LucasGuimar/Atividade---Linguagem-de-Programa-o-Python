#coding: utf-8

'''Atividade 4: Implementar uma função que retorne verdadeiro se o número for primo
(falso caso contrário). Testar de 1 a 100.'''

num = int(input('Digite um número: '))
tdiv = 0
for c in range(1, num + 1):
    if num % c == 0:
        tdiv += 1
if tdiv == 2:
    print('VERDADEIRO!')
else:
    print('FALSO!')



