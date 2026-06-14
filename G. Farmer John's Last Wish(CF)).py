import math

t = int(input())   # número de casos de prueba

for _ in range(t):
    n = int(input())                 # tamaño del array
    a = list(map(int, input().split()))  # elementos del array
    
    res = []
    for i in range(1, n + 1):        # vamos viendo cada prefijo
        prefix = a[:i]
        
        # calculamos gcd de todo el prefijo
        g = prefix[0]
        for x in prefix[1:]:
            g = math.gcd(g, x)
        
        # buscamos el mejor "k" posible
        best = 0
        for d in range(g + 1, max(prefix) + 1):
            cnt = 0
            for x in prefix:
                if x % d == 0:
                    cnt += 1
            best = max(best, cnt)
        
        res.append(best)
    
    print(" ".join(map(str, res)))
