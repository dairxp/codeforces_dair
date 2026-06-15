import sys
from collections import deque

def solve_case(n, a):
    def check(L):
        freq = [0] * (n + 1)
        dup = 0

        minq = deque()
        maxq = deque()

        def add(i):
            nonlocal dup
            v = a[i]
            c = freq[v]
            if c == 1:
                dup += 1
            freq[v] = c + 1

            while minq and a[minq[-1]] >= v:
                minq.pop()
            minq.append(i)

            while maxq and a[maxq[-1]] <= v:
                maxq.pop()
            maxq.append(i)

        def remove(i):
            nonlocal dup
            v = a[i]
            c = freq[v]
            if c == 2:
                dup -= 1
            freq[v] = c - 1

            if minq and minq[0] == i:
                minq.popleft()
            if maxq and maxq[0] == i:
                maxq.popleft()

        # primer ventana
        for i in range(L):
            add(i)

        INF = 10**9
        first_pos = [INF] * (n + 2)
        last_pos = [-1] * (n + 2)

        def process(start):
            if dup == 0:
                mn = a[minq[0]]
                mx = a[maxq[0]]
                if mx - mn == L - 1:
                    if start < first_pos[mn]:
                        first_pos[mn] = start
                    if start > last_pos[mn]:
                        last_pos[mn] = start

        process(0)

        for r in range(L, n):
            remove(r - L)
            add(r)
            process(r - L + 1)

        # buscamos dos bloques consecutivos de valores:
        # [s ... s+L-1] y [s+L ... s+2L-1]
        for s in range(1, n - 2 * L + 2):
            if first_pos[s] != INF and first_pos[s + L] != INF:
                a1, b1 = first_pos[s], last_pos[s]
                a2, b2 = first_pos[s + L], last_pos[s + L]

                # basta con que exista un par no traslapado
                if b1 - a2 >= L or b2 - a1 >= L:
                    return True

        return False

    for L in range(n // 2, 0, -1):
        if check(L):
            return L
    return 0


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        out.append(str(solve_case(n, a)))

    print("\n".join(out))


if __name__ == "__main__":
    main()