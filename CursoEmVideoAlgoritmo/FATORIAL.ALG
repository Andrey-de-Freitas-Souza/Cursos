Algoritmo "Fatorial"

Var
    C, N, F: Inteiro
Inicio
       Escreva("Digite um n�mero:")
       leia(n)
       c <- n
       F <- 1
       Repita
             F <- F * c
             c <- C - 1
       Ate (C < 1)
       Escreva("O valor do fatorial de " ,N, "� igual a:" ,F)

Fimalgoritmo