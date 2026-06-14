n,k= map(int, input().split())
p= list(map(int, input().split()))

limite=p[k-1]
contador=0

for puntuacion in p:
    if puntuacion >=limite and puntuacion >0:
        contador+=1

print(contador)