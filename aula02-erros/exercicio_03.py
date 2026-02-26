# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

try: 
    primeira_parcela = int(input('Digite o primeiro número: '))
    segunda_parcela = int(input('Digite o segundo número: '))

    produto = primeira_parcela * segunda_parcela

    print(f'O produto entre {primeira_parcela} e {segunda_parcela} é igual a {produto}')
except ValueError:
    print('Ops! Recebemos algo inválido. Insira apenas números!')