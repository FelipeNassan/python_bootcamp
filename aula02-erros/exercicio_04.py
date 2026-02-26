# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

try: 
    dividendo = int(input('Digite o primeiro número: '))
    divisor = int(input('Digite o segundo número: '))

    quociente = dividendo // divisor

    print(f'O quociente entre {dividendo} e {divisor} é igual a {quociente}')
except ValueError:
    print('Ops! Recebemos algo inválido. Insira apenas números!')
except ZeroDivisionError:
    print('Ops! Não é possível dividir por zero!')