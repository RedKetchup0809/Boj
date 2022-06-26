N = int(input())
min_direction = 1
max_number = 1
while True:
    if N <= max_number:
        print(min_direction)
        break
    
    max_number += min_direction * 6
    min_direction += 1