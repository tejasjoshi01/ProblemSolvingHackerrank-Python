t = int(input())

for i in range(t):
    n = int(input())
    elements = []
    string = input().split(" ")
    sum = 0
    elements = string
    
    for i in range(n):
        elements[i] = int(elements[i])

#    print(elements)
    for i in range(n):
        sum = sum + elements[i]

    print(round( sum/7 ,6))
