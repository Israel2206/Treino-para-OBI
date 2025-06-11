conta = int(input())

preco = 7

if conta <=10:
    print(preco)

elif conta >10 and conta <=30:
    conta -= 10
    print(preco+conta)

elif conta >30 and conta <=100:
    preco += 20
    conta -= 30
    print(preco+(conta*2))

else:
    preco+=160
    conta-=100
    print(preco+(conta*5))
