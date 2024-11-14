
algoritmo "semnome"
var
   cadeira : vetor [1..10] de inteiro
   c : inteiro
   aluguel : Inteiro
   resposta : caractere
inicio

      Para c := 1 ate 10 faca
          cadeira[c] := c
      FimPara

      Repita
      limpaTela
      para c := 1 ate 10 faca
      se (aluguel = cadeira[c]) ou (cadeira[c] = 11) entao
         cadeira[c] := 11
         escreva("[---] ")
         Senao
         escreva("[B",cadeira[c],"] ")
      fimse

      fimpara

      escreval(" ")
      escreva("Reservar assento: B")
      leia(aluguel)

      Se (cadeira[aluguel] = 11) entao
         escreval("!ERROR: Cadeira ocupada! ")
         Senao
              escreval("Cadeira B", aluguel, " reservada!")
      FimSe

      escreva("Deseja continuar reservando? [s/n]: ")
      leia(resposta)

      ate(resposta = "n")
fimalgoritmo