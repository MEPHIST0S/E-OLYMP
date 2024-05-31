n = int(input())

if (n < 99999):

    first = n//10000
    second = n//1000%10
    third = n//100%10
    fourth = n%100//10
    fivth = n%10

    if first < second:
        if second < third:
            if third < fourth:
                if fourth < fivth:
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")     
        else:
            print("NO")
    else:
        print("NO")