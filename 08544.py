n = int(input())
for i in range(1, int(n**0.5 + 1)):
    if i*i <= n:
        print(i*i, end = " ")

#Solution with Function
def Square(n):
    for i in range(1, int(n**0.5 + 1)):
        if i*i <= n:
            print(i*i, end = " ")
        else:
            break

n = int(input())
Square(n)