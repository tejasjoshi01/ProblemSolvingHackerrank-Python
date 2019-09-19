#submitted succesfully


n = int(input())

elements = []
elements = input().split(" ")

unique_elements = []

for i in range(len(elements)):
    elements[i] = int(elements[i])






for ele in elements:
    if ele not in unique_elements:
        unique_elements.append(ele)







pairs = 0
for i in range(len(unique_elements)):
    cnt = elements.count(unique_elements[i])
    pairs += cnt//2
print(pairs)


