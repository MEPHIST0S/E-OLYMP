n = int(input())
if (n < 9999):
    first = n//1000
    second = n//100%10
    third = n%100//10
    fourth = n%10

    if ((first == second == third and first != fourth) or 
        (first == third == fourth and first != second) or
        (first == second == fourth and first != third) or
        (second == third == fourth and second != first)):
        print("YES")
    else:
        print("NO")