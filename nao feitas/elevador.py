q, l = map(int, input().split())
contador = 1
verificador = "N"
entrada = 0

while contador <=q:
    e,s = map(int, input().split())
    entrada+=e
    entrada-=s
    if entrada >= l:
        verificador = "S"
    contador+=1

print(verificador)