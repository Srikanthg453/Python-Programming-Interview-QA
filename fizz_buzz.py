"""
Given a positive interger N, print all the integers from 1 to N.

For multiples of 3 print Fizz instead of the number and for multiples of 5 pring "Buzz"
For number which are multiples of 3 and 5 print "FizzBuzz"

"""
n = 18

for i in range(1,n+1):
  if (i%3 == 0) & (i%5 == 0):
    print("FizzBuzz")
  elif i%5 == 0:
    print("Buzz")
  elif i%3 == 0:
    print("Fizz")
  else: 
    print(i)