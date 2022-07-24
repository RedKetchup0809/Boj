# boj 3052번 나머지

B = 42
result=set()

for i in range(10):
    A = int(input())
    result.add(A%B)

print(len(result))
