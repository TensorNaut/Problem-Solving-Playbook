n = int(input())
solution = 0
for _ in range(n):
    lst = list(map(int, input().split()))
    if sum(lst) >= 2:
        solution += 1
    lst.clear()
print(solution)