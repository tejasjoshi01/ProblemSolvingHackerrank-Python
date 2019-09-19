
v = int(input())

ud = input()
udint = []
count = 0
sum = 0

for i in range(v):
    if "U" == ud[i]:
        udint.append(1)
    else:
        udint.append(-1)

for i in range(v):
    sum = sum + udint[i]
    if sum == 0:
        count+=1

print(count-1)
