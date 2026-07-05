n, k = map(int, input().split())
a = list(map(int, input().split()))
threshold = a[k-1]
output = 0
 
for score in a:
    if score >= threshold and score > 0:
        output += 1
print(output)