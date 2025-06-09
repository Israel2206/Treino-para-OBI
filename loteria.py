sorteio = []
sorteado = []

numero = 1
acertos = 0

n1,n2,n3,n4,n5,n6 = map(int, input().split())
sorteio.append(n1)
sorteio.append(n2)
sorteio.append(n3)
sorteio.append(n4)
sorteio.append(n5)
sorteio.append(n6)

numero = 1


n1,n2,n3,n4,n5,n6 = map(int, input().split())
sorteado.append(n1)
sorteado.append(n2)
sorteado.append(n3)
sorteado.append(n4)
sorteado.append(n5)
sorteado.append(n6)

numero += 1

sorteio.sort()
sorteado.sort()

for num in sorteio:
    if num in sorteado:
        acertos += 1

if acertos == 3:
    print("terno")
elif acertos == 4:
    print("quadra")
elif acertos == 5:
    print("quina")
elif acertos == 6:
    print("sena")
else:
    print("azar")
