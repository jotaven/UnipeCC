"""03.Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres)."""

nome = str(input("Qual o seu nome [mínimo 4 caracteres]: ")).strip()
while len(nome) < 4:
    nome = str(input("Seu nome deve ter mais que 3 caracteres: ")).strip()

idade = int(input("Qual a sua idade: "))
while (idade > 150) or (idade < 0):
    idade = int(input("Idade invalida! \nQual a sua idade(entre 0 e 150): "))

salario = float(input("Qual o seu salário? "))
while salario < 0:
    salario = float(input("Que salario é esse que você fica devendo logo após o seu salário???\nDigite o seu salário seu abestado: "))

sexo = str(input("Digite seu sexo[M/F]: ")).strip().upper()
while sexo != "M" and sexo != "F":
    sexo = str(input("Biologicamente, você deve ser 'F' ou 'M': ")).strip().upper()

estadoCivil = str(input("Digite o seu Estado civil (s, c, v ou d): ")).strip().lower()
while (estadoCivil!='s')and(estadoCivil!='c')and(estadoCivil!='v')and(estadoCivil!='d'):
    print("Nao tem estado civil 'confuso'")
    estadoCivil = input("Deve ser s, c, v ou d: ")


