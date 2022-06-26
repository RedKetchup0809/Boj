x, y, w, h = map(int, input().split())
Distances = [x, y, h-y, w-x]
print(min(Distances))