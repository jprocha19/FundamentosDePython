nome = (input("Digite seu nome: "))
cargo = (input("Digite seu cargo: "))
salario = float(input("Digite seu salário: "))

salario = salario + (salario * 0.1)

print(f"Nome: {nome}")
print(f"Cargo: {cargo}")
print(f"Salário: $ {salario:.2f}")