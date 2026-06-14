
for _ in range(int(input())):
	i=input()
	if len(i) <= 10:
		print(i)
	else:
		resu=str(len(i)-2)
		print(i[0]+resu+i[-1])