Algoritmo "NumeroPrimo"

Var
    C , N, ContDiv: inteiro


Inicio
      C <- 1
      ContDiv <- 1
      Escreva("Digite um valor para saber se ele é primo:")
      Leia(N)
      Repita

            C <- C + 1
            Se (N % C = 0) então
               ContDiv <- ContDiv + 1
            FimSe
      Ate (C > N)
      Se (ContDiv > 2) então
         escreval("O número " , N , " pode ser dividido por " , COntDiv," números")
         escreval("Portanto ele não é um número primo")
      Senão
         escreval("O número " , N , " pode ser dividido apenas por " , COntDiv," números")
         escreval("Portanto ele é um número primo")
      FimSe
Fimalgoritmo
