import math

idade1 = int(input())
idade2 = int(input())

if idade1 == idade2:
    print(idade1)
else:
    maior = max(idade1,idade2)
    menor = min(idade1,idade2)
    velho = maior - menor
    print(maior+velho)