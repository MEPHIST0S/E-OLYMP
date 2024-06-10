#Solution - Itterative (100%)
def Factorial(num):
    res = 1
    if num == 0:
        return res
    elif num == 1:
        return res
    else:
        for _ in range (num):
            res *= num
            num -= 1
            if num == 1:
                break
        return res

n = int(input())
print(Factorial(n))

#Solution - Recursive 
def Factorial(num):
    res = 1
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * Factorial(num - 1)

n = int(input())
print(Factorial(n))