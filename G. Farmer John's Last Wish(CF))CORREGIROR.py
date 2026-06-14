import math

t = int(input())   

for _ in range(t):
    n = int(input())                
    a = list(map(int, input().split()))  
    
    res = []
    for i in range(1, n + 1):        
        prefix = a[:i]
        
        g = prefix[0]
        for x in prefix[1:]:
            g = math.gcd(g, x)

        best = 0
        for d in range(g + 1, max(prefix) + 1):
            cnt = 0
            for x in prefix:
                if x % d == 0:
                    cnt += 1
            best = max(best, cnt)
        
        res.append(best)
    
    print(" ".join(map(str, res)))
