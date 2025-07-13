linhas = colunas = 3

matriz = []

for l in range(linhas):
    linha = []
    for c in range(colunas):
        linha.append(1 if l == c else 0)
    matriz.append(linha)
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print(matriz[l][c], end=" ")
    print()
