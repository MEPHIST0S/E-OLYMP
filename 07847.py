n = int(input())
arr = [int(i) for i in input().split()]
unique = set()

for i in arr:
    unique.add(i)

print(len(unique))