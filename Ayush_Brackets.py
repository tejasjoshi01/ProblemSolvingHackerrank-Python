
def check(myStr):
    open_list = ["[","{","(","<"]
    close_list = ["]","}",")",">"]
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"

t = int(input())

for i in range(t):
    bracket_seq = input()
    print(check(bracket_seq))

