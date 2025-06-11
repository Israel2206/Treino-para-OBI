n = int(input())
contador = 1

saida = 0

while contador <= n:
    t,v =map(int, input().split())

    saida += (t*v)

    contador +=1

print(saida)