n=int(input())
if (n < 9999):

    first = n//1000
    second = n//100%10
    third = n//10%10
    fourth = n%10

    if ((first == 3 and second == 7) or (second == 3 and third == 7) 
        or (third == 3 and fourth == 7)):
        print('YES')
    else:
        print('NO')