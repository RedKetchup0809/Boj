#2884 by. 나운재 2021-05-02

def main():
    H , M = map(int, input().split())

    if M - 45 < 0:
        H = H-1
        M = M + 60

    if H < 0:
        H = 23

    M = M - 45

    print (H, M)

if __name__ == "__main__":
    main()
