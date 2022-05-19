programa
{
	
	funcao inicio()
	{
		inteiro qMacas
		real valorTotal
		escreva("Quantas maças? ")
		leia(qMacas)
		se (qMacas < 12) {
			valorTotal = 1.30 * qMacas
			escreva("R$ ", valorTotal)
		}
		senao {
			valorTotal = 1 * qMacas
			escreva("R$ ", valorTotal)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 263; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */