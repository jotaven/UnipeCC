programa
{
	
	funcao inicio()
	{
		real salario, novoSalario
          escreva("Informe o salário: ")
          leia(salario)
          se(salario <= 300)
          {
          	novoSalario = salario*1.35
          } senao {
          	novoSalario = salario*1.15
          }
   		escreva("Novo salário: ", novoSalario)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 56; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */