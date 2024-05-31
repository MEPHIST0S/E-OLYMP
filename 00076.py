a, b, x, y, z = map(int, input().split())
if (0 < a < 10 and 0 < b < 10 and 0 < x < 10 and 
   0 < y < 10  and 0 < z < 10):
    if ((a > x and b > y) or (a > y and b > x) or 
       (a > y and b > z) or (a > z and b > y) or
       (a > x and b > z) or (a > z and b > x)):
        print(1)
    else:
        print(0)