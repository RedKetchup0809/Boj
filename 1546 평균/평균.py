N = int(input())
원래점수 = list(map(int, input().split()))
최고점수 = max(원래점수)
def 변환(원래점수):
    return 원래점수/최고점수 * 100
새점수 = list(map(변환, 원래점수))

print(sum(새점수) / N)
    