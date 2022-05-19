programa
{
	
	funcao inicio()
	{
		inteiro anoAtual, anoNascimento, idade
		
		escreva("Digite o ano atual: ")
		leia(anoAtual)
		escreva("Digite o ano de nascimento: ")
		leia(anoNascimento)
		idade = anoAtual - anoNascimento
		se (idade < 18) {
			escreva("NÃO PODERÁS VOTAR")
		} senao {
			escreva("VOTO OBRIGATORIO...")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 340; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */