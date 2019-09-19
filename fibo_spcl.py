t = int(input())

for i in range(t):
    ( c , d ) = input().split(" ")
    ( c , d ) = (int(c),int(d))

    b = d - c

    a = c - b
    print(a , b)

