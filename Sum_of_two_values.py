def funcao(n,x,lista):
    for i in range(n):
        j = n - 1
        k = 0
        while True:
            if k == n or j < 0:
                break
            else:
                if lista[i] + lista[j] == x:
                    return f"{i+1} {j+1}"
                    break
                else:
                    j -= 1
                    k += 1
    return "IMPOSSIBLE"

n,x = map(int,input().split())
lista = list(map(int,input().split()))
print(funcao(n,x,lista))