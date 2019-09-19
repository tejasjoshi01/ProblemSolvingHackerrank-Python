


t = int(input())

for z in range(t):
    (x,y,z)=input().split(" ")
    (x,y,z)=(int(x),int(y),int(z))
    
    cnt = 0
    for i in range(1,1000001):
        if(i%x==0 and i%y==0 and i%z==0):
            cnt+=1
    print(cnt)
