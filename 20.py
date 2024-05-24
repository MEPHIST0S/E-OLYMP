n = int(input())
num = n
sumd = 0
count = 0

while num > 0:
   sumd += num%10 
   num = num//10

while n - sumd > 0:
   n = n - sumd
   count += 1

print(count)