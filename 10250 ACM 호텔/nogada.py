def room_number(H, W, N):
    count = 1
    for w in range(1, W+1):
        for h in range(1, H+1):
            if count == N:
                return h*100 + w
            count += 1
                

T = int(input())
for t in range(1, T+1):
    H, W, N = map(int, input().split())
    print(room_number(H, W, N))