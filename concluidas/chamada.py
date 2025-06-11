alunos = []

quantidade, numero = map(int, input().split())
contador = 1

while contador <= quantidade:
    aluno = input()
    alunos.append(aluno)
    contador+=1

alunos.sort()
print(alunos[numero-1])