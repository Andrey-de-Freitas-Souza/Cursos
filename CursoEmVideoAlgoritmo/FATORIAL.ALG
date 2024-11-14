Algoritmo "Fatorial"

Var
    C, N, F: Inteiro
Inicio
       Escreva("Digite um número:")
       leia(n)
       c <- n
       F <- 1
       Repita
             F <- F * c
             c <- C - 1
       Ate (C < 1)
       Escreva("O valor do fatorial de " ,N, "é igual a:" ,F)

Fimalgoritmo