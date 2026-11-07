#1. Receba a idade em anos e imprima em meses, dias, horas e minutos

# Padrões de escrita de variáves, funções etc em programação
# Pascal Case - Idade Da pessoa - Maiúscula desde a primeira palavra
# Camel Case  - idade Da pessoa - Maiúscula desde a segunda palavra 
# Snake Case  - Idade_Da_Pessoa - Underline para separar cada palavra 
# Kebab Case  - Idade-Da-Pessoa - Tracinho para separar cada palavra

# Números, textos e booleanos
# Entrada
idade = int(input("Digite a idade: ")) #pega o texto e converte para número inteiro

# Processamento
idadeEmMeses = idade * 12
idadeEmDias = idade * 365
#idadeEmHoras = idade * 365 * 24
idadeEmHoras =  idadeEmDias * 241
idadeEmMinutos =   idadeEmHoras * 60 

# Saída
print(f" Sua idade em meses é igual a: {idadeEmMeses} meses!😁👍")
print(f" Sua idade em dias é igual a: {idadeEmDias} dias!😁👍")
print(f" Sua idade em horas é igual a: {idadeEmHoras} horas!😁👍")
print(f" Sua idade em minutos é igual a: {idadeEmMinutos} minutos!😁👍")