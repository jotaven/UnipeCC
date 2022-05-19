programa
{
	
	funcao inicio()
	{
		inteiro a, b, c
		escreva("numero 1: ")
		leia(a)
		escreva("numero 2: ")
		leia(b)
		escreva("numero 3: ")
		leia(c)
		se (a < b e a < c) {
			escreva(b + c)
		}
		senao se (b < a e b < c) {
			escreva(a + c)
		}
		senao se (c < a e c < b) {
			escreva (a + b)
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 305; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */