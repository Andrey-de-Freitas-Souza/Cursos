Algoritmo "Sequenciadefibonaci"

Var
 C, N1, N2, N3: inteiro


Inicio
      N1 <- 0
      N2 <- 0
      N3 <- 1
      Escreva("0")
      Para C <- 1 ate 15 passo 1 faca
           Escreva(N3)
           N1 <- N2
           N2 <- N3
           N3 <- N1 + N3
      FimPara

Fimalgoritmo