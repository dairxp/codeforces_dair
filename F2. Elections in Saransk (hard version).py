import sys

MOD = 10**9 + 7
MAXA = 500000

# ---------- SPF ----------
spf = list(range(MAXA + 1))
for i in range(2, int(MAXA ** 0.5) + 1):
    if spf[i] == i:
        step = i
        start = i * i
        for j in range(start, MAXA + 1, step):
            if spf[j] == j:
                spf[j] = i


def factorize(n):
    """Return prime factorization as {prime: exponent}."""
    res = {}
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        res[p] = res.get(p, 0) + e
    return res


def mul_poly(a, b, D):
    """Multiply two polynomials truncated to degree D."""
    res = [0] * (D + 1)
    for i in range(D + 1):
        ai = a[i]
        if ai:
            lim = D - i
            for j in range(lim + 1):
                bj = b[j]
                if bj:
                    res[i + j] = (res[i + j] + ai * bj) % MOD
    return res


def pow_poly(base, exp, D):
    """Polynomial exponentiation truncated to degree D."""
    res = [0] * (D + 1)
    res[0] = 1
    b = base
    e = exp
    while e:
        if e & 1:
            res = mul_poly(res, b, D)
        e >>= 1
        if e:
            b = mul_poly(b, b, D)
    return res


def count_for_prime(hist, c):
    """
    hist[r] = how many numbers a_i have exponent r for this prime.
    c = exponent of this prime in x.
    """
    Emax = 0
    for r in range(len(hist) - 1, 0, -1):
        if hist[r]:
            Emax = r
            break

    D = c + Emax

    # ge[m] = number of voters with exponent >= m
    ge = [0] * (Emax + 2)
    for m in range(Emax, 0, -1):
        ge[m] = ge[m + 1] + hist[m]

    # P_0 = 1
    prev = [0] * (D + 1)
    prev[0] = 1

    ways = prev[c] if c <= D else 0

    # cache of powers for this prime
    cache = {}
    bases = [None] * (Emax + 1)
    for u in range(1, Emax + 1):
        bases[u] = [1] * (u + 1) + [0] * (D - u)

    for m in range(1, Emax + 1):
        poly = [0] * (D + 1)
        poly[0] = 1

        # factors with exact exponent < m
        for u in range(1, m):
            cnt = hist[u]
            if cnt:
                key = (u, cnt)
                if key not in cache:
                    cache[key] = pow_poly(bases[u], cnt, D)
                poly = mul_poly(poly, cache[key], D)

        # factors with exponent >= m
        cnt = ge[m]
        if cnt:
            key = (m, cnt)
            if key not in cache:
                cache[key] = pow_poly(bases[m], cnt, D)
            poly = mul_poly(poly, cache[key], D)

        # exact max m
        ways = (ways + poly[c + m] - prev[c + m]) % MOD
        prev = poly

    return ways


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        x = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n

        fx = factorize(x)

        # Histograms only for primes from x
        need_hist = {p: [0] * 20 for p in fx}   # exponent up to 18 is enough
        other_sumexp = {}  # primes not in x -> total exponent sum

        for val in a:
            f = factorize(val)
            for p, e in f.items():
                if p in fx:
                    need_hist[p][e] += 1
                else:
                    other_sumexp[p] = other_sumexp.get(p, 0) + e

        ans = 1

        # primes not in x: c = 0, easy formula
        for s in other_sumexp.values():
            ans = (ans * (s + 1)) % MOD

        # primes in x: polynomial DP
        for p, c in fx.items():
            ans = (ans * count_for_prime(need_hist[p], c)) % MOD

        out.append(str(ans))

    print("\n".join(out))


if __name__ == "__main__":
    solve()