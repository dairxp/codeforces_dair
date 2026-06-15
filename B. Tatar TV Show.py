t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    ok = True

    for r in range(k):
        ones = 0

        for i in range(r, n, k):
            if s[i] == '1':
                ones += 1

        if ones % 2:
            ok = False
            break

    print("YES" if ok else "NO")