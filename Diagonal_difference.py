#submitted succesfully

n = int(input())
matrix = []

for i in range(n):
    line = []
    lines = str(input()).split(" ")
    matrix.append(lines)


d1=0
d2=0

for i in range(n):
    for j in range(n):
        if(i==j):
            d1=d1+int(matrix[i][j])

for i in range(n):
    for j in range(n):
        if(i+j==(n-1)):
            d2=d2+int(matrix[i][j])


diff=d1-d2
print(abs(diff))
