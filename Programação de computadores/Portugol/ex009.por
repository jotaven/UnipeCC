programa
{
	
	funcao inicio()
	{
		real numero1, numero2, resultado
		inteiro operacao
		escreva("Digite o primeiro numero: ")
		leia(numero1)
		escreva(" [1] Soma \n [2] Subtração \n [3] Multiplicação \n [4] Divisão \n Digite o numero que corresponde a operação que você quer: ")
		leia(operacao)
		escreva("Digite o segundo numero: ")
		leia(numero2)
		se (operacao == 1) {
			resultado = numero1 + numero2
			escreva(resultado)
		} senao se (operacao == 2) {
			resultado = numero1 - numero2
			escreva(resultado)
		} senao se (operacao == 3) {
			resultado = numero1 * numero2
			escreva(resultado)
		} senao se (operacao == 4) {
			resultado = numero1 / numero2
			escreva(resultado)
		} senao{
			escreva("Algo deu errado, tente novamente.")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 226; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */