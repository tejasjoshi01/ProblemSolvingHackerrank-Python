
#testcases_failed

p = int(input())

n = int(input())

r = p - n
l = n
#print(l,r)


if(abs(n-p) == 1 and n !=2):
    print(0)

else:
    if l < r:
#        print("here 1")
#
#
#        print(n)


        if( n%2 == 1 ):
#            print("here 2")
            print(n - 2)
        else:
#            print("here 2-a")
            print(n-1)


    else:
#        print("here 3")
        if(n%2 == 0):
#            print("here 4")
            print(p - n-1)
        else:
#            print("here 4-a")
            print(p - n)



