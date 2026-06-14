for i in range(int(input())):
	n,m =map(int, input().split())
	req=[tuple(map(int, input().split())) for _ in range(n)]

	total=0
	tiempo=0
	inicio=0

	for a,b in req:
		delta =a-tiempo


		min_movi=delta

		if (inicio^b)!=(delta%2):
			min_movi-=1

		if min_movi<0:
			min_movi=0

		total+=min_movi

		tiempo=a
		inicio=b

	total+=m-tiempo
	print(total)