#Solution - 1 (20%)
n = input()
res = 0
n = n.split()

if n[1] == "*":
    res = int(n[0]) * int(n[2])
elif n[1] == "+":
    res = int(n[0]) * int(n[2])
elif n[1] == "-":
    res = int(n[0]) * int(n[2])
elif n[1] == "/":
    res = int(n[0]) * int(n[2])

print(int(res))

