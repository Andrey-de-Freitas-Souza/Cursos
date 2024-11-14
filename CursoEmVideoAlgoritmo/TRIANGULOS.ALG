Algoritmo "triangulos"

Var
    l1,l2,l3: Real
    eq, es, tri: Logico
Inicio
      Escreval("Digite o primeiro lado:")
      leia(l1)
      Escreval("Digite o segundo lado:")
      leia(l2)
      Escreval("Digite o terceiro lado:")
      leia(l3)
      tri <- (l1 < l2 + l3) e (l2 < l1 + l3) e (l3 < l1 + l2)
      eq <- (l1 = l2) e (l2 = l3)
      es <- (l1 <> l2)e (l2 <> l3) e (l1 <> l3)

      Escreval("Pode formar um triângulo? ", tri)
      Escreval("O triângulo é EQUILATERO? ", eq)
      Escreval("O triângulo é ESCALENO? ", es)

      
      
Fimalgoritmo