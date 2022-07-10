A = int(input())
B = int(input())
C = int(input())

ABC= A * B * C
ABCstr = str(ABC)
ABClist = list(ABCstr)


for i in range(0, 10):
    print(ABClist.count(str(i)))
    