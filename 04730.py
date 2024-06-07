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

#Iterative
def Fibb(curr):
    if curr == 0:
        return 1
    elif curr == 1:
        return 1
    else:
        l = [1, 1]
        for i in range(2, curr + 1):
            l.append(l[i-1]+l[i-2])
        return l[curr]

n = int(input())
print(Fibb(n))