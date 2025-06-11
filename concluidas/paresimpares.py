par=[]
impar=[]

quantidade = int(input())
contador = 1

while contador <=quantidade:
    numero = int(input())
    if numero %2==0:
        par.append(numero)
    else:
        impar.append(numero)
    contador+=1

par.sort()
impar.sort(reverse=True)

for i in par:
    print(i)
for i in impar:
    print(i)