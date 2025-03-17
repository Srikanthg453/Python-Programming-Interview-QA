print("Hello, World!")
"""
# Given an array of integers , every element appears twice except for one.
Find that single one.

Note: your algorithm should have a linear runtme complexity. Could you implement it without using 
extra memory ??

input = [1,2,2,3,1]
output = 3
"""
num = [ 1,2,2,8,1]
#output = 3 
di={}
temp=1
for i in num:
  if i not in di:
    di[i] = 1
  else:
    di[i]=di[i]+1

print(di)
for k,v in di.items():
  if v==1:
    print("the element is" , k)
    

# Best way to use is XOR --> ^ (if two elements same means 0, or else 1)
ans = 0
for i in range(len(num)):
  ans ^= num[i]

print(ans)