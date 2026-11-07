#entrada
nome = (input("Digite o seu nome: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

#processamento
imc = peso / (altura * altura)

#saida
print(f"Seu imc é igual a: {imc:.2f} kgs")