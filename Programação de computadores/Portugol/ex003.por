programa
{
	
	funcao inicio()
	{
		
		real salario, financiamento
          escreva("Informe o salário: ")
          leia(salario)
          escreva("Informe o financiamento: ")
          leia(financiamento)
          se (financiamento <= (5 * salario)){
          	escreva("Financionamento concedido")
          } senao {
          	escreva("Financiamento negado")
   		}
          escreva("\nObrigado por nos consultar!")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 426; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */