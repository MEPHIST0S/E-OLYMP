n = int(input())

if (n//1000*10 + n//100%10 == n%10*10 + n%100//10):
    print("YES")
else:
    print("NO")