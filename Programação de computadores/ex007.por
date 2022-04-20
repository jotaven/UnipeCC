programa
{
	
	funcao inicio()
	{
		real numero1, numero2, numero3, media
		escreva("Digite o primeiro numero: ")
		leia(numero1)
		escreva("Digite o segundo numero: ")
		leia(numero2)
		escreva("Digite o terceiro numero: ")
		leia(numero3)
		media = (numero1 + numero2 + numero3)/3
		se (numero1>media) {
			escreva("O ", numero1, "  é maior que a média")
		} senao se (numero2>media){
			escreva("O ", numero2, "  é maior que a média")
		} senao se (numero3>media){
			escreva("O ", numero3, "  é maior que a média")
		} senao {
			escreva("Todos os numeros são iguais")
		}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 581; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */