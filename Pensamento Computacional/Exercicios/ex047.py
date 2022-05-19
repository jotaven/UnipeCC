"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

nome = str(input("Nome: ")).strip()
senha = str(input("Senha: "))

while (nome == senha):
    print("Sua senha deve ser diferente do login")
    senha = str(input("Senha: "))

print("Cadastro concluido")

