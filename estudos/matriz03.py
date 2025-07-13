linhas = int(input("Digite o total de linhas: "))
colunas = int(input("Digite o total de colunas: "))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input("Digite um valor: "))
        linha.append(valor)
    matriz.append(linha)
    
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print(matriz[l][c],end=" ")
    print()
    
    
