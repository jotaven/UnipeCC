nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
mediaFinal = (nota1 + nota2 + nota3)/3

if mediaFinal > 5:
    print("Aprovado!")
else:
    print("Reprovado!")
