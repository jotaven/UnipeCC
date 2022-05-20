salario = float(input('Digite o seu salário'))

if salario < 300:
    novoSalario = salario * 1.45
elif 300 <= salario <= 600:
    novoSalario = salario * 1.25
else:
    novoSalario = salario * 1.15

print(f"O seu novo salário é de R${novoSalario:.2f}")