"""
Maximum subarray(subsequent part of the arry) sum
arr=[-2,-3,4,-1,-2,1,5,-3]

[4] or [-1,-2] --> Subarray 
[-1,-2,5] --> not subarray , it's subsequence bcz it discontinuous

ans = 7

Brute force TC --> O(n3) and SC --> O(1) -- three for loops i=0 to n, j=i to n, i->j one loop
Better TC --> O(n2) & SC --> O(1)  -- two loops 
Optimal -- Kadane's Algo --> TC --> O(n) & SC --> O(1)
YT - take U forward DSA 

"""
arr=[-2,-3,4,-1,-2,1,5,-3]

sum = 0
start=0
maxS = -1
maxE = -1
max=0
for i in range(len(arr)):
  if sum==0:
    start=i
    
  sum += arr[i]
    
  if sum>max:
    max=sum
    maxS=start
    maxE=i
      
  if sum<0:
    sum=0

print(max)
print(maxE,maxS)
for i in range(maxS,maxE+1):
  print(arr[i])



    
