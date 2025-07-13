#Encontre e exiba o maior valor de uma matriz 3x3 preenchida.

linhas = colunas = 3
matriz = []

for l in range(linhas):
    linha = []
    for c in range(colunas):
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)
    
maior = matriz[0][0]

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] > maior:
            maior = matriz[l][c]
            
print(f'\nO maior número é : {maior}')