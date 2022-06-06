AnswerList = []
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in A:
    if i < X:
        AnswerList.append(i)
        
for i in range(len(AnswerList)):
    print(AnswerList[i], end=' ')
