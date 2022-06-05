def n_power5(x):
    return(x**5)

result = 0
n = input()
for i in n:
    result += n_power5(int(i))
    
print(result)