# Entrada
anoDeNascimento = int(input("Digite o seu ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
idade = 0

# Processamento
idade = anoAtual - anoDeNascimento
idadeEmSemanas = 4 * 12 * idade

# Saida
print(f"Sua idade é igual a: {idade} ano(s)")
print(f"Sua idade em semanas é igual a: {idadeEmSemanas} semana(s)")