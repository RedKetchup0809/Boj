numbers = []

for i in range(9):
    a = int(input())
    numbers.append(a)

chadatgab_index = 0
chadatgab = 0
for i in range(0, 9):
    if numbers[i] > chadatgab:
        chadatgab = numbers[i]
        chadatgab_index = i + 1

print(chadatgab)
print(chadatgab_index)