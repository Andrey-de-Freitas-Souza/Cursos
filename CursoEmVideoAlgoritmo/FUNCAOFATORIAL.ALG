Algoritmo "FuncaoFatorial"

Var
   N, F: Inteiro
Funcao Fatorial(X: inteiro): Inteiro
Var C,R: Inteiro
inicio
      R<- 1
      Para C <- 1 ate X faca
           R <- R * C
           C <- C + 1
      Retorne R
FImPara
FimFuncao
Inicio
    Escreval("Digite um número para saber seu Fatorial: ")
    Leia (N)
     F <- Fatorial(N)
     Escreval("O Fatorial de" , N , " é ", F)
    
    
    
    

Fimalgoritmo