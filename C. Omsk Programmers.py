t = int(input())

for _ in range(t):
    a, b, x = map(int, input().split())

    A = []
    cost = 0
    cur = a

    while True:
        A.append((cur, cost))
        if cur == 0:
            break
        cur //= x
        cost += 1

    B = []
    cost = 0
    cur = b

    while True:
        B.append((cur, cost))
        if cur == 0:
            break
        cur //= x
        cost += 1

    ans = float('inf')

    for va, ca in A:
        for vb, cb in B:
            ans = min(ans, ca + cb + abs(va - vb))

    print(ans)