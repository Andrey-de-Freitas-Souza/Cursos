Algoritmo "MatrizPares"

Var
   valores: vetor[1..3, 1..3] de inteiro
   l, c, totpar: Inteiro
Inicio
   para l <- 1 ate 3 faca
        para c <- 1 ate 3 faca
             Escreva("Digite o valor da posição [" , l, "," , c,  "]:")
             Leia(valores[l,c])
        FimPara
   FimPara
     totpar <- 0
    para l <- 1 ate 3 faca
        para c <- 1 ate 3 faca
             Se valores[l,c] % 2 = 0 entao
                escreva("{", valores[l,c]:2, "}")
                totpar <- totpar + 1
             senao
             Escreva(valores[l,c]:4)
             FimSe
        FimPara
        Escreval()
    FimPara
    Escreval("ao todo foram ", totpar,"números pares.")
Fimalgoritmo