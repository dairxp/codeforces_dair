t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    k = max(h) + 1 - min(h)
    print(k)