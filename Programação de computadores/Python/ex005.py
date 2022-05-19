sigla = str(input("Digite o estado: ")).strip().upper()
nordeste = ["PE", "PB"]
sudeste = ["RJ", "SP"]
if sigla in nordeste:
    print("Nordeste")
else:
    print("Sudeste")