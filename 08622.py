n = int(input())

if (n < 9999):

    first = n//1000
    second = n//100%10
    third = n//10%10
    fourth = n%10

    if (first != 0 and second != 0 and third != 0 and fourth != 0 and 
        n%first == 0 and n%second == 0 and n%third == 0 and n%fourth == 0):
        print("YES")
    else:
        print("NO")