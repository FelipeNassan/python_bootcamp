CONSTANTE_BONUS_ANUAL = 1000

# 1) Solicita ao usuário que digite seu nome
nome_completo = input('Digite seu nome completo: ')

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario_bruto = float(input('Infome seu salário bruto (ex.: 1250.78): '))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
percentual_bonus = float(input('Informe o percentual de bônus (ex.: 12.5): '))

# 4) Calcule o valor do bônus final
bonus_final = CONSTANTE_BONUS_ANUAL + (salario_bruto * percentual_bonus)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f'Olá {nome_completo}, seu bônus final é de R$ {bonus_final:.2f}')

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# 1) Informar o salário e/ou o percentual de bönus com a vírgula sendo o separador decimal (ex.: 1250,78)