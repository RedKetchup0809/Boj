# 2021-05-09 boj 10818 by. 나윤재

numberList = []
N = int(input())
maximum = -1000000
minimum = 1000000

numberList = [int(x) for x in input().split()]

for x in numberList:

    if x > maximum:
        maximum = x

    if x < minimum:
        minimum = x

print(minimum , maximum)    