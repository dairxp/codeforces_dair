'''
for _ in range(int(input())):
    n, m, q = map(int, input().split()) 
    b = list(map(int, input().split()))  
    a = list(map(int, input().split())) 

    distancia_1 = abs(a[0] - b[0])
    distancia_2 = abs(a[0] - b[1])

    print(min(distancia_1, distancia_2))
'''
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, q = map(int, input().split())
    b1, b2 = map(int, input().split())
    a   = int(input())

    left, right = min(b1, b2), max(b1, b2)

    if left < a < right:
        
        interval = right - left
        pasos = (interval + 1) // 2
    else:
        pasos = min(abs(a - b1), abs(a - b2))

    print(pasos)
