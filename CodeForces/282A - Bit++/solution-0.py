n = int(input())
x = 0
for _ in range(n):
    b = input()
    if b == '++X' or b== 'X++':
        x += 1
    elif b == '--X' or b == 'X--':
        x-=1
print(x)