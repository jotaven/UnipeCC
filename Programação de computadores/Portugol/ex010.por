programa
{
	
	funcao inicio()
	{
		inteiro opcao
		escreva("[1] Domingo\n[2] Segunda\n[3] terça\n[4] Quarta\n[5] Quinta\n[6] Sexta \n[7] Sábado\n")
		escreva("Digite um número de 1 a 7 e informaremos o dia da semana correspondente: ")
		leia(opcao)
		se (opcao == 1) {
			escreva("Domingo")
		}
		senao se (opcao == 2) {
			escreva("Segunda")
		}
		senao se (opcao == 3) {
			escreva("terça")
		}
		senao se (opcao == 4) {
			escreva("Quarta")
		}
		senao se (opcao == 5) {
			escreva("Quinta")
		}
		senao se (opcao == 6) {
			escreva("Sexta")
		}
		senao se (opcao == 7) {
			escreva("Sábado")
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
 * @POSICAO-CURSOR = 648; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */