# a=int(input())
# lista=[]
# for i in range(1, a+1):
# 	for j in range(1, i+1):
# 		lista.append(j)
# print(lista)

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    count = 0

    for k in range(1, n + 1):
        seq = list(range(1, k + 1))
        
        for start in range(len(seq) - m + 1):
            match = True
            for i in range(m):
                if seq[start + i] != a[i]:
                    match = False
                    break
            if match:
                count += 1
    
    print(count)
