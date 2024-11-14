Algoritmo "Pesado"

Var
   I: inteiro
   N ,Pesado: Caractere
   P, Mai: Real
Procedimento Topo()
inicio
      LimpaTela
      EscrevaL("---------------------------------")
      EscrevaL("D E T E C T O R  DE  P E S A D O")
      EscrevaL("Maio Peso até agora; ", Mai, "Kg")
      Escreval("----------------------------------")

FimProcedimento
Inicio
      Topo()
      Para I <- 1 ate 5 faca
           Escreva("Digite o nome: ")
           Leia(N)
           Escreva("Digite o peso de ", N , ": ")
           Leia(P)
           Se (P>Mai) entao
           Mai <- P
           Pesado <- N
           FimSe
           Topo()
      Fimpara
      Topo()

Fimalgoritmo