contador=0

for _ in range(int(input())):
	p,v,t=map(int, input().split())

	
	if p+v+t >=2:
		contador+=1
print(contador)


'''
n = int(input())
contador = 0

for _ in range(n):
    linea = list(map(int, input().split()))
    if sum(linea) >= 2:
        contador += 1

print(contador)
'''

