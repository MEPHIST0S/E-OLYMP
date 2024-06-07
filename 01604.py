n = input()
product = 1
condition = False

for i in range (len(n)):
    if n[i] != "-":
        if int(n[i]) % 2 == 0:
            product *= int(n[i])
            condition = True

if condition:
    print(product)
else:
    print(-1)