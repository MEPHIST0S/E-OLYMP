k = int(input())
n = 1

def sum(n):
    return (n*(n+1))//2

while sum(n) % k != 0:
    n += 1

print(n)