# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

try: 
    numero_do_usuario = int(input('Insira um número: '))

    resto = numero_do_usuario % 5

    print(f'O resto da divisão de {numero_do_usuario} por 5 é igual a {resto}')
except ValueError:
    print('Ops! Recebemos algo inválido. Insira apenas números!')