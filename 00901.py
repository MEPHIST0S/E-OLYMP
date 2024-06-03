n = input()
count = 0
if n[0] == "-" or n[0] == "+":
    count -= 1
for i in n:
    if i == "+" or i == "*" or i == "-":
        count += 1
print(count)