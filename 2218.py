n = int(input())
countz = 0
counto = 0

for _ in range(n):
    a = int(input())
    if (a == 0):
        countz += 1
    elif (a == 1):
        counto += 1
        
if (countz > counto):
    print(counto)
else:
    print(countz)