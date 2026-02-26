# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário

try: 
    numero_1 = int(input('Insire um número: '))
    numero_2 = int(input('Insire outro número: '))

    soma = numero_1 + numero_2

    print(f'A soma de {numero_1} e {numero_2} é igual a {soma}')
except ValueError:
    print('\nOps! Recebemos algo inválido. \nInsira apenas números inteiros!')
