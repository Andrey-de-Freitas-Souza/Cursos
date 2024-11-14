Algoritmo "Opcoesdejogos"

Var
   time: vetor[1..6] de caractere
   i,j: Inteiro
Inicio
         Escreval("----------------------")
         EscrevaL("CAMPEONATO DE FUTEBOL")
         Escreval("----------------------")
    Para i <- 1 ate 3 faca
         Escreva("Digite o nome do ",i," time: ")
         Leia(time[i])
    FimPara
    LimpaTela
    Escreval("------------------")
    Escreval("OPÇÕES DE JOGOS")
    Escreval("------------------")


    Para i <- 1  ate 2 faca
          para j <- i+ 1 ate 3 faca
             Se (time[i] <> time[j]) entao
                Escreval(time[i], " [] X [] " ,time[j])
                Escreval(time[j], " [] X [] " ,time[i])

             FimSe
          FimPara
     FimPara

Fimalgoritmo