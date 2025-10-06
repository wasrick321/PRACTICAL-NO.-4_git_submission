def MaxSubArray(A,low,high):
if low==high:
return A[low]
mid=(low+high)//2
left=MaxSubArray(A,low,mid)
right=MaxSubArray(A,mid+1,high)
cross=MaxCrossSubArray(A,low,mid,high)
return max(left,right,cross)
def MaxCrossSubArray(A,low,mid,high):
leftSum=-1
sum=0
for i in range(mid,low-1,-1):
sum+=A[i]
if sum>leftSum:
leftSum=sum
rightSum=-1
sum=0
for j in range(mid+1,high+1):
sum+=A[j]
if sum>rightSum:
rightSum=sum
return leftSum+rightSum
A = [2, -4, 3, -1, 5, -6]

print("Array:", A)
print("Maximum element is:", max(A))
