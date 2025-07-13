#criando Uma Matriz 3x3 em python
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
        print(matriz[l][c],end=" ")
    print()