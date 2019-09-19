
def binaryToDecimal(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal


t = int(input())
for i in range(t):
    b1 = int(input())
    b2 = int(input())

    c = binaryToDecimal(b1)
    d = binaryToDecimal(b2)


    if c>d:
        print("Kevin")

    if d>c:
        print("Ash")

