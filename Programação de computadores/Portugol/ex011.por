programa
{
	
	funcao inicio()
	{
		inteiro opcao, quantidade
		escreva("[100] Cachorro Quente\n[101] Bauru Simples\n[102] Bauru com ovo\n[103] Hamburguer\n[104] Cheeseburguer\n[105] Refrigerante\n")
		escreva("Digite o código do item  correspondente: ")
		leia(opcao)
		escreva("\nDigite a quantidade: ")
		leia(quantidade)
		se (opcao == 100) {
			escreva("R$ ", 1.70*quantidade, '0')
		}
		senao se (opcao == 101) {
			escreva("R$ ", 2.30*quantidade, '0')
		}
		senao se (opcao == 102) {
			escreva("R$ ", 2.60*quantidade, '0')
		}
		senao se (opcao == 103) {
			escreva("R$ ", 2.40*quantidade, '0')
		}
		senao se (opcao == 104) {
			escreva("R$ ", 2.50*quantidade, '0')
		}
		senao se (opcao == 105) {
			escreva("R$ ", 1.00*quantidade, '0')
		}
		senao {
			escreva("Erro, tente novamente...")
		}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 203; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */