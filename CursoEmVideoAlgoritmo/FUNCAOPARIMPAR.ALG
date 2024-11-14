Algoritmo "FuncaoParImpar"


Var
    N: Inteiro
    R: caractere
Funcao ParOuImpar(V: inteiro): caractere
inicio
    se (v % 2 = 0) entao
       Retorne "PAR"
    senao
       Retorne "IMPAR"
    FimSe
FimFuncao

Inicio
   EscrevaL("Digite um número: ")
   Leia(N)
   R <- ParOuImpar(N)
   EscrevaL("o número ",N, " é um valor ", R)


Fimalgoritmo