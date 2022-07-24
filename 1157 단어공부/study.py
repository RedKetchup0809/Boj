def count(word):
    L = [0] * 27
    for i in word:
        L[ord(i) - ord('A') + 1] += 1
    return L

def find(L):
    max1 = 0
    max2 = 0
    for i in range(1, len(L)):
        if L[i] > L[max1]:
            max2 = max1
            max1 = i
            
        elif L[i] > L[max2]:
            max2 = i
        
    if L[max1] == L[max2]:
        # 알파벳이 여러개인 경우
        return "?"
    else:
        # 가장많은 알파벳이 있는 경우
        return chr(max1 + ord('A') - 1)

word = input()
word = word.upper()

L = count(word)
print(find(L))