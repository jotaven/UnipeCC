programa
{
	
	funcao inicio()
	{
		cadeia time1, time2
		inteiro qGols1, qGols2
		
		escreva("Digite o nome do time 1: ")
		leia(time1)
		
		escreva("Digite a quantidade de gols do ", time1, ": ")
		leia(qGols1)
		
		escreva("Digite o nome do time 2: ")
		leia(time2)
		
		escreva("Digite a quantidade de gols do ", time2, ": ")
		leia(qGols2)
		
		se (qGols1 > qGols2){
			escreva("O ", time1, " Ganhou!")
		}
		senao se (qGols2 > qGols1) {
			escreva("O ", time2, " Ganhou!")
		}
		senao {
			escreva("Empate")
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 521; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */