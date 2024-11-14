Algoritmo "ListagemAlunos"

Var
   nome: vetor[1..4] de caractere
   n1: vetor[1..4] de Real
   n2: vetor[1..4] de Real
   m: vetor[1..4] de Real
   i: Inteiro
Inicio
    Para i <- 1 ate 4 faca
         Escreval("Aluno(a) ", i)
         Escreval("----------------------")
         Escreva("Nome: ")
         Leia (nome[i])
         Escreva("Primeira nota: ")
         Leia (n1[i])
         Escreva("Segunda nota: ")
         Leia (n2[i])
         Escreval("----------------------")
         m[i] <- (n1[i]+ n2[i]) / 2
         
    FimPara

    LimpaTela
    Escreval("LISTAGEM DE ALUNOS")
    Escreval("------------------")
    Para i <- 1 ate 4 faca
         Escreval("O aluno(a) ",nome[i]," tirou: ")
         Escreval(n1[i]," na primeira prova,")
         Escreval(n2[i], " na segunda,")
         Escreval("e obteve média: ", m[i])
         Escreval("----------------------")
    FimPara
Fimalgoritmo