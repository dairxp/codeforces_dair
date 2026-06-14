for i in range(int(input())):
	n=int(input())
	campos=list(map(int, input().split()))

	suma_total=sum(campos)
	impares=[x for x in campos if x%2==1]

	if not impares:
		print(0)
	elif len(impares) %2==1:
		print(suma_total)
	else:
		print(suma_total- min(impares))

################
#Esta mal
