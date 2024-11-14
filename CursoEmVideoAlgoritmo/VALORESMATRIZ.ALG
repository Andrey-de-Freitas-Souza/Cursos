Algoritmo "ValoresMatriz"

Var
   mid: vetor[1..4, 1..4] de inteiro
   l, c,sdp, psl, maior: Inteiro
Inicio
   maior <- 0
   sdp <- 0
   psl <- 1
   para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
             Escreva("Digite o valor da posicao [", l, "," , c, "]: ")
             Leia(mid[l,c])
             Se (l = c) entao
              sdp <- sdp + mid[l,c]
             FimSe
             Se l = 2 entao
                psl <- psl * mid[2, c]
             Fimse
        FimPara
   FimPara

    Para c <- 1 ate 4 faca
        Se c = 3 entao
           psl <- psl * mid[2, c]
        Fimse
    FimPara
    
   Para l <- 1 ate 4 faca
        se mid[l,3] > maior entao
           maior <- mid[l,3]
        FimSe
   FimPara

    para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
             Escreva(mid[l,c]:5)
        FimPara
        escreval()
   FimPara

   Escreval("a soma dos valores da diagonal principal é de ", sdp)
   Escreval("O produto dos valores da segunda linha é de ", psl)
   Escreval("O maior número da terciera coluna é ", maior)
   
Fimalgoritmo