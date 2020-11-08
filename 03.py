#coding: utf-8

'''Atividade 3: Faça um programa que leia 3 números inteiros e mostre o menor deles.'''

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

print('O menor valor é: {}'.format(menor))

