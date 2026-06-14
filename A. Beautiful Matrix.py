for i in range(5):
    matrix=list(map(int, input().split()))
    for j in range(5):
        if matrix[j]==1:
            x,y=i,j 
            
print(abs(x-2)+abs(y-2))

