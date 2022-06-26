Max = 0
List = []
Jayeonsu = int(input())
for i in range(1, Jayeonsu+1):
    N = int(input())
    List.append(N)
    
for i in List:
        if Max < i:
            Max = i
        Max.