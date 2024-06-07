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

#Solution via Function
import math

n = int(input())

def IsPrime(n):
    count = 0
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                count += 1
                break  

    if count > 0:
        return False
    else:
        return True

if IsPrime(n):
    print("Yes")
else:
    print("No")