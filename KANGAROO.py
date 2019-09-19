n = input()
values = []
values = n.split(" ")
for i in range(len(values)):
    values[i] = int(values[i])



(x1,v1,x2,v2) = (values[0],values[1],values[2],values[3])

d1 = x1+(i*v1)
d2 = x2+(i*v2)

#if(x2 > x1 and v2 > v1):
#   print("NO")



#else:
#    for i in range(1000):
#        if(x1+(i*v1) == x2+(i*v2)):
#            print("YES")
#    while(d1 != d2):
#      print("NO")
#      break



i = 0
while i < 1000:
  if(x1+(i*v1) == x2+(i*v2)):
    print("YES")
    break
  else:
    i += 1

if(x1+(i*v1) != x2+(i*v2)):
  print("NO")
