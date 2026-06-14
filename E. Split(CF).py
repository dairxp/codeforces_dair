
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    total = {}
    for v in a:
        total[v] = total.get(v, 0) + 1
    
    imposible = False
    for v in total:
        if total[v] % k != 0:
            imposible = True
            break
    if imposible:
        print(0)
        continue

    cuota = {}
    for v in total:
        cuota[v] = total[v] // k
    
    izquierda = 0
    freq = {}
    ans = 0
    
    for derecha in range(n):
        val = a[derecha]
        freq[val] = freq.get(val, 0) + 1
        
        while freq[val] > cuota[val]:
            left_val = a[izquierda]
            freq[left_val] -= 1
            izquierda += 1
        
        ans += (derecha - izquierda + 1)
    
    print(ans)
