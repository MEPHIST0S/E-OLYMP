#Recursive (72%)
def Fibb(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return Fibb(n-2) + Fibb(n-1)

n = int(input())
print(Fibb(n))

#