t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = sorted(map(int, input().split()))

    # comprimir valores iguales: (valor, cantidad)
    comp = []
    for x in a:
        if not comp or comp[-1][0] != x:
            comp.append([x, 1])
        else:
            comp[-1][1] += 1

    while comp:
        # si el máximo aparece un número par de veces, ya es YES
        if comp[-1][1] % 2 == 0:
            print("YES")
            break

        # si solo queda un valor distinto, no hay forma
        if len(comp) == 1:
            print("NO")
            break

        # si el segundo máximo está lo bastante cerca, también es YES
        if comp[-1][0] - comp[-2][0] <= k:
            print("YES")
            break

        # si no, ignoramos ese máximo y probamos con el siguiente
        comp.pop()