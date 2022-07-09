
while True:
    L = [int(i) for i in input().split()]
    L.sort()
    if L[0] + L[1] + L[2] == 0:
        break
    else:
        if L[0]**2 + L[1]**2 == L[2]**2:
            print("right")
            
        else:
            print("wrong")