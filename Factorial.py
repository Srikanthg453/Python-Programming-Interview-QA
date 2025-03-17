"""
Write a iterative and recursive function that implements the factorial of a number.

5! = 5 * 4 * 3 * 2 * 1 
 =120
 
"""

n = 4

def ite_factorial(n):
  out=1
  for i in range(n,0,-1):
    out = out * i
  return out
    

oo=ite_factorial(n)
print(oo)

def rec_factorial(n):
  if n==0 or n== 1:
    return 1
  else:
    return n * rec_factorial(n-1)

rr = rec_factorial(n)
print(rr)