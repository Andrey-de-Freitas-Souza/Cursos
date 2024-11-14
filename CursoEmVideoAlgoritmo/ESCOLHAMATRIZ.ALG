Algoritmo "EscolhaMatriz"

Var
   mid: vetor[1..4, 1..4] de inteiro
   l, c, r: Inteiro

Inicio

   r <- 5
   para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
             Escreva("Digite o valor para posição [" ,l, "," ,c, "]: ")
             Leia(mid[l,c])
        FimPara
   FimPara

    Repita
          LimpaTela
          Se r = 1 entao
             para l <- 1 ate 4 faca
                  para c <- 1 ate 4 faca
                       Escreva(mid[l,c]:4)
                  FimPara
                  escreval()
             FimPara
          FimSe
          Se r = 2 entao
                 para l <- 1 ate 4 faca
                      para c <- 1 ate 4 faca
                           Se l = c entao
                                Escreva(mid[l,c]:4)
                           Senao
                                Escreva("    ")
                           FimSe
                      FimPara
                      escreval()

                 FimPara
          FimSe
          
          Se r = 3 entao
                 para l <- 1 ate 4 faca
                      para c <- 1 ate 4 faca
                           Se c > l  entao
                                Escreva(mid[l,c]:4)
                           Senao
                                Escreva("    ")
                           FimSe
                      FimPara
                      escreval()

                 FimPara
          FimSe

          Se r = 4 entao
                 para l <- 1 ate 4 faca
                      para c <- 1 ate 4 faca
                           Se c < l  entao
                                Escreva(mid[l,c]:4)
                           Senao
                                Escreva("    ")
                           FimSe
                      FimPara
                      escreval()

                 FimPara
          FimSe

          Escreval("MENU DE OPCOES")
          EscrevaL("=================")
          EscrevaL("[1] Mostrar a Matriz")
          EscrevaL("[2] Diagonal Principal")
          EscrevaL("[3] Triângulo Superior")
          EscrevaL("[4] Triâgulo Inferior")
          EscrevaL("[5] Sair")
          Escreva("Digite a opção: ")
          Leia(r)

     ate r = 5

Fimalgoritmo