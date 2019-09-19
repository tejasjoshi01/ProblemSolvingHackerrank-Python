#
#def Roman(number):
#    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
#    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
#
#    i = 12
#    while number:
#        div = number // num[i]
#        number %= num[i]
#
#        while div:
#            print(sym[i], end ='')
#            div -= 1
#        i -= 1
#
#
#
#t = int(input())
#
#for z in range(t):
#    number = int(input())
#    print(Roman(number))
#



#def printRoman(number):
#    num = [1, 4, 5, 9, 10, 40, 50, 90,
#           100, 400, 500, 900, 1000]
#    sym = ["I", "IV", "V", "IX", "X", "XL",
#                  "L", "XC", "C", "CD", "D", "CM", "M"]
#    i = 12
#    while number:
#        div = number // num[i]
#        number %= num[i]
#
#        while div:
#            print(sym[i], end = "")
#            div -= 1
#        i -= 1
#
#n = int(input())
#print(printRoman(n))

def printRoman(number):
           num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
           sym = ["I", "IV", "V", "IX", "X", "XL",
                  "L", "XC", "C", "CD", "D", "CM", "M"]
           
           op = []
           i = 12
           while number:
               div = number // num[i]
               number %= num[i]
               
               while div:
#                   print(sym[i], end = "")
                    op.append(sym[i])
                    div -= 1
               i -= 1
            opt = op
            print(opt)
# Driver code


if __name__ == "__main__":
    number = 23
#    print(printRoman(number))

