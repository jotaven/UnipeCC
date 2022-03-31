def idadeNome():
    nome = str(input('Digite seu nome: ')).strip().capitalize()
    idade = int(input('Digite a sua idade: '))
    print(f'seu nome é {nome} e você tem {idade} anos.')


def somaDois():
    n1 = int(input('digite um numero inteiro: '))
    n2 = int(input('digite outro numero inteiro: '))
    soma = n1 + n2
    print(f'a soma entre {n1} e {n2} é igual à {soma}')

somaDois()