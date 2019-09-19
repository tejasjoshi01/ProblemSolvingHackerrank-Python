#second test case shold be TLE but showing runtime error

t = int(input())

for q in range(0,t):
    sum_all = []
    n = int(input())
    array = input().split(" ")
    list = []
    list = array

    for i in range(n):
        list[i] = int(list[i])

    for i in range(n):
        sum = 0
        for j in range(n):
            if i != j :
                sum+=array[j]
        sum_all.append(sum)


    for i in range(len(sum_all)):
        sum_all[i] = str(sum_all[i])


    sep = " "
    sum_op = sep.join(sum_all)
    print(sum_op)

