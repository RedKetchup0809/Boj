T = int(input())
for t in range(T):
    result = 0
    beforeQuestion = 0
    testCase = input()
    for question in testCase:
        if question == "O":
            beforeQuestion += 1
        elif question == "X":
            beforeQuestion = 0
        result += beforeQuestion

    print(result)
