Algoritmo "NumeroPrimo"

Var
    C , N, ContDiv: inteiro


Inicio
      C <- 1
      ContDiv <- 1
      Escreva("Digite um valor para saber se ele � primo:")
      Leia(N)
      Repita

            C <- C + 1
            Se (N % C = 0) ent�o
               ContDiv <- ContDiv + 1
            FimSe
      Ate (C > N)
      Se (ContDiv > 2) ent�o
         escreval("O n�mero " , N , " pode ser dividido por " , COntDiv," n�meros")
         escreval("Portanto ele n�o � um n�mero primo")
      Sen�o
         escreval("O n�mero " , N , " pode ser dividido apenas por " , COntDiv," n�meros")
         escreval("Portanto ele � um n�mero primo")
      FimSe
Fimalgoritmo
