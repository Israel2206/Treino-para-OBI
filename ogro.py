n = int(input())

if n >= 0 and n <=10:
    if n == 0:
        print("*\n*")
    elif n <=5:
        print(n*"I"+"\n*")
    else:
        print("IIIII")
        n-=5
        print(n*"I")
    
