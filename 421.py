l, k = map(float, input().split())
count = 0

while l/k > 1:
    l = l/k
    count += 1

print(count)