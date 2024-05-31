#Solution - 1 (70%)
"""
n = int(input())
clone = n
sum = 0
count = 0

while n > 0:
   
   while clone > 0:
      sum += clone%10 
      clone = clone//10
      
   
   print("Sum for each cycle: {}".format(sum))

   n -= sum
   
   print("Initial Number: {}".format(n))
   
   clone = n
   
   print("Clone: {}".format(clone))
   
   count += 1
   
   print("Count: {}".format(count))
   
   sum = 0

print(count)
"""
#Solution - 2 (70%)
"""
n = int(input())
count = 0

while n > 0:

    sum_of_digits = sum(int(digit) for digit in str(n))
    n -= sum_of_digits
    count += 1

print(count)
"""
#Solution - 3 (100%)