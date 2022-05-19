"""faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um
 link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando
  este link (em minutos)."""

tamanhoArquivo = float(input("Informe o tamanho de um arquivo para download em MB: "))
velocidadeDownload = float(input("Informe a velocidade da internet em Mbps: "))

tempoMinutos = (tamanhoArquivo / velocidadeDownload) // 60
print(f"O donwload demorará aproximadamente {tempoMinutos:.0f} minutos")