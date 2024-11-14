Algoritmo "JogoDaVelha"

Var
   midinv: vetor[1..3, 1..3] de inteiro
   mid: vetor[1..3, 1..3] de caractere
   jogador: vetor[1..3,1..3] de inteiro
   l, c,cont, contpar: Inteiro
   r: caractere
Inicio

   contpar <- 0
   r <- "0"
   c <- 0
   cont <- 1
   mid[1,1] <- "1"
   mid[1,2] <- "2"
   mid[1,3] <- "3"
   mid[2,1] <- "4"
   mid[2,2] <- "5"
   mid[2,3] <- "6"
   mid[3,1] <- "7"
   mid[3,2] <- "8"
   mid[3,3] <- "9"



   repita
          LimpaTela
         Se contpar % 2 = 1 entao
             para l <- 1 ate 3 faca
                para c <- 1 ate 3 faca
                 se r = mid[l,c] entao
                         mid[l,c] <- " X "
                 FimSe
                FimPara
             FimPara
          FimSe
          
          Se contpar % 2 = 0 entao
             para l <- 1 ate 3 faca
                para c <- 1 ate 3 faca
                 se r = mid[l,c] entao
                    mid[l,c] <- " O "

                 FimSe
                FimPara
             FimPara
          FimSe

          para l <- 1 ate 3 faca
              para c <- 1 ate 3 faca
                    Se c < 3 entao
                       Escreva(mid[l,c]:3,"|")
                    Senao
                         Escreva(mid[l,c]:3)
                    FimSe
              FimPara
              Escreval()
              Se l < 3 entao
                 escreval("---+---+----")
              FimSe
        FimPara

               para l <- 1 ate 3 faca
                  para c <- 1 ate 3 faca
                       se mid[l,1] = mid[l,2] entao
                          se mid[l,2] = mid[l,3] entao
                               r <- "99"
                          FimSe
                       FimSe
                       se mid[1,c] = mid[2,c] entao
                          se mid[2,c] = mid[3,c] entao
                               r <- "99"
                          FimSe
                       FimSe
                       se mid[1,c] = mid[2,c] entao
                          se mid[2,c] = mid[3,c] entao
                               r <- "99"
                          FimSe
                       FimSe
                       se mid[1,1] = mid[2,2] entao
                          se mid[2,2] = mid[3,3] entao
                               r <- "99"
                          FimSe
                       FimSe
                       se mid[3,1] = mid[2,2] entao
                          se mid[2,2] = mid[1,3] entao
                               r <- "99"
                          FimSe
                       FimSe
                       
                  FimPara
               FimPara
                
          se r <> "99" entao
               Se contpar % 2 = 0 entao
                   EscrevaL("=================")
                   EscrevaL("VEZ DO JOGADOR (X) JOGAR!")
                   EscrevaL("Qual a sua jogada?")
                   leia(r)
                   contpar <- contpar + 1

               senao
                    EscrevaL("=================")
                   EscrevaL("VEZ DO JOGADOR (O) JOGAR!")
                   EscrevaL("Qual a sua jogada?")
                   leia(r)
                   contpar <- contpar + 1
               FimSe
          FimSe
          

   ate r = "99"
 Escreval("JOOGO FINALIZADO")



Fimalgoritmo