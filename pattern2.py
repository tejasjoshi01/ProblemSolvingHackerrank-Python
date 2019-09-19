def crown(length,height):
    for i in range(height):
        for j in range(length):
            if i==0:
                if( j==0 or j==height or j==height-1):
                    print("*", end="")
                else:
                    print("*",end="")
        
            elif( i == height -1):
                print("*", end="")
            elif((j<i or j>height-1) and (j<height+i or j>=length-1)):
                print("$", end="")
            else:
                print("*", end="")
        print("")

t = int(input())

for i in range(t):
    length = int(input())
    height = (length - 1)/2
    height = int(height)
    crown(length,height)
