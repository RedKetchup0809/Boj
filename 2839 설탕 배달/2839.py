N = int(input())
Q = N//5
R = N%5
while Q != -1:
    if R % 3 == 0:
        print(Q + R // 3)
        break
    else:
        Q -= 1
        R += 5
    if Q == -1:
        print(-1)