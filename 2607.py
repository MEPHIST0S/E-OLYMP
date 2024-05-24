n = int(input())

first = 0
last = 0
odd = 0
even = 0

while (n > 0):
    last = n%10
    n = n//10
    even += last
    first = n%10
    n = n//10
    odd += first

print (odd * even)