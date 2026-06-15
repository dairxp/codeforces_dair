import sys

MOD = 10**9 + 7
MAXA = 500000

# SPF = smallest prime factor
spf = list(range(MAXA + 1))
for i in range(2, int(MAXA ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, MAXA + 1, i):
            if spf[j] == j:
                spf[j] = i

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
out = []

for _ in range(t):
    n = data[idx]
    x = data[idx + 1]  # en la versión fácil siempre es 1
    idx += 2

    a = data[idx:idx + n]
    idx += n

    total_exp = {}

    for num in a:
        while num > 1:
            p = spf[num]
            cnt = 0
            while num % p == 0:
                num //= p
                cnt += 1
            total_exp[p] = total_exp.get(p, 0) + cnt

    ans = 1
    for s in total_exp.values():
        ans = (ans * (s + 1)) % MOD

    out.append(str(ans))

print("\n".join(out))