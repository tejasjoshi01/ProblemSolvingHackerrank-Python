(s,t) = input().split(" ")
(s,t) = (int(s),int(t))

 
(a,b) = input().split(" ")
(a,b) = (int(a),int(b))



(m,n) = input().split(" ")
(m,n) = (int(m),int(n))

 
apple = []
oranges = []

cnt1 = 0
cnt2 = 0

apple = input().split(" ")
oranges = input().split(" ")
 

#
#print(m,n)

for i in range(m):
    apple[i] = int(apple[i])
    apple[i] = apple[i] + a
 
 
for i in range(n):
    oranges[i] = int(oranges[i])
    oranges[i] = oranges[i] + b
 
#
#print(type(apple[0]))
#print(oranges)

for i in range(m):
    if (apple[i]>=s and apple[i]<=t):
        cnt1+=1
 
for i in range(n):
     if (oranges[i]>=s and oranges[i]<=t):
         cnt2+=1
 
print(cnt1)
print(cnt2)
