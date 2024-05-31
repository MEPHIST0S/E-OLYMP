import math

n = int(input())
count = 0

if n == 1:
    print("No")
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            break

    if count > 0:
        print("No")
    else:
        print("Yes")