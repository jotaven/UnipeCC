salario = float(input("Digite o seu salario: "))
if salario < 300:
    novoSalario = salario * 1.35
else:
    novoSalario = salario *1.15
print(f"O seu salario antigo era de {salario:.2f} e foi reajustado para {novoSalario:.2f}")