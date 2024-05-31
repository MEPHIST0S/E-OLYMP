n = int(input())

if (n < 9999):

    first = n//1000
    second = n//100%10
    third = n//10%10
    fourth = n%10

    if (first%2 == 1 or second%2 == 1 or 
        third%2 == 1 or fourth%2 == 1):
        print('YES')
    else:
        print('NO')