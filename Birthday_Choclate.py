#Submitted_Succesfully

n = int(input())

if n == 1:
    sl = int(input())

    ( d , m ) = input().split(" ")
    ( d , m ) = ( int(d) , int(m) )

    if sl == d:
        print(1)
    else:
        print(0)


else:
    choc = []
    sum_all = []

    count = 0

    choclate = input().split(' ')
    choc = choclate

    for i in range(n):
        choc[i] = int(choc[i])

    ( d , m ) = input().split(" ")
    ( d , m ) = ( int(d) , int(m) )


    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum = sum + choc[i+j]
        sum_all.append(sum)



    for i in range(len(sum_all)):
        if  sum_all[i] == d:
            count+=1

    print(count)
