n = int(input())

if (n < 9999):
    first = n//1000
    second = n//100%10
    third = n//10%10
    fourth = n%10

    if ((first == second and third == fourth and first != third)
        or 
        (first == third  and second == fourth and first != second) 
        or 
        (first == fourth and second == third and first != second)):
        print("YES")
    else:
        print("NO")