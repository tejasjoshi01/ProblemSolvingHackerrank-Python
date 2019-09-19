n = int(input())

b1 = []
b2 = []
b3 = []
b4 = []
b5 = []
b6 = []



for i in range(n):
    number = int(input())
    if number < 100 :
        b1.append(number)
        b1.sort()

    if number<10000 and number>=100 :
        b2.append(number)
        b2.sort()

    if number<100000000 and number >= 10000:
        b3.append(number)
        b3.sort()

    if number<10000000000000000 and number >=100000000:
        b4.append(number)
        b4.sort()

    if number<100000000000000000000000000000000 and number >= 10000000000000000:
        b5.append(number)
        b5.sort()

    if number >= 100000000000000000000000000000000:
        b6.append(number)
        b6.sort()

total_string = b1 + b2 + b3 + b4 + b5 + b6

for i in range(len(total_string)):
    print(total_string[i])
