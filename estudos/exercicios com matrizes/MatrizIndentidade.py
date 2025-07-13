linhas = 3
colunas = 3

matriz = []

for l in range(linhas):
    linha = []
    for c in range(colunas):
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if l == c:
            matriz[l][c] = 1
        else:
            matriz[l][c] = 0

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print(matriz[l][c], end=" ")
    print()