Algoritmo "MatrizDecisao"

Var
   mid: vetor[1..4, 1..4] de inteiro
   l, c: Inteiro
Inicio
   para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
             se (l = c) entao
             mid[l,c] <- 1
             senao
             mid[l,c] <- 0
             FimSe
        FimPara
   FimPara
    para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
             Escreva(mid[l,c]:2)
        FimPara
        escreval()
   FimPara

Fimalgoritmo