alunos = []
boletins = list()
cont = 0
while True:
    alunos.append(str(input("Nome: ")))
    alunos.append(float(input("Primeira nota: ")))
    alunos.append(float(input("Segunda nota: ")))
    media = (alunos[1] + alunos[2]) / 2
    alunos.append(media)
    boletins.append(alunos[:])
    alunos.clear()
    resp = str(input("Deseja continuar? [S/N]"))
    if resp in "Nn":
        break

print("=-" * 30)
print("No. NOME            MÉDIA")
print("------------------------------")
for i, a in enumerate(boletins):
    print(f"{i}  {a[0]}            {a[3]}")
print("------------------------------")
while True:
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe)"))
    if opc == 999:
        print("FINALIZANDO...")
        break
    if opc <= len(boletins) - 1:
        print(f"Notas de {boletins[opc][0]} são {boletins[opc][1]} e {boletins[opc][2]}")
