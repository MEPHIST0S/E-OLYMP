#Solution - 1
n = int(input())
if n < 0:
    n = abs(n)

l = n%10

while n >= 10:
    n = n//10

print(n + l)

#Solution - 2
n = input()

if n[0] == "-":
    n = n[1:]

print(n[1])