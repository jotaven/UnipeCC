'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

salarioPorHora = float(input('Digite quanto você ganha por hora em R$: '))
horaTrabalhadas = int(input('Digite quantas horas você trabalha por mês: '))

salarioBruto = salarioPorHora * horaTrabalhadas

impostoDeRenda = salarioBruto * 0.11
INSS = salarioBruto * 0.08
sindicado = salarioBruto * 0.05
salarioLiquido = salarioBruto - (impostoDeRenda + INSS + sindicado)

print(f'''+ Salário Bruto : R${salarioBruto:.2f}
- IR (11%): R${impostoDeRenda:.2f}
- INSS (8%): R${INSS:.2f}
- Sindicato ( 5%): R${sindicado:.2f}
= Salário Liquido: R${salarioLiquido:.2f}''')
