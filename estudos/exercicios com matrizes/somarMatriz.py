#Crie uma matriz 2x2 com valores quaisquer e calcule a soma de todos os seus elementos.

linhas = colunas = 2
matriz = []
soma = 0

for l in range(linhas):
    linha = []
    for c in range(colunas):
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        soma += matriz[l][c]

print(f'A soma de todos os elementos é: {soma}')