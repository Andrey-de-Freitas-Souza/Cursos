Algoritmo "ParesComVetor"

Var
    i, c: Inteiro
    v: vetor[1..7] de inteiro

Inicio
      Para i <- 1 ate 7 faca
           Escreval("Digite o" ,i,"o. valor")
           Leia (v[i])
           se v[i] % 2 = 0 entao
              c <- c + 1
           FimSe
      Fimpara
      Escreval("Desses números",c, " são pares")
      Para i <- 1 ate 7 faca
           Se (v[i] % 2 = 0) entao
              Escreval("Valor PAR na posição ",i)
           FimSe
      Fimpara
Fimalgoritmo