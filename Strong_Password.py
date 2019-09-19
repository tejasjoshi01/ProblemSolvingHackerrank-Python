# successfully  submitted


def my_function(n):
    password = str(input())

    count = 0

    bool_1 = False
    bool_2 = False
    bool_3 = False
    bool_4 = False

    for i in range(n):
        if password[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            bool_1 = True


        if password[i] in  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            bool_2 = True


        if password[i] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            bool_3 = True


        if password[i] in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']:
            bool_4 = True
            

    if (bool_1 == False):
        count += 1

    if (bool_2 == False):
        count += 1

    if (bool_3 == False):
        count += 1

    if (bool_4 == False):
        count += 1


    if ( n + count < 6):
        min = 6 - (count + n )
        print(count+min)
    else:
        print(count)




n = int(input())
my_function(n)




































#   ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#   ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']















































