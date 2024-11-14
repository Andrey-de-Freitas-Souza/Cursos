nome = str(input("Nome: "))
media = float(input("Média: "))
sit = 'Reprovado'
if media >= 6:
    sit = 'Aprovado'
aluno = {'Nome':nome, 'Média': media,'Situação': sit}
for k, v in aluno.items():
    print(f"{k} é igual a {v}")