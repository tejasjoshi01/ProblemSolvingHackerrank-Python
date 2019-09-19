
#submitted succesfully

(elements , posn ) = input().split(" ")
(elements , posn ) = ( int(elements) , int(posn) )

ele = []
ele_st = input("").split(" ")
ele = ele_st
for i in range(len(ele)):
    ele[i] = int(ele[i])

anna = int(input())

ele.remove(ele[posn])

sum = 0
for i in range(len(ele)):
    sum += ele[i]

if  anna - sum*0.5 == 0 :
    print('Bon Appetit')
else:
    print(anna - sum*0.5)
